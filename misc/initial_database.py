import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceattendance-9c4cc-default-rtdb.firebaseio.com/',
    'storageBucket': "faceattendance-9c4cc.appspot.com"
})

ref = db.reference(
    "Students"
)  # reference path to our database... will create student directory in the database

data = {
    "22CA0052": {  
        "id": "22CA0052",
        "name": "K Tarun",
        "password": "Tarun@123",
        "dob": "2002-11-05",
        "address": "Dollygunj, Port Blair",
        "phone": "8900917763",
        "email": "kt9684512@gmail.com",
        "Degree": "Computer Science",
        "starting_year": 2022,
        "CGPA": 7.00,
        "total_attendance": 4,
        "Web_Tech": 0,
        "Web_Attendance": "2024-09-17 12:33:10",
        "SoftWare_Testing": 0,
        "Software_Attendance": "2024-09-16 12:33:10",
        "Accounting_Tools": 0,
        "Acc_Attendance": "2024-09-13 12:33:10",
        "Curr_year": 3,
        "last_attendance_time": "2024-09-17 12:33:10",
        "Notice": "Information or any Notice given out to students",

    },
    "22CA0053": {  
        "id": "22CA0053",
        "name": "Vishakha Sapkal",
        "password": "12345678",
        "dob": "2004-07-08",
        "address": "Port Blair",
        "phone": "8900973980",
        "email": "vishusapkal@gmail.com",
        "Degree": "Computer Science",
        "starting_year": 2022,
        "CGPA": "7.00",
        "total_attendance": 0,
        "Web_Tech": 0,
        "Web_Attendance": "2024-09-16 12:33:10",
        "SoftWare_Testing": 0,
        "Software_Attendance": "2024-09-16 12:33:10",
        "Accounting_Tools": 0,
        "Acc_Attendance": "2024-09-13 12:33:10",
        "Curr_year": 3,
        "last_attendance_time": "2024-09-17 12:33:10",
        "Notice": "Information or any Notice given out to students",
                
    },
    "Admin": {  # id of student which is a key
        "id": "Admin",
        "name": "Admin",
        "password": "Admin",
        "dob": "1997-08-02",
        "address": "Admin",
        "phone": "",
        "email": "email@gmail.com",
        "Degree": "Admin",
        "starting_year": 0,
        "CGPA": "",
        "total_attendance": 0,
        "Curr_year": 0,
        "last_attendance_time": "2023-02-21 12:33:10",
        "Notice": "Information or any Notice given out to students",
            },
        }


for key, value in data.items():
    ref.child(key).set(value)
