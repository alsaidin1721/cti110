# CTI-110
# P3HW1 - Debugging
# Alsaidi
# 11-1-2022
#
grades = []
for i in range(6):
    grades.append(float(input(f'Enter grade for module {i+1}: ')))

lowest = min(grades)
highest = max(grades)
tot = sum(grades)
avg = tot/len(grades)

grade = ''
if avg > 90:
    grade = 'A'
elif avg > 80:
    grade = 'B'
elif avg > 70:
    grade = 'C'
elif avg > 60:
    grade = 'D'
else:
    grade = 'F'
print("\n-----------------Results-------------------")
print(f'Lowest Grade:      {lowest:.1f}')
print(f'Highest Grade:     {highest:.1f}')
print(f'Sum of Grades:     {tot:.1f}')
print(f'Average:           {avg:.2f}')
print("---------------------------------------------")
print(f'Your grade is: {grade}')





