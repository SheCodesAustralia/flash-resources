names = []
with open("exam-results-1000.txt") as txt_file:
    for line in txt_file:
        names.append(line.split())

with open("exam-results-1000.csv", 'w') as csv_file:
    for name in names:
        csv_file.write(f"{name[0]}, {name[1]}\n")
