class student:

    #constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    #member functions
    def show_info(self):
        print('\n\tName : ',self.name)
        print('\n\tage : ',self.age)


    

object__1=student('vijay',19)
object__1.show_info()