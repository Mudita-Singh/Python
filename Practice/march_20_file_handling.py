file = open("file.txt" , "rb")
print(file)


file = open("File.txt" , "wb")
print("Name of the file: " , file.closed)
print("file has been opened" , file.mode ,"mode" )


file = open("file.txt" , "w")
file.write("Hello All  , hope yor are learning python")
file.close()
print("Data written into the file")


file = open("file.txt" , "rb")
print("position of file pointer before reading is " , file.tell())
print(file.read(10))
print("position of file pointer after reading is:" , file.tell())
print("setting 3 bytes from the current position of file pointer")
file.seek(3, 1)
print(file.read())
file.close()




