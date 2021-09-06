import csv
import numpy as np

# how does csv.reader object work?
# will, you initialize it with a file handle
#   probably want it to be blank and opened with the correct settings
# then, you just feed it lists and it writes them as comma separated lines

class dictToCsvFile:

    def __init__(self, filename, _dict):
        self.filename = filename
        self.dict = _dict

    def openBlankFile(self, filename):
        return open(filename, 'w', newline='', encoding='utf-8')
    
    def write(self):
        file = self.openBlankFile(self.filename)
        writer = csv.writer(file)
        heading = list(self.dict.keys())
        writer.writerow(heading)

        dictToList = self.dictValuesToList()
        actualData = self.transpose2dList(dictToList)

        for row in actualData:
            writer.writerow(row)
        file.close()
    
    def dictValuesToList(self):
        return [value for value in self.dict.values()]
    
    def transpose2dList(self, _list):
        arr = np.array(_list)
        return list(arr.transpose())

if __name__ == '__main__':
    
    test_data = {
        'title': ['Walden','Walden two'],
        'author': ['Henry David Thoreau','B.F. Skinner'],
        'isbn': ['123', '456']
    }

    dictToCsv = dictToCsvFile('mycsvfile.csv', test_data)
    dictToCsv.write()