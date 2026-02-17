weights=[]
n=int(input("enter no.of pacakges:"))
weights=[0]*n
for i in range(n):
    w=int(input("Enter weight "+str(i+1)+": "))
    weights[i]=w
very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid_entries=[]
for w in weights:
    if w<0:
        invalid_entries=invalid_entries+[w]
    elif w>=0 and w<=5:
        very_light=very_light+[w]
    elif w>=6 and w<=25:
        normal_load=normal_load+[w]
    elif w>=26 and w<=60:
        heavy_load=heavy_load+[w]
    elif w>60:
        overload=overload+[w]
print("Very Light:",very_light)
print("Normal Load:",normal_load)
print("Heavy Load:",heavy_load)
print("Overload:",overload)
print("Invalid Entries:",invalid_entries)
