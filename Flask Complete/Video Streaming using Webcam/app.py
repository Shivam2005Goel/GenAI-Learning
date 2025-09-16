from flask import Flask,render_template,Response
import cv2
import face_recognition
import numpy as np

app = Flask(__name__)
camera = cv2.VideoCapture(0)


def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
            rgb_small_frame = small_frame[:,:,::-1]
    
            if process_this_frame:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                    face_names.append(name)
            process_this_frame = not process_this_frame
            
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

                    # face_cascade = cv2.CascadeClassifier("./haar-cascade-files/haarcascade_frontalface_default.xml")
                    # eye_cascade = cv2.CascadeClassifier("./haar-cascade-files/haarcascade_eye.xml")

                    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    # faces = face_cascade.detectMultiScale(gray, 1.1, 7)     
                    #Draw the Rectangle around each face
                    # for(x,y,w,h) in faces:
                    #     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                    #     roi_gray = gray[y:y+h,x:x+w]
                    #     roi_color = frame[y:y+h,x:x+w]
                    #     eyes = eye_cascade.detectMultiScale(roi_gray,1.1,3)
                    #     for(ex,ey,ew,eh) in eyes:
                    #         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)



            ret,buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

           

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype = 'multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug = True)





