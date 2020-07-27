#import time
from time import strftime   # Load just the strftime Module from Time

file_csv = str(strftime("%Y-%m-%d") + "_from_csv" + ".csv")
file_log = str(strftime("%Y-%m-%d") + "_from_csv" + ".log")

folder_in_win = 'Z:\\'
#folder_win_in = 'E:\\Temp\\geodex_test'
folder_in_linux = '/Users/glory/projects/CSV_ALL'

folder_out_win = 'E:\\TEMP\\info.doc\\'
folder_out_linux = '/Users/glory/projects/out'


# host = 'localhost'
# schema = 'udataschema'
# user = 'udatauser'
# user_password = 'udatauserpassword'
# database = 'udatadb'
# postgresql://udatauser:udatauserpassword@localhost:5432/udatadb

csv_delimiter = ';'

#csv_fieldnames_in = ["compname","FullName","Length","CreationTime"]

# csv_dict = {'COMPNAME': '',
#             'DISK': '',
#             'FOLDER': '',
#             'FILENAME_LONG': '',
#             'FILENAME_SHOT': '',
#             'EXT_LONG': '',
#             'EXT_SHOT': '',
#             'SIZE': '',
#             'FULLNAME': '',
#             'DATE': '',
#             'YEAR': '',
#             'MONTH': '',
#             'CREATIONTIME': '',
#             'FIO': '',
#             'OTDEL': '',
#             'TEXTFULL': '',
#             'TEXTLESS': '',
#             'LASTUPDATE': ''}

csv_dict = {'FULLNAME': '',
                'NAME': '',
                'DISK': '',
                'CNT': '',
                'COLUMNS': '',
                'MAXDELIM': ''
                }
