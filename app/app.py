from flask import render_template
from flask import Flask
from flask import request
import matplotlib.pyplot as plt
import numpy as np
from cStringIO import StringIO
import pandas as pd

app = Flask(__name__)


html = '''
<html>
    <body>
        <img src="data:image/png;base64,{}" />
    </body>
</html>
'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_recommendation',methods=['POST'])
def generate_recommendation():
    student_id = request.form["studentID"]
    row_counter = request.form["rowCounter"]
    course_list = []
    grade = []

    metric_list = []
    increase_list = []
    for i in range(int(row_counter) + 1):
        course_list.append(request.form["courseID[" + str(i) + "]"])
        grade.append(request.form["expectedGrade[" + str(i) + "]"])

    data = pd.read_csv('../data/data.csv')

    data_student =  data.loc[data['student_id'] == int(student_id)]
    for i in range(len(course_list)):
        print str(course_list[i])
        data_courselist = data[(data.course_id == str(course_list[i])) & (data.grade == grade[i])]
        print 'Your scores need to increase by the following %'
        if data_courselist['class_participation'].mean() > data_student['class_participation'].mean():
            metric_list.append('Class Participation')
            increase_list.append(data_courselist['class_participation'].mean() - data_student['class_participation'].mean())
            print 'Class Participation',data_courselist['class_participation'].mean() - data_student['class_participation'].mean()

        if data_courselist['attendance'].mean() > data_student['attendance'].mean():
            print 'Attendance',data_courselist['attendance'].mean() - data_student['attendance'].mean()
            metric_list.append('Attendance')
            increase_list.append(data_courselist['attendance'].mean() - data_student['attendance'].mean())

        if data_courselist['calibration'].mean() > data_student['calibration'].mean():
            print 'Calibration',data_courselist['calibration'].mean() - data_student['calibration'].mean()
            metric_list.append('Calibration')
            increase_list.append(data_courselist['calibration'].mean() - data_student['calibration'].mean())

        if data_courselist['assignments'].mean() > data_student['assignments'].mean():
            print 'Assignments',data_courselist['assignments'].mean() - data_student['assignments'].mean()
            metric_list.append('Assignments')
            increase_list.append(data_courselist['assignments'].mean() - data_student['assignments'].mean())

        if data_courselist['midterm'].mean() > data_student['midterm'].mean():
            print 'Midterm',data_courselist['midterm'].mean() - data_student['midterm'].mean()
            metric_list.append('Midterm')
            increase_list.append(data_courselist['midterm'].mean() - data_student['midterm'].mean())

        if data_courselist['final'].mean() > data_student['final'].mean():
            print 'Final',data_courselist['final'].mean() - data_student['final'].mean()
            metric_list.append('Final')
            increase_list.append(data_courselist['final'].mean() - data_student['final'].mean())

        if data_courselist['weekly_hours_1'].mean() > data_student['weekly_hours_1'].mean():
            print 'Weekly hours 1',data_courselist['weekly_hours_1'].mean() - data_student['weekly_hours_1'].mean()
            metric_list.append('Weekly hours 1')
            increase_list.append(data_courselist['weekly_hours_1'].mean() - data_student['weekly_hours_1'].mean())

        if data_courselist['weekly_hours_2'].mean() > data_student['weekly_hours_2'].mean():
            print 'Weekly hours 2',data_courselist['weekly_hours_2'].mean() - data_student['weekly_hours_2'].mean()
            metric_list.append('Weekly hours 2')
            increase_list.append(data_courselist['weekly_hours_2'].mean() - data_student['weekly_hours_2'].mean())

        if data_courselist['weekly_hours_3'].mean() > data_student['weekly_hours_3'].mean():
            print 'Weekly hours 3',data_courselist['weekly_hours_3'].mean() - data_student['weekly_hours_3'].mean()
            metric_list.append('Weekly hours 3')
            increase_list.append(data_courselist['weekly_hours_3'].mean() - data_student['weekly_hours_3'].mean())

        if data_courselist['weekly_hours_4'].mean() > data_student['weekly_hours_4'].mean():
            print 'Weekly hours 4',data_courselist['weekly_hours_4'].mean() - data_student['weekly_hours_4'].mean()
            metric_list.append('Weekly hours 4')
            increase_list.append(data_courselist['weekly_hours_4'].mean() - data_student['weekly_hours_4'].mean())

        if data_courselist['weekly_hours_5'].mean() > data_student['weekly_hours_5'].mean():
            print 'Weekly hours 5',data_courselist['weekly_hours_5'].mean() - data_student['weekly_hours_5'].mean()
            metric_list.append('Weekly hours 5')
            increase_list.append(data_courselist['weekly_hours_5'].mean() - data_student['weekly_hours_5'].mean())
        print "\n"

    return render_template('reco_display.html',metrics = metric_list,change = increase_list,course = course_list)
if __name__ == '__main__':
    app.run(debug=True)
