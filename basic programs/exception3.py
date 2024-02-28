try:
    klu1=open("file.txt","r+")
    try:
        klu1.write("xyzThis is S17 Section CRT Class")
    finally:
        klu1.close()
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    klu1.close()