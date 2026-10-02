info = {
    "name":"Sibasis",
    "age":26
}

# Here there is pair of key and value where key can be any immutable data structure.
# like tuple and primitive data type also
# dictionary are unordered

# make sure here key only can be immutable but dictionary itself is mutable.
# dont allow duplicate key name

info_with_tuplekey = {
    "name":"Sibasis",
    "age":26,
    (1,2):"tuple data"
}

print(info_with_tuplekey)

print(info_with_tuplekey["name"]) 
# accesing value

info_with_tuplekey["name"]="Ansuman"
# can be mutated

info_with_tuplekey["lastname"]="Badatya"
# adding new key 

print(info_with_tuplekey)

null_dict={}
# can make null dictionary

print(null_dict)


# Nesting Dictionary
# ----------------------------------

student={
    "name":"Sibasis",
    "grades":{
        "math":90,
        "physics":"92"
    }
}

print(student)
print(student["grades"]["physics"])


# Methods
# ----------------------------

# .keys() returns all keys and can be type casted to list or tuple
print(student.keys())

print(list(student.keys()))

print(tuple(student.keys()))

# .values() returns all value corresponding to key can be type casted to list or tuple
print(student.values())
 
# .items()  retuns all key,value pair as tuple
print(student.items())

# .get() and .update() for get and update to new dictionary(will merge and may override)

print(student.get("name")) 
# for wroong key return null insted of error while simple accessing give error

a = {"name": "Sibasis", "age": 22}
b = {"age": 23, "city": "Bhubaneswar"}

a.update(b)

print(a)

# .copy() for shallow copy
d=a.copy()
print("Printing D")
print(d)
d["name"]="Ansuman"
print(d)
print(a)

# .popitem() is to get last entered tuple (key-value pair)

e=a.popitem()
print(e)
 