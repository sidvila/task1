import numpy as np
import pandas as pd

# ---------- NumPy Operations ----------
print("NumPy Operations")

numbers = np.array([10, 20, 30, 40, 50])

print("Original Array:", numbers)

# Calculate average using NumPy
average = np.mean(numbers)
print("Average:", average)

# Broadcasting example
result = numbers * 2
print("Array after broadcasting (*2):", result)


# ---------- Pandas Data Manipulation ----------
print("\nPandas DataFrame Operations")

data = {
    "Name": ["Asha", "Ravi", "Kiran", "Meena", "Ravi"],
    "Age": [21, 22, 23, None, 22],
    "Score": [85, 90, 88, 92, 90]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

print("\nCleaned Dataset:")
print(df)

# Calculate average score
average_score = df["Score"].mean()

print("\nAverage Score:", average_score)