#Program copies images
f1=open("tony.jpg","rb")
f2=open("RDJ.jpg","wb")
bytes_data = f1.read()
print(bytes_data)
f2.write(bytes_data)
f2.close()
print("new image is available with name:\t",f2.name)
f1.close()
