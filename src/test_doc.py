
# "E:\\Temp\\geodex_test\\1\\INFO.doc"

# import transform_doc
#
# YOUR_DOC = "E:\\Temp\\geodex_test\\1\\INFO.doc"
# with open(YOUR_DOC, "rb") as fp:
#     content = fp.read()
#
# txt = transform_doc.transform_doc_stream(content)
# print(txt)

import textract
text = textract.process("E:\\Temp\\geodex_test\\1\\INFO.doc")
print(text)