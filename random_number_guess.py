import time
import random
print("*"*62)
print("==========WELCOME TO THE RANDOM NUMBER GUESSING GAME==========")
print("*"*62)
time.sleep(2)
print("THIS GAME ALLOWS YOU TO GUESS A RANDOM NUMBER WITHIN A RANGE YOU SPECIFY")
print("PRO TIP: DON'T TAKE TOO HIGH OF A RANGE :)")
time.sleep(2)
def main(v):
    print("START BY ENTERING THE RANGES")
    a=int(input("LOWER RANGE: "))
    b=int(input("UPPER RANGE: "))
    if(a==b):
          print('SORRY, YOU CANNOT CHOOSE THE SAME NUMBER AS LOWER AND UPPER RANGE, TRY AGAIN')
          main(v-1)
    s=random.randint(a,b)
    print("""NOW IT'S TIME TO GUESS YOUR NUMBER
CHOOSE WISELY""")
    o=int(input())
    if(s==o):
        print("CONGRATS, YOU SUCCESSFULLY GUESSED THE NUMBER. YOUR LUCK IS LOOKING GOOD")
        again()
    elif(s!=o):
        v-=1
        print(f"SORRY BUDDY, YOU GUESSED WRONG, THE RIGHT ANSWER WAS {s}")
        print(f"YOU HAVE {v} LIVES LEFT")
        time.sleep(2)
        if(v==0):
            again()
        else:
            main(v)
    else:
        print("INVALID CHARACTER ENTERED")
        exit()
def again():
    p=input("WOULD YOU LIKE TO TRY AGAIN? (Y/N): ")
    print('-'*62)
    if(p in 'Yy'):
          main(n)
          
    elif(p in 'Nn'):
        print("""NICE PLAYING WITH YOU
exiting...""")
        time.sleep(2)
        exit()
n=3
main(n)
