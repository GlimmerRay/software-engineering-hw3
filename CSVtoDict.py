import csv
import tempfile

# how does a csv.reader object work?
# basically you initialize with a file handle
#   must be opened in the proper way
# then, it's just an iterator which has each line as a list!

class csvToDict:

    def __init__(self, filename, temp=False):
        self.filename = filename
    
    def openFile(self):
        if not self.temp:
            return open(self.filename, 'r', newline='')
        else:
            return tempfile.NamedTemporaryFile(mode='w', newline='', encoding='utf-8')
    
    
    # takes one line of a csv file and enters the data 
    # appropriately into a dictoinary
    def csvLineToDict(self, line, _dict):
        keys = list(_dict.keys())
        for i in range(len(keys)):
            key = keys[i]
            _dict[key].append(line[i])
        return _dict

    
    def toDict(self):
        with self.openFile() as file:
            reader = csv.reader(file)
            titles = next(reader)
            _dict = {}
            for title in titles:
                _dict[title] = []
            for row in reader:
                _dict = self.csvLineToDict(row, _dict)
            return _dict
            

if __name__ == '__main__':
    _dict = csvToDict('mycsvfile.csv')
    print(_dict.toDict())