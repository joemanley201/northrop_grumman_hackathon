__author__ = 'Srinivas Avireddy'
import pandas as pd

def find_mean_vector(student_id):
    data = pd.read_csv("../data/data.csv")
    data_student =  data.loc[data['student_id'] == int(student_id)]
    print data_student
find_mean_vector(2)
