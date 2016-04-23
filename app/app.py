from flask import render_template
from flask import Flask
from flask import request
import json
import pandas as pd
import re
from statistics_recommender import generate_stats_recommendation
from kclosest_student_predictor import find_kclosest_student_grades,find_all_mean_vectors

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_recommendation',methods=['POST'])
def generate_recommendation():
    student_id = request.form["studentID"]
    row_counter = request.form["rowCounter"]
    course_list = []
    grade = []
    closest_grades_list = []
    student_mean_vector = find_all_mean_vectors(65)
    for i in range(int(row_counter) + 1):
        course_list.append(request.form["courseID[" + str(i) + "]"])
        grade.append(request.form["expectedGrade[" + str(i) + "]"])
        closest_grades = find_kclosest_student_grades(student_mean_vector,course_list[i],5)
        closest_grades_list.append(closest_grades)
    metric_list,current_student_list,original_list = generate_stats_recommendation(student_id, row_counter, course_list,grade)
    print metric_list
    print current_student_list
    print original_list
    return render_template('reco_display.html', result = "'" +  re.escape(json.dumps({"metric_list": metric_list, "current_student_list": current_student_list, "course_list": course_list,"closest_grades_list":closest_grades_list,"original_list":original_list})) + "'")

if __name__ == '__main__':
    app.run(debug=True)
