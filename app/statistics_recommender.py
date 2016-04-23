from flask import render_template
from flask import Flask
from flask import request
import pandas as pd


def generate_stats_recommendation(student_id,row_counter,course_list,grade):

    metric_list = []
    increase_list = []

    data = pd.read_csv('../data/data.csv')

    data_student =  data.loc[data['student_id'] == int(student_id)]
    for i in range(len(course_list)):
        data_courselist = data[(data.course_id == str(course_list[i])) & (data.grade == grade[i])]

        if data_courselist['class_participation'].mean() > data_student['class_participation'].mean():
            metric_list.append('Class Participation')
            increase_list.append(data_courselist['class_participation'].mean() - data_student['class_participation'].mean())

        if data_courselist['attendance'].mean() > data_student['attendance'].mean():
            metric_list.append('Attendance')
            increase_list.append(data_courselist['attendance'].mean() - data_student['attendance'].mean())

        if data_courselist['calibration'].mean() > data_student['calibration'].mean():
            metric_list.append('Calibration')
            increase_list.append(data_courselist['calibration'].mean() - data_student['calibration'].mean())

        if data_courselist['assignments'].mean() > data_student['assignments'].mean():
            metric_list.append('Assignments')
            increase_list.append(data_courselist['assignments'].mean() - data_student['assignments'].mean())

        if data_courselist['midterm'].mean() > data_student['midterm'].mean():
            metric_list.append('Midterm')
            increase_list.append(data_courselist['midterm'].mean() - data_student['midterm'].mean())

        if data_courselist['final'].mean() > data_student['final'].mean():
            metric_list.append('Final')
            increase_list.append(data_courselist['final'].mean() - data_student['final'].mean())

        if data_courselist['weekly_hours_1'].mean() > data_student['weekly_hours_1'].mean():
            metric_list.append('Weekly hours 1')
            increase_list.append(data_courselist['weekly_hours_1'].mean() - data_student['weekly_hours_1'].mean())

        if data_courselist['weekly_hours_2'].mean() > data_student['weekly_hours_2'].mean():
            metric_list.append('Weekly hours 2')
            increase_list.append(data_courselist['weekly_hours_2'].mean() - data_student['weekly_hours_2'].mean())

        if data_courselist['weekly_hours_3'].mean() > data_student['weekly_hours_3'].mean():
            metric_list.append('Weekly hours 3')
            increase_list.append(data_courselist['weekly_hours_3'].mean() - data_student['weekly_hours_3'].mean())

        if data_courselist['weekly_hours_4'].mean() > data_student['weekly_hours_4'].mean():
            metric_list.append('Weekly hours 4')
            increase_list.append(data_courselist['weekly_hours_4'].mean() - data_student['weekly_hours_4'].mean())

        if data_courselist['weekly_hours_5'].mean() > data_student['weekly_hours_5'].mean():
            metric_list.append('Weekly hours 5')
            increase_list.append(data_courselist['weekly_hours_5'].mean() - data_student['weekly_hours_5'].mean())

    return metric_list,increase_list,course_list

