grade = []
grade.append(float(input('Enter grade for Module 1: ')))
grade.append(float(input('Enter grade for Module 2: ')))
grade.append(float(input('Enter grade for Module 3: ')))
grade.append(float(input('Enter grade for Module 4: ')))
grade.append(float(input('Enter grade for Module 5: ')))
grade.append(float(input('Enter grade for Module 6: ')))

print()
print('---------------Results----------------------')

print(f'Lowest Grade:           {min(grade):.2f}')
print(f'Highest Grade:          {max(grade):.2f}')
print(f'Sum of Grades:          {sum(grade):.2f}')
print(f'Average:                {(sum(grade)/len(grade)):.2f}')
print('--------------------------------------------')

if avg >= 80:
    print('Your grade is: B')

