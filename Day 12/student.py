
#Access 24-sc-student-report-generator.py

#Task 1: Update the class dictionary with averages for every student (Step 3)
#Task 2: Come up with a logic to assign ranks for every student and implement it (Step 4)

# Step 1
# Read the content
 
 
f = open(r'python progrM/day12\student_data.csv','r')
content = f.readlines()
f.close()
 
print("INFO -> step 1", content)
 
# Step 2
# Process the content and store in a data structure
# What data structure will be good here? Sanjeev -> Dictionary
# student_dict -> class_dict
 
class_dict = {}
columns = [item.strip() for item in content[0].split(',')] # Keys of the student dictionary
for dataitem in content[1:]:
    values = [item.strip() for item in dataitem.split(',')] # Values for the student dictionary
    student_dict = dict(zip(columns, values)) # Zipping keys and values to form the student dictionary
    class_dict[student_dict['regid']] = student_dict # Adding student dictionery to class dictionary
 
 
 
 
# Step 3
# Calculate the average
 
 
for regid, student_data in class_dict.items():
    marks = [int(student_data[sub]) for sub in ['phy', 'chem', 'math','bio']]
    average = sum(marks) / len(marks)
    student_data['avg'] = round(average, 2)
 
print("\n" + "-"*100)
#print("INFO -> step 3 -> Class dictionary after averages updated\n", class_dict)
 
# Calculate the rank
sorted_students = sorted(class_dict.values(), key=lambda item: item.get('avg',0),reverse=True)
 
rank = 0
previous_average = None
 
for student in sorted_students:
    if student['avg'] == previous_average:
        student['rank'] = rank  # Same rank for same average
    else:
        rank += 1  # Ensure next rank is sequential
        student['rank'] = rank
   
    previous_average = student['avg']
 
class_dict = {student['regid']: student for student in sorted_students}
 
print("\n" + "-"*100)
print("INFO -> step 4 -> Class dictionary after ranks updated\n", class_dict)
 
 
# Step 5
# Display the report
'''print("\n" + "="*100)
print("INFO -> step 5 -> Final Report")
print(f"{'RegID':<10} {'Name':<20} {'PHYSICS': <20} {'CHEMISTRY': <20} {'MATHS': <20} {'BIOLOGY': <20} {'Average':<10} {'Rank':<5}")
print("-" * 50)
for student_id, student_data in class_dict.items():
    print(f"{student_id:<10} {student_data.get('name', 'N/A'):<20}{student_data.get('phy','N/A'):<20}{student_data.get('chem','N/A'): < 20}{student_data.get('math','N/A'): < 20}{student_data.get('bio','N/A'): < 20}{student_data.get('avg','N/A'):<10} {student_data.get('rank','N/A'):<5}")
'''
print("\n" + "="*100)
print("INFO -> step 5 -> Final Report")
print(f"{'RegID':<10} {'Name':<15} {'PHYSICS':<10} {'CHEMISTRY':<10} {'MATHS':<10} {'BIOLOGY':<10} {'AVERAGE':<10} {'Rank':<5}")
print("-" *100)
for student_id, student_data in class_dict.items():
    print(f"{student_id:<10} {student_data.get('name', 'N/A'):<15} {student_data.get('phy', 'N/A'):<10} {student_data.get('chem', 'N/A'):<10} {student_data.get('math', 'N/A'):<10} {student_data.get('bio', 'N/A'):<10} {student_data.get('avg', 'N/A'):<10} {student_data.get('rank', 'N/A'):<5}")
 
with open(r"python progrM/day12\rank.txt", "w") as file:
    file.write(f"{'RegID':<10} {'Name':<15} {'PHYSICS':<10} {'CHEMISTRY':<10} {'MATHS':<10} {'BIOLOGY':<10} {'AVERAGE':<10} {'Rank':<5}\n")
    file.write(("-" *100))
    for student_id, student_data in class_dict.items():
       file.write(f"\n{student_id:<10} {student_data.get('name', 'N/A'):<15} {student_data.get('phy', 'N/A'):<10} {student_data.get('chem', 'N/A'):<10} {student_data.get('math', 'N/A'):<10} {student_data.get('bio', 'N/A'):<10} {student_data.get('avg', 'N/A'):<10} {student_data.get('rank', 'N/A'):<5}\n")
    file.close()
 
 
with open(r"python progrM/day12\student_data.csv", "w") as file:
        file.write(','.join(columns) + '\n')
       
        for student in sorted_students:
            row = [str(student.get(col, '')) for col in student]
            file.write(','.join(row) + '\n')
 