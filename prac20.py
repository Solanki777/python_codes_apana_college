
def rec(hero,index):
    if index==len(hero):
        return
    print(hero[index])
    rec(hero,index+1)
heros=["ironman","captain","thor","loki",7,89,79]
rec(heros,0)

