import face_recognition

known_image = face_recognition.load_image_file("enrico_mentana.jpg")
unknown_image = face_recognition.load_image_file("other.jpg")

known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(known_image)[0]

results = face_recognition.compare_faces([known_encoding], unknown_encoding)
answer = "Yes" if results[0] else "No"

print(
    f"The unknown image shows the popular Italian journalist, Enrico Mentana? { answer }"
)

