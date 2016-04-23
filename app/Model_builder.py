import pandas as pd
data = pd.read_csv('../data/data.csv')

student_id = 1
course_list = [11,12,13]
grade = ['A+','A+','A+']
data_student =  data.loc[data['student_id'] == 1]
for i in range(len(course_list)):
    print 'CSE' + str(course_list[i])
    data_courselist = data[(data.course_id == 'CSE' + str(course_list[i])) & (data.grade == grade[i])]
    print 'Your scores need to increase by the following %'
    if data_courselist['class_participation'].mean() > data_student['class_participation'].mean():
        print 'Class Participation',data_courselist['class_participation'].mean() - data_student['class_participation'].mean()

    if data_courselist['attendance'].mean() > data_student['attendance'].mean():
        print 'Attendance',data_courselist['attendance'].mean() - data_student['attendance'].mean()

    if data_courselist['calibration'].mean() > data_student['calibration'].mean():
        print 'Calibration',data_courselist['calibration'].mean() - data_student['calibration'].mean()

    if data_courselist['assignments'].mean() > data_student['assignments'].mean():
        print 'Assignments',data_courselist['assignments'].mean() - data_student['assignments'].mean()

    if data_courselist['midterm'].mean() > data_student['midterm'].mean():
        print 'Midterm',data_courselist['midterm'].mean() - data_student['midterm'].mean()

    if data_courselist['final'].mean() > data_student['final'].mean():
        print 'Final',data_courselist['final'].mean() - data_student['final'].mean()

    if data_courselist['weekly_hours_1'].mean() > data_student['weekly_hours_1'].mean():
        print 'Weekly hours 1',data_courselist['weekly_hours_1'].mean() - data_student['weekly_hours_1'].mean()

    if data_courselist['weekly_hours_2'].mean() > data_student['weekly_hours_2'].mean():
        print 'Weekly hours 2',data_courselist['weekly_hours_2'].mean() - data_student['weekly_hours_2'].mean()

    if data_courselist['weekly_hours_3'].mean() > data_student['weekly_hours_3'].mean():
        print 'Weekly hours 3',data_courselist['weekly_hours_3'].mean() - data_student['weekly_hours_3'].mean()

    if data_courselist['weekly_hours_4'].mean() > data_student['weekly_hours_4'].mean():
        print 'Weekly hours 4',data_courselist['weekly_hours_4'].mean() - data_student['weekly_hours_4'].mean()

    if data_courselist['weekly_hours_5'].mean() > data_student['weekly_hours_5'].mean():
        print 'Weekly hours 5',data_courselist['weekly_hours_5'].mean() - data_student['weekly_hours_5'].mean()
    print "\n"








