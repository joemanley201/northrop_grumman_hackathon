import json
import numpy as np

#Constants
CONST_OUTPUT_FILE_NAME = "../data/data.csv"

#CSV Structure
#course_id, student_id, class_participation, attendance, calibration, assignments, midterm, final, weekly_hours_1, weekly_hours_2, weekly_hours_3, weekly_hours_4, weekly_hours_5, grade

output_file_csv = open(CONST_OUTPUT_FILE_NAME, "w")

course_list = ['CSE1', 'CSE2', 'CSE3', 'CSE4', 'CSE5', 'CSE6', 'CSE7', 'CSE8', 'CSE9', 'CSE10', 'CSE11', 'CSE12', 'CSE13', 'CSE14', 'CSE15', 'CSE16', 'CSE17', 'CSE18', 'CSE19', 'CSE20']
csv_header = "course_id,student_id,class_participation,attendance,calibration,assignments,midterm,final,weekly_hours_1,weekly_hours_2,weekly_hours_3,weekly_hours_4,weekly_hours_5,grade"
output_file_csv.write(csv_header + "\n")
for course in course_list:
    np.random.seed(seed = int(filter(str.isdigit, course)))

    low_class_participation = np.random.normal(40, 5, 30).tolist()
    low_attendance = np.random.normal(30, 10, 30).tolist()
    low_calibration = np.random.normal(40, 8, 30).tolist()
    low_assignments = np.random.normal(40, 7, 30).tolist()
    low_midterm = np.random.normal(30, 11, 30).tolist()
    low_final = np.random.normal(44, 7, 30).tolist()
    #time for discussion sessions
    low_weekly_hours_1 = np.random.uniform(0, 2, 30).tolist()
    #time for lab hours
    low_weekly_hours_2 = np.random.uniform(0, 2, 30).tolist()
    #time for office hours
    low_weekly_hours_3 = np.random.uniform(0, 2, 30).tolist()
    #time for individual study
    low_weekly_hours_4 = np.random.uniform(0, 2, 30).tolist()
    #time for assignments
    low_weekly_hours_5 = np.random.uniform(0, 2, 30).tolist()

    med_class_participation = np.random.normal(65, 5, 40).tolist()
    med_attendance = np.random.normal(65, 10, 40).tolist()
    med_calibration = np.random.normal(63, 8, 40).tolist()
    med_assignments = np.random.normal(59, 7, 40).tolist()
    med_midterm = np.random.normal(63, 11, 40).tolist()
    med_final = np.random.normal(64, 7, 40).tolist()
    #time for discussion sessions
    med_weekly_hours_1 = np.random.uniform(1, 3, 40).tolist()
    #time for lab hours
    med_weekly_hours_2 = np.random.uniform(1, 3, 40).tolist()
    #time for office hours
    med_weekly_hours_3 = np.random.uniform(1, 3, 40).tolist()
    #time for individual study
    med_weekly_hours_4 = np.random.uniform(1, 3, 40).tolist()
    #time for assignments
    med_weekly_hours_5 = np.random.uniform(1, 3, 40).tolist()

    high_class_participation = np.random.normal(80, 5, 30).tolist()
    high_attendance = np.random.normal(85, 2, 30).tolist()
    high_calibration = np.random.normal(79, 1, 30).tolist()
    high_assignments = np.random.normal(85, 3, 30).tolist()
    high_midterm = np.random.normal(80, 5, 30).tolist()
    high_final = np.random.normal(90, 2, 30).tolist()
    #time for discussion sessions
    high_weekly_hours_1 = np.random.uniform(3, 5, 30).tolist()
    #time for lab hours
    high_weekly_hours_2 = np.random.uniform(3, 5, 30).tolist()
    #time for office hours
    high_weekly_hours_3 = np.random.uniform(3, 5, 30).tolist()
    #time for individual study
    high_weekly_hours_4 = np.random.uniform(3, 5, 30).tolist()
    #time for assignments
    high_weekly_hours_5 = np.random.uniform(3, 5, 30).tolist()


    total_class_participation = low_class_participation + med_class_participation + high_class_participation
    total_attendance = low_attendance + med_attendance + high_attendance
    total_calibration = low_calibration + med_calibration + high_calibration
    total_assignments = low_assignments + med_assignments + high_assignments
    total_midterm = low_midterm + med_midterm + high_midterm
    total_final = low_final + med_final + high_final
    total_weekly_hours_1 = low_weekly_hours_1 + med_weekly_hours_1 + high_weekly_hours_1
    total_weekly_hours_2 = low_weekly_hours_2 + med_weekly_hours_2 + high_weekly_hours_2
    total_weekly_hours_3 = low_weekly_hours_3 + med_weekly_hours_3 + high_weekly_hours_3
    total_weekly_hours_4 = low_weekly_hours_4 + med_weekly_hours_4 + high_weekly_hours_4
    total_weekly_hours_5 = low_weekly_hours_5 + med_weekly_hours_5 + high_weekly_hours_5

    for student in range(1, 101):
        recordSTR = ""
        recordSTR += course + ","
        recordSTR += str(student) + ","
        recordSTR += str(total_class_participation[student - 1]) + ","
        recordSTR += str(total_attendance[student - 1]) + ","
        recordSTR += str(total_calibration[student - 1]) + ","
        recordSTR += str(total_assignments[student - 1]) + ","
        recordSTR += str(total_midterm[student - 1]) + ","
        recordSTR += str(total_final[student - 1]) + ","
        recordSTR += str(total_weekly_hours_1[student - 1]) + ","
        recordSTR += str(total_weekly_hours_2[student - 1]) + ","
        recordSTR += str(total_weekly_hours_3[student - 1]) + ","
        recordSTR += str(total_weekly_hours_4[student - 1]) + ","
        recordSTR += str(total_weekly_hours_4[student - 1]) + ","
        grade = ((total_class_participation[student - 1] * 0.1) + (total_attendance[student - 1] * 0.05) + (total_calibration[student - 1] * 0.2) + (total_assignments[student - 1] * 0.3) + (total_midterm[student - 1] * 0.23) + (total_final[student - 1] * 0.3))
        recordSTR += str(grade)
        output_file_csv.write(recordSTR + "\n")
output_file_csv.close()