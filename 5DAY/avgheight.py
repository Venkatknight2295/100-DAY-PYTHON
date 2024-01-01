student_height = input().split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

totalheight = 0
for height in student_height:
    totalheight += height

numberofstudents = 0
for nostudents in student_height:
    numberofstudents += 1

averageheight = round(totalheight / numberofstudents)

print(f"Total Height: {totalheight}")
print(f"Number of Students: {numberofstudents}")
print(f"Average Height: {averageheight}")

