#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          :   Viacheslav Zamaraev
#   email           :   zamaraev@gmail.com
#   Script Name     : 01_check_info_files.py
#   Created         : 13th July 2020
#   Last Modified	: 13th July 2020
#   Version		    : 1.0
#   PIP             : pip install
#   RESULT          : csv file with columns: FILENAME;...LASTACCESS
# Modifications	: 1.1 -
#               : 1.2 -
#
# Description   : get count lines in each csv fle in folder

import os  # Load the Library Module
import os.path
import sys
import time
from sys import platform as _platform
from time import strftime  # Load just the strftime Module from Time
from datetime import datetime
import csv
import codecs
import logging
#from itertools import (takewhile,repeat)

# non standard packages
# try:
#     import peewee
# except Exception as e:
#     print("Exception occurred " + str(e), exc_info=True)
#     print("try: pip install peewee")


import cfg  # some global configurations



def get_input_directory_from_cfg():
    directory_in = str(os.getcwd())
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        if os.path.isdir(cfg.folder_in_linux):
            print('Input directory from a config file: ' + cfg.folder_in_linux)
            return cfg.folder_in_linux
        else:
            print('Input directories from config wrong: ' + cfg.folder_in_linux + ' Using current directory: ' + directory_in)
            return directory_in
    if _platform == "win32" or _platform == "win64":  # Windows or Windows 64-bit
        if os.path.isdir(cfg.folder_in_win):
            print('Input directory from a config file: ' + cfg.folder_in_win)
            return cfg.folder_in_win
        else:
            print('Input directories from config wrong: ' + cfg.folder_in_win + ' Using current directory: ' + directory_in)
            return directory_in
    return directory_in


def get_input_directory():
    # get from config
    directory_in = str(os.getcwd())
    # if only run the script (1 argument)
    if len(sys.argv) == 1:  # there is no arguments in command line
        return get_input_directory_from_cfg()

    if len(sys.argv) == 2:  # there is only one argument in command line
        directory_in = str(sys.argv[1:][0])
        if os.path.isdir(directory_in):
            return directory_in
        else:
            return get_input_directory_from_cfg()

    if len(sys.argv) > 2:  # there is only one argument in command line
        print("Arguments much more than 1! Please use only path as an argument. (Script.py /mnt/some_path) ")
        print(sys.argv, len(sys.argv))
        exit(1)
    return directory_in


def get_output_directory():
    dir_out = str(os.getcwd())
    # Linux platform
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        dir_out = cfg.folder_linux_out
        print('Output directory from config file: ' + dir_out)
        if os.path.exists(dir_out) and os.path.isdir(dir_out):
            return dir_out
    if _platform == "win32" or _platform == "win64":  # Windows or Windows 64-bit
        dir_out = cfg.folder_win_out
        print('Output directory from config file' + dir_out)
        if os.path.exists(dir_out) and os.path.isdir(dir_out):
            return dir_out
    else:
        print(
            'Output directories from config wrong: ' + cfg.folder_out_win + ' or ' + cfg.folder_out_linux + ' Using current directory: ' + dir_out)
    print('Using Output directory: ' + dir_out)
    return dir_out

def get_extension(filename=''):
    basename = os.path.basename(filename)  # os independent
    ffile = filename.split('\\').pop().split('/').pop()
    ext = '.'.join(ffile.split('.')[1:])

    if len(ext):
        return '.' + ext if ext else None
    else:
        return ''


def get_file_name_with_extension(path=''):
    #ext = get_extension(path)
    return os.path.split(path)[1]
    # if len(ext):
    #     return path.split('\\').pop().split('/')[0]
    # else:
    #     return path.split('\\').pop().split('/').pop()

    # return path.split('\\').pop().split('/')[0]        #  path.split('\\').pop().split('/').pop().rsplit('.', 1)[0]


def get_file_name_without_extension(path=''):
    ext = get_extension(path)
    if len(ext):
        return path.split('\\').pop().split('/').pop().rsplit(ext, 1)[0]
    else:
        return path.split('\\').pop().split('/').pop()
    #return path.split('\\').pop().split('/').pop().rsplit(get_extension(path), 1)[0]



