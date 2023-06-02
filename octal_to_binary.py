def octtobin(o):
    return bin(int(o,8))
octnum=input()
binnum=octtobin(octnum)
print(binnum[2:])