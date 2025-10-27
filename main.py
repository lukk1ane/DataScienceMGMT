class person2:
    def __init__(self, name, last_name):
        self.name=name
        self.last_name=last_name 
    def show(self):
        print(self.name,self.last_name)    

l2=person2("Mero","Oboladze")
smlist=[x**2 for x in range(10)]
print(smlist)
res=[]
for a in smlist:
    res.append(a*3)
print(res)  
