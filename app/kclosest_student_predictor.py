__author__ = 'Srinivas Avireddy'
import pandas as pd
from collections import defaultdict

def read_student_csv():
    data = pd.read_csv("../data/data.csv")
    return data

def find_mean_vector(student_id,data_student):
    student_mean_dict = defaultdict(float)
    column_list = list(data_student.columns.values)
    columns_to_avoid = ["student_id","course_id","grade"]
    student_mean_dict["student_id"] = student_id
    for column in column_list:
        if column not in columns_to_avoid:
            student_mean_dict[column] = data_student[column].mean()
    return student_mean_dict

def find_all_mean_vectors(student_id):
    data = read_student_csv()
    student_mean_vectors = []
    data_student =  data.loc[data['student_id'] == int(student_id)]
    student_mean_vectors.append(find_mean_vector(student_id,data_student))
    student_list = data.student_id.unique()
    for id in student_list:
        if id != student_id:
            data_student =  data.loc[data['student_id'] == int(id)]
            student_mean_vector = find_mean_vector(id,data_student)
            student_mean_vectors.append(student_mean_vector)
    return student_mean_vectors

def find_euclidean_distance(student1, student2):
    euclidean_distance = 0.0
    for key in student1:
        if key != "student_id":
            euclidean_distance += ((student1[key] - student2[key]) ** 2)
    return euclidean_distance


def find_kclosest_student_grades(student_mean_vector,course_id,data,k):
    euclidean_distances = []
    k_closest_grades = []
    for student_vector in student_mean_vector[1:]:
        id2 = student_vector["student_id"]
        euclidean_distances.append((find_euclidean_distance(student_mean_vector[0],student_vector),id2))

    for item in sorted(euclidean_distances):
        id = item[1]
        if ((data.student_id == id) & (data.course_id == course_id)).any():
            if k > 0:
                filtered_row = data[(data.student_id == id) & (data.course_id == course_id)]
                #print filtered_row
                k_closest_grades.append(filtered_row["grade"].iloc[0])
                k = k - 1
            else:
                break
    #print k_closest_grades
    return k_closest_grades


data = read_student_csv()
student_mean_vector = find_all_mean_vectors(65)
#print student_mean_vector
print find_kclosest_student_grades(student_mean_vector,"CSE1",data,5)
