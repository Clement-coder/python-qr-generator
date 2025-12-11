import qrcode

url = input("enter text or url")

img = qrcode.make(url)

img.save('qrcode.png')
print('qrcode created succesfully !! ')