students={'Alice':12,'Bob':10, 'Charlie':50,}
#print(students[12])
#print(students[10])
#print(students[50])
#print (students.keys())
#print (students.values())
for name in students.items():
  print(f'{name}')

del students['Bob']
print()
print(students)
