import cv2
faces_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade=cv2.CascadeClassifier("haarcascade_smile.xml")
photo_name=input("tell us the name of photo: ")
img=cv2.imread(photo_name)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=faces_cascade.detectMultiScale(img,1.5,5)
#eyes=eye_cascade.detectMultiScale(imgGray,1.5,2)
#smiles=smile_cascade.detectMultiScale(imgGray,1.5,2)
for x,y,w,z in faces[:]:
    cv2.rectangle(img,(x,y),(x+w,y+z),(0,225,0),2) 
    saved_faced=img[y:y+z,x:x+w]
    face_name="faces.png"
    cv2.imwrite(face_name,saved_faced)

# while True:
#     imgvid=cap
# #for x,y,w,z in eyes[:]:
# #    cv2.rectangle(img,(x,y),(x+w,y+z),(0,225,0),2) 
#     #saved_faced=imgGray[y:y+z,x:x+w]
#     #face_name="eyes.png"
#     #cv2.imwrite(face_name,saved_faced)

# #for x,y,w,z in smiles[:]:
# #    cv2.rectangle(img,(x,y),(x+w,y+z),(0,225,0),2) 
#     #saved_faced=imgGray[y:y+z,x:x+w]
#     #face_name="smile.png"
#     #cv2.imwrite(face_name,saved_faced)
cv2.imshow("face detector",img)


cv2.waitKey(0)
