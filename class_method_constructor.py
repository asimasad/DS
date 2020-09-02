class Person:
  count=0
  def __init__(self,first_name,last_name,age):
       Person.count +=1
       self.firstname=first_name
       self.lastname=last_name
       self.age=age

  @classmethod
  def form_string(cls,string):
     first,last,age= string.split(',') 
     return cls(first,last,age)
  @classmethod
  def count_instances(cls):
      return f'You have create {cls.count} instance of {cls.__name__} class'    

  def full_name(self):
      return f'{self.firstname} {self.lastname} age is {self.age}'     


  def is_above_18(self):
     return self.age>18


p1=Person('Asim','Asad',25)
p2=Person('Ali','Asad',35)
p3=Person.form_string('Adnan,Khan,40')
print(p3.full_name())
# print(p1.full_name())
# print(p1.is_above_18())


