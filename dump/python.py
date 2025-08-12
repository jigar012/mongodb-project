import bson

with open('dump/school/students.bson', 'rb') as f:
    data = bson.decode_all(f.read())

print(data)