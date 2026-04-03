class std__marks:
    def get__marks(self,m1,m2,m3,m4,m5):
        self.m1=int(input('\n\tEnter mark 1  : '))
        self.m2=int(input('\n\tEnter mark 2  : '))
        self.m3=int(input('\n\tEnter mark 3  : '))
        self.m4=int(input('\n\tEnter mark 4  : '))
        self.m5=int(input('\n\tEnter mark 5  : '))

        sum_a=m1+m2+m3+m4+m5
        self.avg=sum_a/5
    
    def show__marks(self):
        print('Average of the student : ',self.avg)
        
student___1=std__marks()
student___1.get__marks(99,98,99,100,100)
student___1.show__marks()