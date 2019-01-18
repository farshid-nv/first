import csv
from statistics import mean

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as csvFile:
        read = csv.reader(csvFile)
        outFile = open(output_file_name, 'w')
        for row in read:
            person = list()
            name = row[0]
            tempList = list()
            for i in row[1:]:
                person.append(float(i))
            avg = mean(person)
            tempList.append(name)
            tempList.append(str(avg))
            writer = csv.writer(outFile)
            writer.writerow(tempList)

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as csvFile:
        read = csv.reader(csvFile)
        outFile = open(output_file_name, 'w')
        nameAvg = dict()
        for row in read:
            person = list()
            name = row[0]
            for i in row[1:]:
                person.append(float(i))
            avg = mean(person)
            nameAvg[name] = avg
        sort = [(k, nameAvg[k]) for k in sorted(nameAvg, key=nameAvg.get, reverse=False)]
        for k, v in sort:
            tempList = list()
            tempList.append(k)
            tempList.append(str(v))
            writer = csv.writer(outFile)
            writer.writerow(tempList)

def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as csvFile:
        read = csv.reader(csvFile)
        outFile = open(output_file_name, 'w')
        nameAvg = dict()
        for row in read:
            person = list()
            name = row[0]
            for i in row[1:]:
                person.append(float(i))
            avg = mean(person)
            nameAvg[name] = avg
        sort = [(k, nameAvg[k]) for k in sorted(nameAvg, key=nameAvg.get, reverse=True)]
        count = 0
        for k, v in sort:
            count += 1
            if count > 3:
                break
            tempList = list()
            tempList.append(k)
            tempList.append(str(v))
            writer = csv.writer(outFile)
            writer.writerow(tempList)

def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as csvFile:
        read = csv.reader(csvFile)
        outFile = open(output_file_name, 'w')
        nameAvg = dict()
        for row in read:
            person = list()
            name = row[0]
            for i in row[1:]:
                person.append(float(i))
            avg = mean(person)
            nameAvg[name] = avg
        sort = [(k, nameAvg[k]) for k in sorted(nameAvg, key=nameAvg.get, reverse=False)]
        count = 0
        for k, v in sort:
            count += 1
            if count <= 3:
                tempList = list()
                tempList.append(str(v))
                writer = csv.writer(outFile)
                writer.writerow(tempList)

def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as csvFile:
        read = csv.reader(csvFile)
        outFile = open(output_file_name, 'w')
        nameAvg = dict()
        for row in read:
            person = list()
            name = row[5]
            for i in row[2:]:
                person.append(float(i))
            avg = mean(person)
            nameAvg[name] = avg
        sort = [(k, nameAvg[k]) for k in sorted(nameAvg, key=nameAvg.get, reverse=False)]
        tempList = list()
        for k, v in sort:
            tempList.append(v)
        averageOfAverages = list()
        averageOfAverages.append(str(mean(tempList)))
        writer = csv.writer(outFile)
        writer.writerow(averageOfAverages)

calculate_averages('grades.csv', 'outcsv1.csv')
calculate_sorted_averages('grades.csv', 'outcsv2.csv')
calculate_three_best('grades.csv', 'outcsv3.csv')
calculate_three_worst('grades.csv', 'outcsv4.csv')
calculate_average_of_averages('grades.csv', 'outcsv5.csv')
