import os
import face_recognition  
import cv2 as cv
import math
import numpy as np 
from Press import login 

def face_confidence(face_distance,face_match_threshold=0.6):
    range=(1.0-face_match_threshold)
    linear_val=(1.0-face_distance)/(range*2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val*100,2))+"%"
    else: 
        value=(linear_val+((1.0-linear_val) * math.pow((linear_val-0.5),0.2)))*100
        return str(round(value,2))+"%"



class ReconnaissanceFaciale():
    face_locations=[]
    face_encodings=[]
    face_names=[]
    known_faces_encodings=[]
    known_faces_names=[]
    process_current_frame=True



    def __init__(self):
        pass

    def face_encoding(self):
        for image in os.listdir("Faces"):
            face_image=face_recognition.load_image_file(f'Faces/{image}')
            #print(face_image)
            face_encoding=face_recognition.face_encodings(face_image)[0]
            #print(face_encoding)
            self.known_faces_encodings.append(face_encoding)
            self.known_faces_names.append(image)
        print("These are the known faces and its encodings !")
        # print(self.known_faces_encodings)
        # print(self.known_faces_names)


    def run_recognition(self):
        video_capture=cv.VideoCapture(0)

        if not video_capture.isOpened():
            
            sys.exit("Video source not found !")

        while True :
            check, frame=video_capture.read()
            if self.process_current_frame:
                small_frame=cv.resize(frame,(0,0),fx=0.25,fy=0.25)
                rgb_small_frame=small_frame[:,:,::-1]

                #finding all faces in the current frame 
                self.face_locations=face_recognition.face_locations(rgb_small_frame)
                self.face_encodings=face_recognition.face_encodings(rgb_small_frame,self.face_locations)
                self.face_names=[]
                for face_encoding in self.face_encodings:
                    matches=face_recognition.compare_faces(self.known_faces_encodings,face_encoding) 
                    name="Unknown"
                    confidence="unKnown"
                    face_distances = face_recognition.face_distance(self.known_faces_encodings,face_encoding)
                    best_match_index=np.argmin(face_distances)
                    if matches[best_match_index]:
                        name=self.known_faces_names[best_match_index]
                        confidence=face_confidence(face_distances[best_match_index])
                        if name=="anas ben raies.jpg":
                            login()
                            return True
                    self.face_names.append(f'{name} ({confidence})')
            self.process_current_frame=not self.process_current_frame
            for (top ,right ,bottom,left) , name in zip(self.face_locations,self.face_names):
                top*=4
                right*=4
                bottom*=4
                left*=4

                cv.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
                cv.rectangle(frame,(left,bottom-25),(right,bottom),(0,0,255),-1)
                cv.putText(frame,name,(left+6,bottom-6),cv.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),1)

            cv.imshow("Face Recognition",frame)
            key=cv.waitKey(1)
            
            #aaa
            if key == 27 :
                break
        video_capture.release()
        cv.destroyAllWindows()


    

    


fr=ReconnaissanceFaciale()
fr.face_encoding()
fr.run_recognition()

