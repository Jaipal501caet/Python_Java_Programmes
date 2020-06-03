num = int(input("Enter the number till you want to create fibonicci series : "))
n1 = 0
n2 = 1
count = 0

if(num<=0):
  print("please enter positive integer only, Fibonnici series : ", n1)
elif(num==1):
   print("Fibonacci sequence upto",num,": is", n1 , num)
   
else:
  print("Fibonnici Series up to ", num, "is :")
  while(count<num):
    print(n1)
    nth = n1 + n2
    n1=n2
    n2=nth
    count=count+1