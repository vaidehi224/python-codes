def file_read(filename):
        content_array = []
        with open(filename) as f:     
                for line in f:
                        content_array.append(line)
                print(content_array)
file_read("file.txt")
