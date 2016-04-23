from flask import render_template
from flask import Flask
from flask import request
import pandas as pd


def generate_stats_recommendation(student_id,row_counter,course_list,grade):

    original_list = []
    current_student_list = []
    metric_list = []

    data = pd.read_csv('../data/data.csv')

    data_student =  data.loc[data['student_id'] == int(student_id)]
    for i in range(len(course_list)):
        original = []
        metric = []
        current_student = []
        data_courselist = data[(data.course_id == str(course_list[i])) & (data.grade == str(grade[i]))]

        if data_courselist['class_participation'].mean() > data_student['class_participation'].mean():
            metric.append('Class Participation')
            original.append(data_courselist['class_participation'].mean())
            current_student.append(data_student['class_participation'].mean())

        if data_courselist['attendance'].mean() > data_student['attendance'].mean():
            metric.append('Attendance')
            original.append(data_courselist['attendance'].mean())
            current_student.append(data_student['attendance'].mean())

        if data_courselist['calibration'].mean() > data_student['calibration'].mean():
            metric.append('Calibration')
            original.append(data_courselist['calibration'].mean())
            current_student.append(data_student['calibration'].mean())

        if data_courselist['assignments'].mean() > data_student['assignments'].mean():
            metric.append('Assignments')
            original.append(data_courselist['assignments'].mean())
            current_student.append(data_student['assignments'].mean())

        if data_courselist['midterm'].mean() > data_student['midterm'].mean():
            metric.append('midterm')
            original.append(data_courselist['midterm'].mean())
            current_student.append(data_student['midterm'].mean())

        if data_courselist['final'].mean() > data_student['final'].mean():
            metric.append('Final')
            original.append(data_courselist['final'].mean())
            current_student.append(data_student['final'].mean())

        if data_courselist['weekly_hours_1'].mean() > data_student['weekly_hours_1'].mean():
            metric.append('Weekly hours 1')
            original.append(data_courselist['weekly_hours_1'].mean())
            current_student.append(data_student['weekly_hours_1'].mean())

        if data_courselist['weekly_hours_2'].mean() > data_student['weekly_hours_2'].mean():
            metric.append('Weekly hours 2')
            original.append(data_courselist['weekly_hours_2'].mean())
            current_student.append(data_student['weekly_hours_2'].mean())

        if data_courselist['weekly_hours_3'].mean() > data_student['weekly_hours_3'].mean():
            metric.append('Weekly hours 3')
            original.append(data_courselist['weekly_hours_3'].mean())
            current_student.append(data_student['weekly_hours_3'].mean())

        if data_courselist['weekly_hours_4'].mean() > data_student['weekly_hours_4'].mean():
            metric.append('Weekly hours 4')
            original.append(data_courselist['weekly_hours_4'].mean())
            current_student.append(data_student['weekly_hours_4'].mean())

        if data_courselist['weekly_hours_5'].mean() > data_student['weekly_hours_5'].mean():
            metric.append('Weekly hours 5')
            original.append(data_courselist['weekly_hours_5'].mean())
            current_student.append(data_student['weekly_hours_5'].mean())

        original_list.append(original)
        metric_list.append(metric)
        current_student_list.append(current_student)

    return metric_list,current_student_list,original_list

