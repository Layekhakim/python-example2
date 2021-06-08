def grade(name,h_score,a_score,f_exam):
    added = (h_score+a_score+f_exam)/175*100
    singlesf = int(added)
    grade = ""
    print("Name: "+name+" achieved " + "{:.2f}".format(added))
    if singlesf >= 90:
        grade = "A"
    elif (singlesf >= 80) and (singlesf < 90):
        grade = "B"
    elif (singlesf >= 80) and (singlesf < 90):
        grade = "C"
    elif (singlesf >= 70) and (singlesf < 80):
        grade = "D"
    elif (singlesf >= 60) and (singlesf < 80):
        grade = "E"
    elif (singlesf >= 50) and (singlesf < 80):
        grade = "F"
    else:
        print("U")
    print(f"Grade: {grade}")
grade("Layek",24,49,100)
