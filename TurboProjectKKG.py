import csv
start_array = []
with open('acme_worksheet.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        start_array.append(row)
start_array = start_array[1:]

names = []
dates = []
for info in start_array:
    if info[1] == start_array[0][1]:
        names.append(info[0])
    dates.append(info[1])
dates = list(set(dates))

end_array = [["Name/Date"] + dates]

for name in names:
    list = [name]
    for date in dates:
        for info in start_array:
            if name == info[0] and date == info[1]:
                list.append(info[2])

    end_array.append(list)

with open('turboProjectKKG.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(end_array)
