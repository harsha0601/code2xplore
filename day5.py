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
full_name="injam venkata gopi harsha vardhan"
L=0
for ch in full_name:
    if ch!=" ":
        L=L+1
PLI=L%3
removed_items=very_light+overload
affected_items=len(removed_items)
very_light=[]
overload=[]
valid_count=len(normal_load)+len(heavy_load)
final_elements=normal_load+heavy_load+invalid_entries
destination=input("Enter Destination of Load: ")
count=0
for ch in destination:
    if ch!=" ":
        count=count+1
print("Full Name:",full_name)
print("Full Name Length (L):",L)
print("PLI Value:",PLI)
print("Applied Rule: Rule C")
print("Final Loading Plan:")
print("Very Light:",very_light)
print("Normal Load:",normal_load)
print("Heavy Load:",heavy_load)
print("Overload:",overload)
print("Invalid Entries:",invalid_entries)
print("Total Valid Weights:",valid_count)
print("Affected Items due to PLI:",affected_items)
print("Items removed because of personalization:",removed_items)
print("All Remaining Elements:",final_elements)
if count%2==0:
    print("** Go Safe **")
else:
    print("!! Drive Safe !!")
