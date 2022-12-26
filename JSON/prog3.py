import json

task = ["oleg", 24, ["Belarus","Russia"], (24,1), ["Moscow","Vladikavkaz",'Krasnodar',"Rostov","Nalchik"]]
data = {'name': task[0],
        'age': task[1],
        'countries': [{
            'name': task[2],
            'time': task[3],
            'cities': task[4],
        }]
}
with open('Philippov3.json', 'w')as write_file:
    json.dump(data, write_file, indent=4)