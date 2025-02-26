import cv2
import os
import string

img = cv2.imread("encryptedImage.png")

with open("encryptionDetails.txt", "r") as file:
    lines=file.readlines()

passcode = lines[0].strip('\n') #The passcode is the first line of the encryptionDetails file
msgLength = lines[1].strip('\n') #The message length is the second line of the encryptionDetails file

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

message = ""
n = 0
m = 0
z = 0

userInput = input("Enter passcode for decryption: ")
if passcode == userInput:
    for i in range(int(msgLength)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decrypted message: ", message)
else:
    print("Invalid passcode")
