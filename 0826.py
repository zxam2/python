'''total=int(input("총 좌석수를 입력하세요:"))
print("현재 잔여석: %d"%total)

while(True):
    n=int(input("예약할 좌석수를 입력하세요:"))
    if(total<n):
        print("잔여석이 부족합니다")

    else:
        total=total-n
        print('현재 잔여석: %d'%total)
    if(total==0):
        print("남은 예약석이 없습니다")
        break
    '''
'''       
num=int(input("시험을 본 과목의 수를 입력하세요:"))



sub=[]
for i in range(num):
    score=int(input("%d번쨰 시험점수:"%(i+1)))
    sub.append(score)

print("%d과목의 평균은 %.2if점입니다.."%(num, sum(sub)/num))
''''''n=int(input())

res=0

while(True):
    res=res+n%10
    n=n//10

    if(n==0):
        break

    res=res*10

print(res)


n=int(input())

res=0


'''
'''
while(True):
    n=int(input())
    cnt=0
    if(n<2):
        break
    for i in range(2,n):
        if(n%i==0):
            cnt=cnt+1
            break

    if(cnt>0):
        print("소수가 아니다")
    else:
        print("소수다") 

'''
n=int(input())
for i in range(2,n+1):
    cnt=0
    for i in range(2,i):
        if(i%j==0):
            cnt=cnt+1
            break
    if(cnt==0):
        print(i,end=' ')

