import copy

def get_details():
    name = input("Enter name (press Enter for default): ")
    roll = input("Enter roll number (press Enter for default): ")
    if name == "":
        name = "Harsha"
    if roll.isdigit():
        roll = int(roll)
    else:
        roll = 24110012122
    return name, roll

def create_data():
    ch = input("Do you want to enter custom data? (y/n): ")
    if ch.lower() == 'y':
        users = []
        n = int(input("Enter number of users: "))
        for i in range(n):
            f = input("Enter files (comma separated): ").split(',')
            u = int(input("Enter usage: "))
            users.append({
                "id": i + 1,
                "data": {"files": f, "usage": u}
            })
        return users
    else:
        return [
            {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
            {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
        ]

def replicate(users):
    a = users
    s = list(users)
    d = copy.deepcopy(users)
    return a, s, d

def modify(users, name, roll):
    for u in users:
        if roll % 2 == 0:
            u["data"]["files"].append(name + "." + str(roll) + ".txt")
        else:
            if len(u["data"]["files"]) > 0:
                u["data"]["files"].pop()
        u["data"]["usage"] += 100
        if len(u["data"]["files"]) > 1:
            u["data"]["files"].pop(0)

def check(before, after, shallow, deep):
    leak = 0
    safe = 0
    overlap = set()
    for i in range(len(after)):
        b = before[i]["data"]["files"]
        a = after[i]["data"]["files"]
        if b != a:
            leak += 1
        if deep[i]["data"]["files"] != a:
            safe += 1
        common = set(a) & set(shallow[i]["data"]["files"])
        overlap = overlap.union(common)
    return leak, safe, len(overlap)

# main
name, roll = get_details()

data = create_data()
before = copy.deepcopy(data)

print("\nBefore:", data)

a, s, d = replicate(data)

modify(a, name, roll)
modify(s, name, roll)
modify(d, name, roll)

print("\nAfter:")
print("Original:", data)
print("Shallow:", s)
print("Deep:", d)

result = check(before, data, s, d)

print("\nResult:", result)