import pyqrcode


url = input("Enter Url to generate qe code : ")

qr_code = pyqrcode.create(url)
qr_code.svg("qrcode.svg",scale=5)


