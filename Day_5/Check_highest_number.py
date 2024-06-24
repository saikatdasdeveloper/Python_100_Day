# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
check_auth = 0
for check in student_scores:
  
  if check > check_auth:
     check_auth = check

print(f"The highest score in the class is: {check_auth}")