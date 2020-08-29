import json
data=[]
class CustomDict(dict):
    def __init__(self):
     self=dict
    def add(self,key,value):
        self[key]=value
       
class User:
    def __init__(self, name, surname):
     self.name=name
     self.surname=surname
     self.CreateDictaddToList()
    def  CreateDictaddToList(self):
        myDict=CustomDict()
        myDict.add('name',self.name)
        myDict.add('surname',self.surname)
        data.append(myDict)

def GetData():
        name=input("enter name:")
        surname=input("enter surname:")
        User(name,surname)
for i in range(4):


 GetData()
with open("db.json","w") as conn:
    json.dump(data,conn)
for d in data:
    print(f" Ad:{d['name']}\ Soyad: {d['surname']}")