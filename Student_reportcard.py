students={                           #can be changeable its just for reference
    "Theerthan" : [90,89,92],
    "Sanjay" : [89,88,97],
    "Sriii" : [89,78,98]
}
for key,value in students.items():
    total=0
    for i in range(0,3):
        total += value[i]

    avg=total/3
    if avg >= 90:
        grade="A"
    elif avg>= 80:
        grade="B"
    else:
        grade="C"

    print("Report Card of ",key)
    print("Name: ",key ,"\nMarks: ",value,"\nTotal: ",total,f"\nAverage: {avg:.2f}","\nGrade: ",grade,"\n\n")