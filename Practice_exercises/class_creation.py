#percentage <40 : fail
#percentage between 40 to 58 : second class
#percentage between 59 to 70 : first class
#percentage >70 : first class with distinction
class Student:
  def __init__(self,regno,name,mark1,mark2,mark3,mark4):
    self.regno=regno
    self.name=name
    self.mark1=mark1
    self.mark2=mark2
    self.mark3=mark3
    self.mark4=mark4
  def score(self):
    self.total = self.mark1+self.mark2+self.mark3+self.mark4
    print("Total marks :",self.total)
  def percentage(self):
    self.percent = (self.total/400)*100
    print("Percentage : ",self.percent)
  def grade(self):
    if (self.percent<40):
      print("Grade : Fail")
    elif self.percent>=40 and self.percent<59:
      print("Grade : Second Class")
    elif self.percent>=59 and self.percent<70:
      print("Grade : First Class")
    elif self.percent>70:
      print("Grade : First Class with ditinction")
  def display(self):
    print("--------------------------------------------")
    print("Reg No : ",self.regno,"\nName : ",self.name)
    self.score()
    self.percentage()
    self.grade()
print("Student Grade Report")
f1=Student(1,"Aswin",1,2,3,4)
f2=Student(2,"Rahul",100,55,70,82)
f3=Student(3,"Tom",20,40,50,80)
f4=Student(4,"Jerry",40,30,100,70)
f1.display()
f2.display()
f3.display()
f4.display()
