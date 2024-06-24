# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
for height in student_heights :
    total_height = total_height + height
print(f"total height = {total_height}")

total_student = len(student_heights)
print(f"number of students = {total_student}")

average = round(total_height / total_student)
print(f"average height = {average}")
