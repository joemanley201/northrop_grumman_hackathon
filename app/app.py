from flask import render_template
from flask import Flask
from flask import request
import pandas as pd
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
        print "hi"
        course_list.append(request.form["courseID[" + str(i) + "]"])
        grade.append(request.form["expectedGrade[" + str(i) + "]"])

    metric_list,increase_list,course_list = generate_stats_recommendation(student_id,row_counter,course_list,grade)

    return render_template('reco_display.html',metrics = metric_list,change = increase_list,course = course_list)
if __name__ == '__main__':
    app.run(debug=True)
