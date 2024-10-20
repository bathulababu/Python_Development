import os
import logging

# Configure logging
logging.basicConfig(filename='attendance_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.attendance = {}

class AttendanceSystem:
    def __init__(self):
        self.students = {}
    
    def add_student(self, roll_no, name):
        student = Student(roll_no, name)
        self.students[roll_no] = student
        logging.info(f"Added student: {name} (Roll No: {roll_no})")
    
    def mark_attendance(self, date):
        for roll_no, student in self.students.items():
            attendance_status = input(f"{student.name} (Roll No: {roll_no}) (enter p or a):  ").lower()
            if attendance_status == "p" or attendance_status == "a":
                student.attendance[date] = attendance_status
                logging.info(f"Marked attendance for {student.name} (Roll No: {roll_no}) on {date}.")
            else:
                logging.warning("Invalid attendance status. Please enter 'present' or 'absent'.")
    
    def save_attendance(self, date):
        dir_name = "attendance_records"
        os.makedirs(dir_name, exist_ok=True)
        file_path = os.path.join(dir_name, f"attendance_{date}.txt")
        
        with open(file_path, 'w') as file:
            for roll_no, student in self.students.items():
                attendance_status = student.attendance.get(date, "absent")
                file.write(f"{student.name} (Roll No: {roll_no}): {attendance_status}\n")

attendance_system = AttendanceSystem()

# Adding students
students_data = [
    (101, "Naveen Babu B"),
    (102, "Pradeep V"),
    (103, "Prakesh M"),
    (104, "Nirmal M"),
    (105, "Naveen b"),
    (106, "Praneeth Kumar R"),
    (107, "Rajasekhar N"),
    (108, "Keerthi S"),
    (109, "SriHarshitha V"),
    (110, "Navya A")
]

for roll_no, name in students_data:
    attendance_system.add_student(roll_no, name)

# Get the attendance date from the user
attendance_date = input("Enter the attendance date (DD-MM-YYYY): ")

# Mark attendance for each student
print("ATTENDANCE FOR: ",attendance_date)
print("=========================================")
attendance_system.mark_attendance(attendance_date)

# Save attendance data for the specified date
attendance_system.save_attendance(attendance_date)

print("\nATTENDANCE TAKEN SUCCESSFULLY!\n")
print("Thank You")

