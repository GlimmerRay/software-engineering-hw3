import tempfile
from dictToCSV import dictToCsvFile
from CSVtoDict import csvToDict


# how does a tempfile.TemporaryFile work?
# well, there are zero required arguments.
# it is destroyed as soon as it is closed.

# for this problem, we're taking a dictionary
# and returning a dictionary




import csv

def dictToCsv(_dict):
    
    csvf = open('mycsvfile.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(csvf)

    heading = list(_dict.keys())
    writer.writerow(heading)
    for key in heading:
        rowdata = _dict[key]
        writer.writerow(rowdata)

def csvToDict(file):
    reader = csv.reader(file)

    titles = next(reader)
    outputDict = {}

    i = 0
    for row in reader:
        title = titles[i]
        outputDict[title] = row
        i += 1
    
    return outputDict

def combineBoth(_dict):
    csvf = tempfile.NamedTemporaryFile(mode='w', newline='', encoding='utf-8')
    writer = csv.writer(csvf)

    heading = list(_dict.keys())
    writer.writerow(heading)
    for key in heading:
        rowdata = _dict[key]
        writer.writerow(rowdata)
    
    reader = csv.reader(csvf)

    titles = next(reader)
    outputDict = {}

    i = 0
    for row in reader:
        title = titles[i]
        outputDict[title] = row
        i += 1
    
    return outputDict

test_data = {
    'title': ['Walden','Walden two'],
    'author': ['Henry David Thoreau','B.F. Skinner'],
    'isbn': ['123', '456']
}

print(combineBoth(test_data))
    
    



