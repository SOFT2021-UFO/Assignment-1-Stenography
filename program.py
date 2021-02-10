from PIL import Image

img = Image.open("./image.png")
width, height = img.size #Returns width and height

extractedBits = []
extractedBytes = []

for x in range(0, height) :
    for y in range(0,width) : 
        extractedBits.append(str(img.getpixel((y,x))[2]&1)) #Get blue value and append it to extractedBits (least significant one)
for i in range(0,len(extractedBits),8):
    extractedBytes.append("".join(extractedBits[i:i+8][::-1]))

result = ""
for byte in extractedBytes :
    if byte != "00000000" :
        result += chr(int(byte,2)) #Convert bytes to integer with base 2 (There are only two, 0 or 1)
    else :
        break

print(result)