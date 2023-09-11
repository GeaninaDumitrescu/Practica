n=9
i=0

while i<3:
    k=int(input ("Guess: "))
    i+=1
    if k ==n:
        print("You won!")
        break
else:
    print("You failed!")