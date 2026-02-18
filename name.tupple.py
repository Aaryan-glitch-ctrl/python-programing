students = [(86,"Milan",18),(91,"aaryan",19),(68,"divy",18)]
roll_nos = []
names = []
age = []
for s in students:
    roll_nos.append(s[0])
    names.append(s[1])
    age.append(s[2])
print("Roll Numbers:" , roll_nos)
print("Names:" , names)
print("Ages:", age)
