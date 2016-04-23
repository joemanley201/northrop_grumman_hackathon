from flask import render_template
from flask import Flask
from flask import request
import json
import pandas as pd
import re
from statistics_recommender import generate_stats_recommendation

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
    for i in range(int(row_counter) + 1):
        course_list.append(request.form["courseID[" + str(i) + "]"])
        grade.append(request.form["expectedGrade[" + str(i) + "]"])

    metric_list,increase_list,course_list = generate_stats_recommendation(student_id, row_counter, course_list,grade)
    return render_template('reco_display.html', result = "'" +  re.escape(json.dumps({"metric_list": metric_list, "increase_list": increase_list, "course_list": course_list})) + "'")

if __name__ == '__main__':
    app.run(debug=True)
