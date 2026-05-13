import datetime
while True:
    
    def prime(l):
        if len(l) == 2:
            return(1)
        else:
            return(0)
        
    def divisors(num):
        l=[]
        for i in range(num):
            i = i+1
            r = num%i
            if r == 0 :
                l.append(i)
        return(l)

    def mersen(power):
        num = 2**power - 1
        l = divisors(num)
        p = prime(l)
        if p == 1:
            print(datetime.datetime.now(),f" - Found!\n > {num} is mersen prime\n")

    limit = int(input("maximum power :\n  >  "))
    print("\n")
    
    for n in range(limit):
        n = n+1
        print(datetime.datetime.now(),f" - solving for power of {n} ..")
        mersen(n)
    print("done.")
