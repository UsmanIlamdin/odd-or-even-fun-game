import random as r
dec1=input("Odd or Even :  ").lower()
t1=int(input("User Input: "))
t2=r.randint(1,6)
print(f"AI input: {t2}")
toss=t1+t2
if toss%2 == 0:
    dec="even"
else:
    dec="odd"
if dec1==dec:
    play=int(input("Batting(1) or Bowling(2)? "))
else:
    play=r.randint(1,2)
if play==1:
    print("You are batting!")
else:
    print("You are bowling!")
#-------------------------------
if play==1:
    runs1=0
    while True:
        r1=int(input("User input: "))
        r2=r.randint(1,6)
        print(f"AI input: {r2}")
        if r1==r2:
            print(f"OUT!!! \nYour Score: {runs1}")
            break
        else:
            runs1+=r1

    print("Bowl and beat AI")
    runs2 = 0
    while runs1>runs2:
        r1 = int(input("User input: "))
        r2 = r.randint(1, 6)
        print(f"AI input: {r2}")
        if r1 == r2:
            print(f"OUT!!! \nAI Score: {runs2}\nYour Score: {runs1}\nYou Won")
            break
        else:
            runs2 += r2
    if runs2>runs1:
        print(f"AI Score: {runs2}\nYour Score: {runs1}\nYou Lost")
#-------------------------------
if play==2:
    runs2 = 0
    while True:
        r1 = int(input("User input: "))
        r2 = r.randint(1, 6)
        print(f"AI input: {r2}")
        if r1 == r2:
            print(f"OUT!!! \nAI Score: {runs2}")
            break
        else:
            runs2 += r2
    print("Bat and beat AI")
    runs1 = 0
    while runs2>runs1:
        r1 = int(input("User input: "))
        r2 = r.randint(1, 6)
        print(f"AI input: {r2}")
        if r1 == r2:
            print(f"OUT!!! \nYour Score: {runs1} \nAI Score: {runs2}\nYou Lost!")
            break
        else:
            runs1 += r1
    if runs1>runs2:
        print(f"Your Score: {runs1}\nAI Score: {runs2}\nYou Won!!!")
#-------------------------------
