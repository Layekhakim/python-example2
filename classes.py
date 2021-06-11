class student():
   def __init__(self,name,age, class_="student"):
    self.name = name
    self.age = age

    self.class_ = class_

    def average(self,score1,score2,score3):
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    avg = (self.score1 + self.score2 + self.score3) // 3

    print(f"{self.name} achieved {avg} as an average")

Layek = student("Layek","25")
Layek.average(90,90,90)

