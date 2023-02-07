#!/usr/bin/env python3

import cv2
import face_recognition
import datetime


def face_analize():
    # Image to compare
    image = cv2.imread("/home/luffy/Pictures/Screenshots/me.png")
    face_loc = face_recognition.face_locations(image)[0]
    print("face_loc: ", face_loc)
    # Vector with 128 features
    face_image_encodings = face_recognition.face_encodings(
            image,
            known_face_locations=[face_loc]
            )[0]
    print("face_encodings: ", face_image_encodings)

    flag = 0
    # Video streaming
    video_capture = cv2.VideoCapture(0)
    
    start_time = datetime.datetime.now()
    # end time is 10 sec after the current time
    end_time = start_time + datetime.timedelta(seconds=10)
    # Run the loop till current time exceeds end time
    while end_time > datetime.datetime.now():
        ret, frame = video_capture.read()
        if ret == False:
            break
        frame = cv2.flip(frame, 1)

        face_locations = face_recognition.face_locations(frame)
        if face_locations != []:
            for face_location in face_locations:
                face_frame_encodings = face_recognition.face_encodings(
                        frame,
                        known_face_locations=[face_location])[0]
                result = face_recognition.compare_faces([face_image_encodings], face_frame_encodings)
                print("Result: ", result)
                if result[0] == True:
                    text = "Smith"
                    color = (125, 220, 0)
                    flag = 1
                else:
                    text = "Unknow"
                    color = (50, 50, 255)

                cv2.rectangle(frame,
                            (face_location[3], face_location[0]),
                            (face_location[1], face_location[2]),
                            color,
                            2)

                cv2.rectangle(frame,
                            (face_location[3], face_location[2]),
                            (face_location[1], face_location[2] + 30),
                            color,
                            -1)
                cv2.putText(frame, text, (face_location[3], face_location[2] + 20),
                            2,
                            0.7,
                            (255, 255, 255),
                            1)
        cv2.imshow('Frame', frame)
        k = cv2.waitKey(1)
        if k == 27 & 0xFF:
            break
    video_capture.release()
    cv2.destroyAllWindows()
    if flag == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    face_analize()
