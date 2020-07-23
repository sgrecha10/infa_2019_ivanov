import shelve, classtools

grecha = classtools.Person('Sergey Grechnev', 'dev', 100000)
anna = classtools.Manager('Anna Chernysheva', 100000)
vasy = classtools.Manager2('Vasy Pupkin', 100000)


db = shelve.open('persondb')

for obj in (grecha, anna, vasy):
    db[obj.name] = obj

db.close()

