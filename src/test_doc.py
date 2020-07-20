
# "E:\\Temp\\geodex_test\\1\\INFO.doc"

# import transform_doc
#
# YOUR_DOC = "E:\\Temp\\geodex_test\\1\\INFO.doc"
# with open(YOUR_DOC, "rb") as fp:
#     content = fp.read()
#
# txt = transform_doc.transform_doc_stream(content)
# print(txt)

# import textract
# text = textract.process("E:\\Temp\\geodex_test\\1\\INFO.doc")
# print(text)
import codecs
import olefile
YOUR_DOC = "/Users/glory/projects/geodex_test/1/INFO.doc"
assert olefile.isOleFile(YOUR_DOC)
ole = olefile.OleFileIO(YOUR_DOC)
print(ole.listdir())
if ole.exists('worddocument'):
    print("This is a Word document.")
    t = ole.get_type('WordDocument')
    print(t)
    data = ole.openstream('WordDocument').read()
    data.decode()
    print(data)
    #data.decode('cp1251','ignore')
    #.encode('utf8')
    print(str(data))
    # data2 = str(data, 'cp1251')
    data2=codecs.decode(data, encoding='cp1251', errors='ignore')
    print(data2)
    # meta = ole.get_metadata()
    # print('Author:', meta.author)
    # print('Title:', meta.title)
    # print('Creation date:', meta.create_time)
    # # print all metadata:
    # meta.dump()

