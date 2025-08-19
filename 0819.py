'''score=int(input())


if score >= 60 and score <= 100:
    print("Pass")


else:
    print("Fail")
    '''
'''score=int(input())
if (score%2==0):
    print("EVEN")

else:
        print("Odd")'''

'''y=int(input("year: "))
if ((y % 4 == 0 and y % 100 !=0) or y%400==0):
    print("leap year")
else:
        print("common year")

'''
'''
score=int(input())

if score>= 90:
    print("A")
elif score>= 80:
    print("B")
elif score>= 70:
    print("c")
elif score>= 60:
    print("D")
else:
    print("f")
'''


'''i=1
while (i<=10):
    print(i, end=' ')
    i+=1'''
'''sum=0
i=1
n=int(input())
while i <=n:
    sum=sum+i

    i=i+1
print(sum)'''

'''i=0
while i<10:
    i+=1
    if i%2==0:
        continue
    print(i, end='')'''

'''while True:
    ans=input("shall we close?(y/n)")
    if ans== "y":
        print("The end")
        break'''
'''for i in range(10):
    print(i, end =' ')

for i in range(10,21):
    print(i,end=' ')
    
for i in range(1,10,2):
    print(i, end=' ')'''
'''
n=int(input("몆 단?"))
for i in range(1,10):
      print("%d*%d=%d"%(n,i,n*i))'''
'''for i in range(2,10):
    print("< %d 단>"%i)
    for j in range(1,10):
        print("%d*%d=%2d"%(i,j,i*j))
    print()'''


sum=0
n=int(input())

for i in range(0,n+1,2):
    print(i,end= ' ')
    sum=sum+i
print()
print(sum)
    
    
    

