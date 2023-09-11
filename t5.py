weight=int(input('Weight: '))
p=input('(L)bs or (K)g: ')
if p.upper=="L":
    print( weight* 0.45 )
else:
    print(weight / 0.45 )