def rawincount(filename):
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))
    return sum( buf.count(b'\n') for buf in bufgen )



'''
    Do many csv files and make one csv file big
'''
def do_csv_file_in_dir_out_csv(filename_with_path=''):
    csv_dict = {'FULLNAME': '',
                'NAME': '',
                'CNT': ''
                }

    file_csv = str(os.path.join(get_output_directory(), cfg.file_csv))
    #file_name = filename_with_path.split('.')[0]
    file_name = get_file_name_with_extension(filename_with_path)
    #csv_dict = cfg.csv_dict
    for key in csv_dict:
        csv_dict[key] = ''
    # csv_dict['DATA_SCRIPT_RUN'] = str(time.strftime("%Y-%m-%d"))
    csv_dict['FULLNAME'] = filename_with_path
    csv_dict['NAME'] = file_name.split('-')[0]
    csv_dict['CNT'] = '' #rawincount(filename_with_path)

    with open(file_csv, 'a', newline='', encoding='utf-8') as csv_file:  # Just use 'w' mode in 3.x
        csv_file_open = csv.DictWriter(csv_file, csv_dict.keys(), delimiter=cfg.csv_delimiter)

        try:
            print(csv_dict['FULLNAME'])
            csv_file_open.writerow(csv_dict)
        except Exception as e:
            print("Exception occurred " + str(e))  # , exc_info=True


def get_list_csv_dir(dir_input=''):
    csv_dict = {'FULLNAME': '',
                'NAME': '',
                'CNT': ''
                }
    listdir = []
    # Если выходной CSV файл существует - удаляем его
    file_csv = str(os.path.join(get_output_directory(), cfg.file_csv)) # from cfg.file
    if os.path.isfile(file_csv):
        os.remove(file_csv)

    with open(file_csv, 'w', newline='', encoding='utf-8') as csv_file:  # Just use 'w' mode in 3.x
        csv_file_open = csv.DictWriter(csv_file, csv_dict.keys(), delimiter=cfg.csv_delimiter)
        csv_file_open.writeheader()
    try:
        for root, subdirs, files in os.walk(dir_input):
            for file in os.listdir(root):
                file_path = str(os.path.join(root, file))
                #.lower() - под линуксом есть разница!!!
                ext = '.'.join(file.split('.')[1:]).lower()
                file_name = file.lower()


                if os.path.isfile(file_path) and file_name.startswith('info.doc'):     #ext == "csv":
                    print(file_path)
                    listdir.append(file_path)
    except Exception as e:
        print("Exception occurred get_list_csv_dir" + str(e))

    return listdir


##let try multithreading

def do_multithreading(dir_input=''):

    list_csv = get_list_csv_dir(dir_input)

    # try:
    #     from multiprocessing import Pool
    # except Exception as e:
    #     print("Exception occurred do_multithreading" + str(e))
    # try:
    #     # кол-во потоков
    #     with Pool(1) as p:
    #          p.map(do_csv_file_in_dir_out_csv, list_csv)
    # except Exception as e:
    #     print("Exception occurred do_multithreading" + str(e))

    for f in list_csv:
        do_csv_file_in_dir_out_csv(f)

    # #map(save_file_html_by_url, url_list)


def do_log_file():
    for handler in logging.root.handlers[:]:  # Remove all handlers associated with the root logger object.
        logging.root.removeHandler(handler)
    dir_out = get_output_directory()
    file_log = str(os.path.join(dir_out, cfg.file_log))  # from cfg.file
    if os.path.isfile(file_log):     # Если выходной LOG файл существует - удаляем его
        os.remove(file_log)
    logging.basicConfig(filename=file_log, format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG,
                        filemode='w')  #
    logging.info(file_log)


# ---------------- do main --------------------------------
def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    dir_input = get_input_directory()

    do_log_file()

    do_multithreading(dir_input)


    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == '__main__':
    main()
