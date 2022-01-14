import random
print("hello everyone\n let's play a game\nactully this is a game of hit and trail \ni will give you 5 chance to try your luck and you have to input any ofnum you know to match our secret number\nand if secret number matches with your inputed number then you simple won otherwise loose\n and this will be the end of game\n")
num=random.randint(1,100)
i,f=1,0
while(i<=5):
    print("enter",i,"num")
    tr=int(input())
    if(num==tr):
        print("congrats you won")
        f=1
        break
    else:
        i+=1
if(f==0):
    print("sorry you loose\n it's okay we will try next time")
    print("secret number =",num)


