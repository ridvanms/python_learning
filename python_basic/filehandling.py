someText = open("someText.txt")
print(someText.read())
someText.close()
#
# f = open("newFile.txt",'a')
# f.write("Hello this is the new file that i just wrote")
# f.close()

# import os
# try:
#     os.remove("newFile.txt")
#     print("a file with name newFile was successfully ware deleted")
# except:
#     print("a file with such name does not exists!")