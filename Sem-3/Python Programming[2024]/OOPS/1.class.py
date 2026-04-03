import random
class student:

    def __init__ (self,name):
        self.name=name
        
    def call__student(self):
        print('hello ',self.name)
    
    

    def marks_of_student(self):
        x_mark=random.randint(0,500)
        print(self.name,' has scored ',x_mark,' marks')

object_1=student('vijay')
object_1.call__student()

object_1.marks_of_student()              