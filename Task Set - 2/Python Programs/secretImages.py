files = input("Enter file names separated by spaces : ")
names = files.split(" ")
png = 0
bmp = 0
jpeg = 0
for i in names:
    if i.endswith(".png"):
        png += 1
    elif i.endswith(".jpeg"):
        jpeg += 1
    elif i.endswith(".bmp"):
        bmp += 1

print(png, bmp, jpeg)