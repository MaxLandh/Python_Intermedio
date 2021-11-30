##UTF-8

#Datos de empleados, edad, organizacion, posicion y lenguje que dominan
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #Qeremos todos los desarrolladores que manejen Python
    #all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]
    #Realizaremos la misma linea de arriba con high function
    devs = list(filter(lambda worker: worker['language']=='python', DATA))
    all_python_devs = list(map(lambda worker: worker['name'], devs))
    for dev  in all_python_devs:
        print(dev)

    
    print('''
            PROCESSING''')

    #Queremos a todos los trabajadores de platzi
    #all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    #Realizaremos la misma linea de arriba con high function
    workers = list(filter(lambda worker: worker['organization']=='Platzi', DATA))
    all_platzi_workers = list(map(lambda worker: worker['name'], workers))
    for work in all_platzi_workers:
        print(work)
    
    print('''
            PROCESSING''')
    #Queremos a todos los adultos, osea mayores de 18 
    all_olders = [worker["name"] for worker in DATA if worker["age"] > 18]
    #Usando las funciones de orden superior
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    

    #old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    #Realizaremos la linea de arriba con list comprehensions
    old_people = [worker['name'] for worker in DATA if worker['age']>70]
    for old in old_people:
        print(old)   


if __name__=="__main__":
    run()   