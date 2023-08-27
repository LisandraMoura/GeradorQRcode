import pyqrcode

code = pyqrcode.create("https://forms.gle/G6NgVS4tDW8ucUor8")

code.png("code.png", scale=8)

if code != 0:
    print("Qr code gerado!")

