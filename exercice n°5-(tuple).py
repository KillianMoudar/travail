def ajoute(t1,t2):
    t = ()
    for i in range(len(t1)):
        t=t + (t1[i] + t2[i],)
    return t

print(ajoute((3,1,5),(6,0,2)))