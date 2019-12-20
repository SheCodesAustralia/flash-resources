data = []

with open('names.txt') as txt_file:
    for line in txt_file:
        line = line.strip()
        data.append(line)

print(data)
