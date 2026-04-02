#import requests


#url = "Aqui va el url de la api a la que vamos a llamar"
#headers = {"Authorization":"Bearer YOUR_ACCESS_TOKEN"}

#params = {"country": "us", "category": "business"}

#response = requests.get(url,headers=headers,params=params)



#if response.status_code == 200:
    #data = response.json()
    #print(data)

import json 
path = 'D:/Edrick/Clases/Semana1/archivos_apoyo/data1.json'
with open(path,'r') as file:
    data = json.load(file)
    print(data)

    