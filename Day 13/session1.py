1.# Refactor the 24-sc-student-report-generator.py to work with student.json
  #  Read student.json
  #  Calculate averages and ranks
  #  Write student-report.json

import json
 
with open(r'C:\Users\Administrator\Desktop\coading\day13\student.json', 'r') as f:
    studs = json.load(f)
 
for s in studs:
    s['avg'] = sum([s['phy'], s['chem'], s['math'], s['bio']]) / 4
 
sorted_studs = sorted(studs, key=lambda x: x['avg'], reverse=True)
 
for i, s in enumerate(sorted_studs, 1):
    s['rank'] = i
 
with open(r'C:\Users\Administrator\Desktop\coading\day13\student-report.json', 'w') as f:
    json.dump(sorted_studs, f, indent=4)
 
print("Report done!")
 
 