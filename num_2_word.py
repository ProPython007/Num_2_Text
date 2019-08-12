#creating  number into words
x=["","one","two","three","four","five","six","seven","eight","nine"]
y=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
z=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
n=int(input("enter a positive number: "))
if n>99999:
    print("not possible greater than 99999")
else:
    d=[0,0,0,0,0]
    i=0
    while n>0:
        d[i]=n%10
        i+=1
        n=n//10
num=""
if d[4]!=0:
    if d[4]==1:
        num+=z[d[3]]+ " thousand "
    else:
        num+=y[d[4]] +" " + x[d[3]]+ " thousand "
else:
    if d[3]!=0:
        num+=x[d[3]]+ " thousand  "
if d[2]!=0:
    num+=x[d[2]] + " hundred  "
if d[1]!=0:
    if d[1]==1:
        num+=z[d[0]]
    else:
        num+=y[d[1]] +" " + x[d[0]]
else:
    if d[0]!=0:
        num+=x[d[0]]
print(num)
input()
