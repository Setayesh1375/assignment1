name=input("Please enter your name : ")
lastname=input("Please enter your last name : ")
number=int(input("please enter Number of lessons : "))
n= number+1
sum=0
for x in range(1 , n):
  grade=float(input("please enter grade of lesson : "))
  sum=sum+grade
a=sum/number
if a>=17:
  print(a)  
  print("your status is great")
elif 17>a>=12:
   print(a)  
   print("your status is normal")  
elif a<12:
   print(a) 
   print("your status is fail")
 