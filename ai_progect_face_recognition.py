import face_recognition
import cv2
import numpy as np
video_capture = cv2.VideoCapture(0)
Utkarsh_Saxena = face_recognition.load_image_file("/home/anirudh/Documents/Projects/2nd_year_project/Person Identification Model/Utkarsh Saxena/utkarsh.jpeg")
Utkarsh_Saxena_face_encoding = face_recognition.face_encodings(Utkarsh_Saxena)[0]
Ajmal_Khan = face_recognition.load_image_file("/home/anirudh/Documents/Projects/2nd_year_project/Person Identification Model/Ajmal Khan/Ajmal.jpeg")
Ajmal_Khan_face_encoding = face_recognition.face_encodings(Ajmal_Khan)[0]
Anirudh_Lodh = face_recognition.load_image_file("/home/anirudh/Documents/Projects/2nd_year_project/Person Identification Model/Anirudh Lodh/Anirudh Lodh.jpeg")
Anirudh_Lodh_face_encoding = face_recognition.face_encodings(Anirudh_Lodh)[0]
known_face_encodings = [Utkarsh_Saxena_face_encoding,Ajmal_Khan_face_encoding,Anirudh_Lodh_face_encoding ]
known_face_names = ["Utkarsh Saxena","Ajmal Khan","Anirudh Lodh"]
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
    process_this_frame = not process_this_frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 3
        right *= 5
        bottom *= 5
        left *= 3
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
