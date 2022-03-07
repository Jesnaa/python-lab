def fread(fname):
    with open(fname) as f:
        c = f.readlines()
    print(c)
fread("file")
