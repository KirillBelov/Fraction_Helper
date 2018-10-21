

num11 = int (input("Enter 1st numerator: "))
num12 = int (input("Enter 1st denominator: "))

act = input("Enter operation: ")

num21 = int (input("Enter 2nd numerator: "))
num22 = int (input("Enter 2nd denominator: "))



if act == "*":
   # Умножение

   res1 = (num11 * num21)
   denmain2 = (num12 * num22)

   print (res1)
   print ("-")
   print (denmain2)
   
if act == "/":
    # Деление
    
   res1 = num11 * num22
   denmain2 = num12 * num21

   print (res1)
   print ("-")
   print (denmain2)
    
if act == "+":
   # Сложение, неведомая хуета 1
   
   denst = (num12 * num22)
   den1 = (denst / num12)
   denmain1 = (num12 * den1)
   den2  = (denst / num22)
   denmain2 = (num22 * den2)
   res1  = (num11 * den1 + num21 * den2)
    
   if num12 == num22:
      res1 = (num11 + num21)
      denmain2 = (num12)
      
   print (res1)
   print ("-")
   print (denmain2)
    
if act == "-":
    # Вычитание, неведомая хуета 2
    
    denst = (num12 * num22)
    den1 = (denst / num12)
    denmain1 = (num12 * den1)
    den2  = (denst / num22)
    denmain2 = (num22 * den2)
    res1  = (num11 * den1 - num21 * den2)

    if num12 == num22:
      res1 = (num11 - num21)
      denmain2 = (num12)
  
    print (res1)
    print ("-")
    print (denmain2)

input()
