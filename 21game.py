import random


def player(gamenumber):
    num=int(input("you can choose how many number want to enter 1-4"))
    while num>0:
        last=gamenumber[-1]
        if last+1==21:
            print("you  lose !")
            exit()
        gamenumber.append(last+1)
        num-=1
    print("after your turn")
    for i in gamenumber:
        print(i,end=" ")
    return gamenumber
        
        
        

def computer(gamenumber):
    
    last = gamenumber[-1]
    target = ((last // 5) + 1) * 5
    num = target - last
    if num == 0 or num > 4:
        num = random.randint(1, 4)
    print("> computer enters", num)
    
    while num > 0:
        last = gamenumber[-1]
        if last + 1 == 21:
            print("computer lose !")
            exit()
        gamenumber.append(last + 1)
        num -= 1
    
    print("after computer turn:")
    for i in gamenumber:
        print(i, end=" ")
    print()
    return gamenumber
    
    
        
        
        
if __name__=="__main__":
    print("🎯 Welcome to the 21 Number Game!")
    print("Rules:")
    print("1️⃣ You and the computer will say numbers starting from 1.")
    print("2️⃣ Each turn, you can say 1 to 4 numbers in order.")
    print("3️⃣ Whoever says 21 loses.\n")
    
    
    gamenumber=[0]
    x=int(input("press 1 to start first\npress 2 to start second\n"))
    while True:
       
        
        for i in gamenumber:
            print(i,end=" ")
        if x==1:
            gamenumber=player(gamenumber)
            gamenumber=computer(gamenumber)
        else:
            gamenumber=computer(gamenumber)
            gamenumber=player(gamenumber)
            
        
        
        
        
        
    
        
    
    
        
        
        
            
        
            
        
        
                