dict_marks = {'venu':95,
              'sravya':94,
              'girish':92,
              'deepu':91
            }
dict_grades = {} 
for i in dict_marks:
    marks = dict_marks[i]
    
    if marks>90:
        dict_grades[i] = 'O'
    elif marks>80:
        dict_grades[i] = 'A+'
    elif marks>70:
        dict_grades[i] = 'A'
    elif marks>60:
        dict_grades[i] = 'B+' 
    elif marks>50:
        dict_grades[i] = 'B'
    elif marks>40:
        dict_grades[i] = "C"
    elif marks<=40:
        dict_grades[i] = "F"
print(dict_grades)