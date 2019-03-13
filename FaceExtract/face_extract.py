import cv2
import sys
import os
import argparse

CASCADE = "Face_cascade.xml"


dim = (48, 48)
FACE_CASCADE = cv2.CascadeClassifier(CASCADE)

ap = argparse.ArgumentParser()

ap.add_argument("-s", "--file", required=True, type=str, help="path to folder contening files")

ap.add_argument("-d", "--dest", required=True, type=str, help="destination path of Extracted data")

args = vars(ap.parse_args())

temp = 0
if not args["dest"] in os.listdir("."):
    os.mkdir(args["dest"])
else:
    pass


directory = os.fsencode(args["file"])

for file in os.listdir(directory):
    filename = args["file"] + os.fsdecode(file)

    image = cv2.imread(filename)
    # print(image)
    # cv2.imshow("data", image)

    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = FACE_CASCADE.detectMultiScale(image_grey, scaleFactor=1.16, minNeighbors=5, minSize=(25, 25), flags=0)
    for x, y, w, h in faces:
        sub_img = image[y - 10:y + h + 10, x - 10:x + w + 10]
        os.chdir(args["dest"])
        temp = temp + 1
        sub_img = cv2.resize(sub_img, dim, interpolation=cv2.INTER_AREA)

        sub_img = cv2.cvtColor(sub_img, cv2.COLOR_BGR2GRAY)

        cv2.imwrite("0000" + str(temp) + ".jpg", sub_img)
        print("image in process " + str(temp))
        os.chdir("../")
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
