from init import *
play(start_detection)
while True:
    ret, img = cap.read()
    #img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,    
        scaleFactor=1.2,
        minNeighbors=5,    
        minSize=(20, 20)
    )
    
    if not faces == ():
        High()
        play(captured)
        #for (x,y,w,h) in faces:
           # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            #roi_gray = gray[y:y+h, x:x+w]
            #roi_color = img[y:y+h, x:x+w] 
        filename = time.strftime("%Y-%m-%d-%H:%M:%S")+'.png'
        cv2.imwrite('./dataset/'+filename,img)
        print filename+" saved with\n"+str(faces)
        play(saved)
        for i in range(10):
            ret, img = cap.read()
            cv2.imshow('video',img)    
        Low()
    cv2.imshow('video',img)    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()