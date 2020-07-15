#import time
from time import strftime   # Load just the strftime Module from Time

file_csv = str(strftime("%Y-%m-%d") + "_from_csv" + ".csv")
file_log = str(strftime("%Y-%m-%d") + "_from_csv" + ".log")

folder_win_in = 'Z:\\'
#folder_win_in = 'E:\\Temp\\geodex_test'
folder_linux_in = '/Users/glory/projects/geodex_test'
#folder_linux_in = '/Users/glory/Desktop/Dropbox/MyPrj/GitHubProjects/udata_load/examples/in'


folder_win_out = 'E:\\TEMP\\info.doc\\'
folder_linux_out = '/Users/glory/projects/geodex_test/out'


host = 'localhost'
schema = 'udataschema'
user = 'udatauser'
user_password = 'udatauserpassword'
database = 'udatadb'
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

csv_dict = {'FOLDER': '',
            'LASTUPDATE': ''}
