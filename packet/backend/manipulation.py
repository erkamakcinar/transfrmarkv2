import csv
from itertools import count

class Reader:
    def __init__(self, files):
        self.files = files

    def getTeam(self):
        city = self.files[len(self.files) - 1]
        name = self.files[len(self.files) - 2]
        stadium = self.files[len(self.files) - 3]

        result = []
        count = 0
        for name in name:
            tmp =  {name:[]}
            tmp[name].append(city[count])
            tmp[name].append(stadium[count])
            result[count] = tmp
            count+=1
        return result
        


        
        
        