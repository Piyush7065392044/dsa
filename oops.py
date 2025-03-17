
# strating of the game 
class student : #  ---->   # this is a class 
    name = "piyush "

s1 = student()  #----> this is a object of the class 
print(s1)#---> if we just print the s1 only then it will return a main object and adress like ---><__main__.student object at 0x000001AE2EF4D250>
print(s1.name) #----> accessing the value have to use properly with name of the class and object name 
# output : piyush 


class car :   # ----> this is a class 
    color = "red "
    brand = "marcedes"

car1 = car   # --> this is a object of class  
#  bec without class object have no existce in python frist have to create a class then a object 
print(car.brand)  # --> use  proper peramintor to get proper data 

# CUNSTRUCTOR in python 

# class student :
#     def __init__(self, fullname ): # ----> def is a cunstructor and frist need initial value 
#         #  self.name = fullname #----> self is a keywords to refreal variable 
#         self.name = fullname

# s1 = student("karan") #--> iska matlab ye hai ki jo bhi value tum isme pass karoge vo fullname variable
# # me store ho jayegi and uske  baad vo autometic self.name variable me store ho jaayegi 
# print(s1.name)


# class test :
#     def __init__(self,a,b):
#         self.d = a
#         self.c = b 
#     def show(self):
#         print(self.c* self.d)


# t1 = test(3,5)
# t2 = test(90,81)
# print(t1.d,t1.c)
# print(t2.d,t2.c)
# t3 = test(23,12)
# ta= test.show(t3.c,t3.d)
# class hello:
#     x = 10 
#     def __init__(self, a, b):

#         self.d = a  
#         self.e = b  

#     def show(self):
#         print(self.d , self.e)  

#     @staticmethod
#     def f2():
#         print("hello")  
#     @classmethod
#     def f3(cls):
#         print(cls.x)


# t1 = hello(9, "hello")  
# print(t1.d, t1.e)  # Output: 9 hello

# t2 = hello(5, "world")  # ✅ अब कोई error नहीं होगी
# print(t2.d, t2.e)  # Output: 5 world

# ww = hello.f2  # ✅ Function reference
# print(ww)  # Output: <function hello.f2 at 0x000...>  

# hello.f2()  # ✅ Function call करने का सही तरीका (Output: hello)

# hello.f3()


class employe :
    def __init__(self,empaid,salary,name):
        self.empid = empaid
        self.salary = salary
        self.name = name
        



t3 = employe(empaid=employe,salary=200000,name="piyush")

print(t3.name,t3.empid,t3.salary)
# t3.detils