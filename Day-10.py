import random
import copy
import pandas as pd
import numpy as np
import math

NAME = input("Enter your name: ")
roll_number = int(input("Enter your roll number: "))

seed_value = sum(ord(c) for c in NAME) + roll_number
random.seed(seed_value)
np.random.seed(seed_value)

def generate_zone_data():
    data = []
    for i in range(1, 16):
        record = {
            "zone": i,
            "metrics": {
                "traffic": random.randint(20, 100),
                "pollution": random.randint(30, 300),
                "energy": random.randint(50, 500)
            },
            "history": [random.randint(10, 100) for _ in range(3)]
        }
        data.append(record)
    return data

def personalize_dataset(data):
    if roll_number % 2 == 0:
        data.reverse()
        print(f"\n[{NAME}] EVEN Roll Rule → Dataset Reversed\n")
    else:
        data = data[3:] + data[:3]
        print(f"\n[{NAME}] ODD Roll Rule → Dataset Rotated by 3\n")
    return data

def create_copies(data):
    assignment_copy = data
    shallow_copy = copy.copy(data)
    deep_copy = copy.deepcopy(data)
    return assignment_copy, shallow_copy, deep_copy

def mutate_data(shallow_copy):
    shallow_copy[0]["metrics"]["traffic"] += 50
    shallow_copy[0]["metrics"]["pollution"] += 40
    shallow_copy[0]["metrics"]["energy"] += 60
    shallow_copy[0]["history"].append(999)
    total = (
        shallow_copy[0]["metrics"]["traffic"] +
        shallow_copy[0]["metrics"]["pollution"] +
        shallow_copy[0]["metrics"]["energy"]
    )
    shallow_copy[0]["risk_score"] = math.log(total)

def convert_to_dataframe(data):
    rows = []
    for item in data:
        rows.append({
            "zone": item["zone"],
            "traffic": item["metrics"]["traffic"],
            "pollution": item["metrics"]["pollution"],
            "energy": item["metrics"]["energy"]
        })
    return pd.DataFrame(rows)

def custom_risk_score(df):
    name_factor = len(NAME) * 0.1
    df["risk"] = np.log(
        df["traffic"] * 0.4 +
        df["pollution"] * 0.4 +
        df["energy"] * 0.2 +
        name_factor
    )
    return df

def analyze_data(df):
    print("\nMean Values:")
    print(df[["traffic", "pollution", "energy"]].mean())
    print("\nVariance:")
    print(df[["traffic", "pollution", "energy"]].var())

    traffic = df["traffic"].values
    pollution = df["pollution"].values

    correlation = np.sum(
        (traffic - np.mean(traffic)) *
        (pollution - np.mean(pollution))
    ) / (
        np.sqrt(np.sum((traffic - np.mean(traffic))**2)) *
        np.sqrt(np.sum((pollution - np.mean(pollution))**2))
    )

    print("\nManual Correlation (Traffic vs Pollution):")
    print(correlation)

    threshold = df["risk"].mean() + df["risk"].std()
    anomalies = df[df["risk"] > threshold]

    print("\nAnomaly Zones:")
    print(anomalies[["zone", "risk"]])

    return anomalies

def detect_patterns(original, shallow_copy, df):
    print("\n--- BEFORE vs AFTER ---")
    print("\nOriginal Data:")
    print(original[0])
    print("\nShallow Copy:")
    print(shallow_copy[0])

    if original[0] == shallow_copy[0]:
        print(f"\n[{NAME}] Hidden Corruption Detected ❗")

    risky_zones = df[df["risk"] > df["risk"].mean()]
    print("\nHigh Risk Zones:")
    print(risky_zones["zone"].tolist())

    print("\nCluster Detection:")
    zones = risky_zones["zone"].tolist()
    for i in range(len(zones) - 1):
        if zones[i+1] - zones[i] == 1:
            print(f"Cluster found between Zone {zones[i]} and Zone {zones[i+1]}")

def final_decision(df):
    max_risk = df["risk"].max()
    min_risk = df["risk"].min()
    stability_index = 1 / (df["risk"].var() + 1e-5)
    result_tuple = (max_risk, min_risk, stability_index)

    print("\nRisk Tuple:")
    print(result_tuple)

    avg_risk = df["risk"].mean()

    if avg_risk < 4:
        decision = "System Stable"
    elif avg_risk < 5:
        decision = "Moderate Risk"
    elif avg_risk < 6:
        decision = "High Corruption Risk"
    else:
        decision = "Critical Failure"

    print(f"\nFinal Decision for {NAME}: {decision}")
    return result_tuple

data = generate_zone_data()

print("\n--- BEFORE MUTATION ---")
print(data)

data = personalize_dataset(data)

assignment_copy, shallow_copy, deep_copy = create_copies(data)

print("\nBefore Mutation Sample:")
print("Original:", data[0])
print("Deep Copy:", deep_copy[0])

mutate_data(shallow_copy)

print("\n--- AFTER MUTATION ---")
print("Original:", data[0], " <-- CORRUPTED ❗")
print("Deep Copy:", deep_copy[0], " <-- SAFE ✅")

df = convert_to_dataframe(data)
df = custom_risk_score(df)

print("\n--- DataFrame ---")
print(df)

analyze_data(df)

detect_patterns(data, shallow_copy, df)

print("\nDeep Copy Safe Data:")
print(deep_copy[0])

print("\nWhy shallow copy corrupts nested structures?")
print("Because it copies only outer objects while inner dictionaries and lists still share references.")

final_decision(df)

print("\n--- UNIQUE IDENTIFIER ---")
print(f"Student: {NAME}")
print(f"Roll Number: {roll_number}")
print(f"Seed Used: {seed_value}")