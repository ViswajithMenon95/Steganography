import cv2
import os
import string

img = cv2.imread("image.jpg")

msg = input("Enter the secret message: ")
passcode = input("Enter the passcode: ")
f = open("encryptionDetails.txt", "w")
f.write(passcode + '\n') #Store the passcode as the first line in the encryptionDetails file
f.write(str(len(msg))) #Store the message length as the second line in the encryptionDetails file
f.close()

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")
