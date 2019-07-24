class CharachterCount:
    def __init__(self):
        self.string=""

    def setString(self,str):
        if type(str)==int:
            print("Invalid Value")
        else:
            self.string=str       
    def getCount(self):
        return len(self.string)

c=CharachterCount()
c.setString(1)    
print(c.getCount())        