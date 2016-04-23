__author__ = 'Srinivas Avireddy'

data_file = open("../data/data.csv","r")
file_records = data_file.readlines()
header = file_records[0]
student_records = file_records[1:]
update_file = open("../data/data.csv","w")
update_file.write(header)

for record in student_records:
    student_record_array = record.strip().split(",")
    grade = float(student_record_array[-1])
    letter_grade = ""
    if grade >= 95.0:
        letter_grade = "A+"
    elif grade >= 90.0:
        letter_grade = "A"
    elif grade >= 85.0:
        letter_grade = "A-"
    elif grade >= 80.0:
        letter_grade = "B+"
    elif grade >= 75.0:
        letter_grade = "B"
    elif grade >= 70.0:
        letter_grade = "B-"
    elif grade >= 65.0:
        letter_grade = "C+"
    elif grade >= 60.0:
        letter_grade = "C"
    elif grade >= 55.0:
        letter_grade = "C-"
    elif grade >= 45.0:
        letter_grade = "D"
    else:
        letter_grade = "F"
    update_file.write(record.strip()+","+letter_grade+"\n")
update_file.close()





