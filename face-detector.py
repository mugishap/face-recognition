import opencv1
faces_cascade=opencv1.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=opencv1.CascadeClassifier("haarcascade_eye.xml")
smile_cascade=opencv1.CascadeClassifier("haarcascade_smile.xml")
photo_name=input("tell us the name of photo: ")
img=opencv1.imread(photo_name)
imgGray=opencv1.cvtColor(img,opencv1.COLOR_BGR2GRAY)
​
faces=faces_cascade.detectMultiScale(img,1.5,5)
#eyes=eye_cascade.detectMultiScale(imgGray,1.5,2)
#smiles=smile_cascade.detectMultiScale(imgGray,1.5,2)
for x,y,w,z in faces[:]:
    opencv1.rectangle(img,(x,y),(x+w,y+z),(0,225,0),2) 
    saved_faced=img[y:y+z,x:x+w]
    face_name="faces.png"
    opencv1.imwrite(face_name,saved_faced)
​
# while True:
#     imgvid=cap
# #for x,y,w,z in eyes[:]:
# #    opencv1.rectangle(img,(x,y),(x+w,y+z),(0,225,0),2) 
#     #saved_faced=imgGray[y:y+z,x:x+w]
#     #face_name="eyes.png"
#     #opencv1.imwrite(face_name,saved_faced)
​
# #for x,y,w,z in smiles[:]:
# #    opencv1.rectangle(img,(x,y),(x+w,y+z),(0,225,0),2) 
#     #saved_faced=imgGray[y:y+z,x:x+w]
#     #face_name="smile.png"
#     #opencv1.imwrite(face_name,saved_faced)
opencv1.imshow("face detector",img)
​
​opencv1.waitKey(0)