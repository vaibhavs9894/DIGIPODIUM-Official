class Mobile:
    def __init__(self,name,,type,modelno,company,):
        self.name=name
        self.type=type
        self.modelno=modelno
        self.company=company

if __name__ == "__main__":
    m1=Mobile('OnePlus Nord','Touch Screen',491894435','One Plus')
    m2=Mobile('Samsung Galaxy A52','qwert','491947167','samsung')


from dataclasses import dataclass

@dataclass



print(m1.name)
print(m2.name)
print(m1.modelno)
print(m2.modelno)