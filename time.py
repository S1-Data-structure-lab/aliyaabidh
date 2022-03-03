class time:
    def __init__ (self,h,m,s):
        self.hr=h
        self.min=m
        self.sec=s
    def __add__(self,other):
        tempsec=self.sec+other.sec
        tempin=tempsec/60
        self.sec=int(tempsec%60)
        self.min=self.min+other.min+tempin
        temphr=self.min/60
        self.min=int(self.min%60)
        self.hr=int(self.hr+other.hr+temphr)
        return time(self.hr,self.min,self.sec)
    def __str__ (self):
        return str(self.hr)+'hr'+str(self.min)+'min'+str(self.sec)+'sec'
a=int(input("Enter Hr of T1:"))
b=int(input("Enter Min of T1:"))
c=int(input("Enter Sec of T1:"))
x=int(input("Enter Hr of T2:"))
y=int(input("Enter Min of T2:"))
z=int(input("Enter Sec of T2:"))
t1=time(a,b,c)
t2=time(x,y,z)
print(t1+t2)


