from qrtools.qrtools import QR

qr = QR()
file = qr.decode("challenges.hackvent.hacking-lab.com.png")
print(file.data)