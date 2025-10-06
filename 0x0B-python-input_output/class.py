with open("output.txt", "br+") as file:
    seek_value = 0
    for i in range(5):
        line = file.readline()
        file.seek(len(file.readline()), 1)
        print(line, file.tell())
        file.write(b"\nThis is me\n")

        #print(file.tell())

        #if "Python" in line:
            #file.write("This is me")
            # Try to ask AI why this code is not writing
            # multiple times inside the file
            # and just writing a single time at the end of the file