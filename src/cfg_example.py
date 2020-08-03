# please rename this file to cfg.py
from time import strftime   # Load just the strftime Module from Time

file_csv = str(strftime("%Y-%m-%d") + "_from_csv" + ".csv")
file_log = str(strftime("%Y-%m-%d") + "_from_csv" + ".log")

folder_in_win = 'Z:\\'
#folder_win_in = 'E:\\Temp\\'
folder_in_linux = '/Users/glory/projects/CSV_ALL'

folder_out_win = 'E:\\TEMP\\'
folder_out_linux = '/Users/glory/projects/out'

csv_delimiter = ';'


csv_dict = {'FULLNAME': '',
                'NAME': '',
                'DISK': '',
                'CNT': '',
                'COLUMNS': '',
                'MAXDELIM': ''
                }
