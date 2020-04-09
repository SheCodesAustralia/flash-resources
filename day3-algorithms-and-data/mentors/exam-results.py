import csv
# import time
import plotly.express as px
# import numpy as np

data = []

with open("exam-results-20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        data.append(line)


num_absent_students = 0
scores = []

txt_file = open("summary.txt", "w")

for student in data:
    first_name = student[0]
    last_name = student[1].strip()
    score = student[2].strip()
    if score == "null":
        score = "ABSENT"
        num_absent_students = num_absent_students + 1
    else:
        scores.append(score)
    student_summary = f"{first_name} {last_name}: {score}\n"
    txt_file.write(student_summary)

total_students = len(data)
num_present_students = total_students - num_absent_students

txt_file.write("=======================================\n")

present_summary = f"Number of students who sat the exam: {num_present_students}\n"
absent_summary = f"Number of students who were absent: {num_absent_students}\n"

txt_file.write(present_summary)
txt_file.write(absent_summary)


scores.sort()

median_index = round(len(scores)/2)
lq_index = round(median_index/2)
uq_index = median_index + lq_index

min_score = scores[0]
lq_score = scores[lq_index]
median_score = scores[median_index]
uq_score = scores[uq_index]
max_score = scores[-1]

min_score_summary = f"The min score was {min_score}\n"
lq_score_summary = f"The LQ score was {lq_score}\n"
median_score_summary = f"The median score was {median_score}\n"
uq_score_summary = f"The UQ score was {uq_score}\n"
max_score_summary = f"The max score was {max_score}\n"

txt_file.write(min_score_summary)
txt_file.write(lq_score_summary)
txt_file.write(median_score_summary)
txt_file.write(uq_score_summary)
txt_file.write(max_score_summary)

txt_file.close()

# graph

df = { "Score": [
        min_score, lq_score, median_score, uq_score, max_score
    ]
}
fig = px.box(df, y="Score")
fig.show()
