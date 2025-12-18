import random
import time

# 22 Challenges (shortened)
CHALLENGES = {
    1: ("Hello World", 'print("Hello World")'),
    2: ("Welcome MRIST", 'print("Welcome to MRIST")'),
    3: ("Print Name", 'name=input("Name:");print(name)'),
    4: ("Name+MRIST", 'name=input("Name:");print(name+" - MRIST")'),
    5: ("Even/Odd", 'n=int(input());print("Even"if n%2==0 else "Odd")'),
    6: ("Pos/Neg", 'n=int(input());print(["Neg","Zero","Pos"][1+(n>0)-(n<0)])'),
    7: ("Vowel", 'c=input().lower();print("Vowel"if c in"aeiou"else"Consonant")'),
    8: ("Leap Year", 'y=int(input());print("Leap"if(y%4==0and y%100!=0)or y%400==0 else"Not")'),
    9: ("Circle Area", 'import math;r=float(input());print(math.pi*r**2)'),
    10: ("Triangle", 'b,h=float(input()),float(input());print(b*h/2)'),
    11: ("Rectangle", 'l,w=float(input()),float(input());print(l*w)'),
    12: ("Square", 's=float(input());print(s**2)'),
    13: ("1-100", 'print(*range(1,101))'),
    14: ("Even 10-100", 'print(*range(10,101,2))'),
    15: ("Odd 10-100", 'print(*[i for i in range(10,101)if i%2])'),
    16: ("Sum 1-n", 'n=int(input());print(sum(range(1,n+1)))'),
    17: ("Even Sum", 'n=int(input());print(sum(range(2,n+1,2)))'),
    18: ("Factorial", 'from math import factorial;n=int(input());print(factorial(n))'),
    19: ("Star Pattern", 'n=int(input());[print("*"*i)for i in range(1,n+1)]'),
    20: ("Table", 'n=int(input());[print(f"{n}x{i}={n*i}")for i in range(1,11)]'),
    21: ("Even Func", 'def e(n):return"Even"if n%2==0 else"Odd";print(e(int(input())))'),
    22: ("Leap Func", 'def l(y):return"Leap"if(y%4==0and y%100!=0)or y%400==0 else"Not";print(l(int(input())))')
}

class MiniLottery:
    def __init__(self):self.p,self.h=[],[]
    def reg(self):
        print("🎰 MRIST MINI LOTTERY 🎰")
        n=int(input("Players: "))
        for i in range(1,n+1):
            name=input(f"Player {i}: ")
            self.p.append((f"MRIST-{i:03d}",name))
            print(f"✓ {name} = MRIST-{i:03d}")
    def draw(self):
        print("\n🎲 DRAWING...")
        for _ in range(10):print(f"🎰 {random.choice(self.p)[0]} 🎰",end="\r");time.sleep(0.1)
        win=random.choice(self.p);print(f"\n✅ WINNER: {win[0]} - {win[1]}")
        return win[0]
    def chal(self,code):
        c=random.randint(1,22);chal=CHALLENGES[c]
        print(f"\n📝 #{c} {chal[0]}\nTASK: Write code\nSOLUTION:\n{chal[1]}\n")
        self.h.append((code,chal[0]))
    def play(self):
        self.reg()
        while input("\nPlay?(y/n): ").lower()=="y":
            code=self.draw()
            self.chal(code)
        print("\n📊 STATS:")
        for code,name in self.p:print(f"{name}: {self.h.count(code)} wins")

if __name__=="__main__":MiniLottery().play()
