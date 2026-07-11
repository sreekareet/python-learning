#with is like a try catch block, it will automatically close the file after the block is executed(like RAII in c++)

#create a file and write to it
with open("test.txt", "w") as f:
    f.write("host = 127.0.0.1\n ")
    f.write("port=7379\n")
    f.write("timeout=30\n")

print("file written")

#read from a file
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())

config = {}
with open("test.txt", "r") as f:
    for line in f:
        line = line.strip()
        key, value = line.split("=")
        config[key.strip()] = value.strip()

print (config)
config["port"] = int(config["port"])  #convert string to int
config["timeout"] = int(config["timeout"])  #convert string to int
print (type(config["port"]))

#exception handling
try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found - using defaults ")
except PermissionError:
    print("no permission to read file ")

