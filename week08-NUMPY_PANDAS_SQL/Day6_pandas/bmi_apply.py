import pandas as pd

# make a dataframe of Patient, height, weight
# make a function to calculate bmi
# apply Bmi colum to calculate BMi for each row


df = pd.DataFrame({
    "Patient": ["A","B","C","D"],
    "Height_m": [1.32, 1.90, 1.56, 1.47],
    "Weight_kg": [70, 56, 67, 89]
})

def cal_Bmi(row):
    return row["Weight_kg"]/ (row["Height_m"]**2)

df["BMI"] = df.apply(cal_Bmi, axis=1)
print(df)
