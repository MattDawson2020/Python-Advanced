# code for the easy front on face
import cv2

face_casecade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("photo.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_casecade.detectMultiScale(gray_img, 
scaleFactor=1.05,
minNeighbors=5)

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)

print(faces)

cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows
#this code returns a clear green rectangle around the face, showing that it works


# code for the second harder to detect face

img2=cv2.imread("news.jpg")
gray_img2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

faces2=face_casecade.detectMultiScale(gray_img2, 
scaleFactor=1.05,
minNeighbors=5)

for x, y, w, h in faces2:
    img=cv2.rectangle(img2, (x, y), (x+w, y+h), (0,255,0), 3)

print(faces2)

cv2.imshow("Gray", img2)
cv2.waitKey(0)
cv2.destroyAllWindows
# this code is able to find the womans face on the left, but is unable to find the mans on the right.
# possibly due to eyes closed, missing chin, angle etc