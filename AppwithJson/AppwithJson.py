import json
sample=[{
    'name':"Nigar",
    'surname':"Mammadova"

    },
{  'name':"Unknownname",
   'surname':"Unknownsurname"
 }]
with open('db.json',"r") as conn:
  data=json.load(conn)
for elem in data :
    for key,value in elem.items():
        if (value=="Nigar"):
         print(elem['surname'])

