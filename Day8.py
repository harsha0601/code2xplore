import random
import pandas as pd
import numpy as np
import math

student_name = input("Enter your name: ")
roll_number = int(input("Enter your roll number: "))
num_zones = int(input("Enter number of zones (15-20 recommended): "))

print("\nChoose Priority:")
print("1. Air Quality")
print("2. Traffic")
print("3. Energy")

choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    priority = "Air Quality"
elif choice == 2:
    priority = "Traffic"
else:
    priority = "Energy"

def generate_data(n):
    data = []
    for i in range(n):
        data.append({
            "zone": i + 1,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        })
    if n >= 3:
        data[0]["traffic"] = 0
        data[1]["air_quality"] = 290
        data[2]["energy"] = 480
    return data

def classify_zone(r):
    if r["air_quality"] > 200 or r["traffic"] > 80:
        return "High Risk"
    elif r["energy"] > 400:
        return "Energy Critical"
    elif r["traffic"] < 30 and r["air_quality"] < 100:
        return "Safe Zone"
    return "Moderate"

def calculate_risk_score(r):
    if priority == "Air Quality":
        w_t, w_a, w_e = 0.2, 0.6, 0.2
    elif priority == "Traffic":
        w_t, w_a, w_e = 0.5, 0.3, 0.2
    else:
        w_t, w_a, w_e = 0.2, 0.3, 0.5
    score = r["traffic"] * w_t + r["air_quality"] * w_a + r["energy"] * w_e
    return math.sqrt(score)

def custom_sort(data, key, reverse=True):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if reverse:
                if data[j][key] < data[j + 1][key]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            else:
                if data[j][key] > data[j + 1][key]:
                    data[j], data[j + 1] = data[j + 1], data[j]
    return data

def detect_patterns(df):
    threshold = df["risk_score"].mean()
    high_risk = df[df["risk_score"] > threshold]
    variance = np.var(df["traffic"])
    stability = "Stable" if variance < 800 else "Unstable"
    clusters = []
    temp = []
    for _, row in df.iterrows():
        if row["risk_score"] > threshold:
            temp.append(row["zone"])
        else:
            if len(temp) > 1:
                clusters.append(temp)
            temp = []
    return high_risk, stability, clusters

zones = generate_data(num_zones)

if priority == "Air Quality":
    zones = custom_sort(zones, "air_quality", reverse=False)
    strategy = "Best Air Quality First"
elif priority == "Traffic":
    zones = custom_sort(zones, "traffic", reverse=False)
    strategy = "Low Traffic First"
else:
    zones = custom_sort(zones, "energy", reverse=False)
    strategy = "Low Energy Usage First"

if roll_number % 3 == 0:
    random.shuffle(zones)

for r in zones:
    r["category"] = classify_zone(r)
    r["risk_score"] = calculate_risk_score(r)

df = pd.DataFrame(zones)

mean_values = np.mean(df[["traffic", "air_quality", "energy"]])

sorted_by_risk = custom_sort(zones.copy(), "risk_score", reverse=True)
top3 = sorted_by_risk[:3]

high_risk, stability, clusters = detect_patterns(df)

max_risk = df["risk_score"].max()
avg_risk = df["risk_score"].mean()
min_risk = df["risk_score"].min()

if avg_risk < 10:
    decision = "City Stable"
elif avg_risk < 15:
    decision = "Moderate Risk"
elif avg_risk < 20:
    decision = "High Alert"
else:
    decision = "Critical Emergency"

print(f"\n--- Smart City Report by {student_name} ---")
print("Priority:", priority)
print("Zones:", num_zones)

print("\nData:\n", df)

print("\nMean Values:\n", mean_values)

print("\nTop 3 Risk Zones:")
for z in top3:
    print(z)

print("\nRisk Stats:", (max_risk, avg_risk, min_risk))
print("Stability:", stability)
print("Clusters:", clusters)

print("\nStrategy:", strategy)
print("Final Decision:", decision)

print("\nInsight:")
print("A smart city prioritizes key resources and optimizes conditions based on real-time needs.")