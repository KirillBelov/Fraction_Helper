
num11 = int (input("Enter 1st numerator: "))
num12 = int (input("Enter 1st denominator: "))


act = input("Enter operation: ")
actdo = 0

if act == "*":
    actdo += 1
if act == "/":
    actdo += 2
if act == "+":
    actdo += 3
if act == "-":
    actdo += 4

num21 = int (input("Enter 2nd numerator: "))
num22 = int (input("Enter 2nd denominator: "))

if actdo == 1:
    print (num11 * num21)
if actdo == 1:
    print ("-")
if actdo == 1:
     print (num12 * num22)

if actdo == 2:
    print  (num11 * num22)
if actdo == 2:
    print ("-")
if actdo == 2:
     print (num12 * num21)

if actdo == 3:
    denst = (num12 * num22)
    den1 = (denst / num12)
    denmain1 = (num12 * den1)
    den2  = (denst / num22)
    denmain2 = (num22 * den2)
    res1  = (num11 * den1 + num21 * den2)
    print (res1)
if actdo == 3:
    print ("-")
if actdo == 3:
    print (denmain2)

if actdo == 4:
    denst = (num12 * num22)
    den1 = (denst / num12)
    denmain1 = (num12 * den1)
    den2  = (denst / num22)
    denmain2 = (num22 * den2)
    res1  = (num11 * den1 - num21 * den2)
    print (res1)
if actdo == 4:
    print ("-")
if actdo == 4:
    print (denmain2)





input()
