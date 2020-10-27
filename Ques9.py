def max_percent(student_info):
 max_percentage = 0
 for name in student_info.keys():
 percentage = sum(student_info[name].values())/4.0
 if percentage>max_percentage:
 max_percentage = percentage
 n = name
 print("\nThe Student with the maximum percentage is " + n )

def main():
 num_students = int(input("Please enter number of students:"))
 student_info = {}
 student_data = ["Maths", "Physics", "Chemistry", "Computer Science"]
 for i in range(0,num_students):
 student_name = input("\nName :")
 student_info[student_name] = {}
 for entry in student_data:
 student_info[student_name][entry] = float(input("\nEnter marks in " + str(entry) + ": "))

 print()
 print(student_info)
 max_percent(student_info)

if __name__ == "__main__":
 main()
