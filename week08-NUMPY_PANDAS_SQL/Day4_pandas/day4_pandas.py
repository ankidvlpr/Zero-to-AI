import pandas as pd

# Series = A pandas 1-dimensional labeled array that can hold any data type
#           think like of single column in a spreadsheet (1=d dimensional)

# series, index, loc, iloc

data = [23, 13, 223, 232, 334, 23]

series = pd.Series(data, index=['a','b','c','d','e','f']) #index can be anything like tuple,list,array...

# series.loc['c'] = 200

# print(series.iloc[0])

print(series)

# for filter

print(series[series > 200])

# lets try with dictionary

portfolio = {"Day1": 100, "Day2": 300, "Day3": 200}

series = pd.Series(portfolio)
print(series)
series.loc["Day1"] += 50
print(series)
print(series.iloc[0])
print(series.iloc[1])
print(series.iloc[2])

print(series[series > 150]) # which day i have more than 150$

pokemon = ["Bulbasaur", "Isaura","Sauveur", "charmander", "Chameleon","charioted"]
series = pd.Series(pokemon, index=range(1, len(pokemon) + 1), dtype="object")

print(series.dtype)
print(series)


"""Dataframe = A tabular data structure with row and column (2D dimensional) similar to spreadsheet in excel"""

data = {
    "Name": ["Person1","Person2", "Person2"],
    "Age": [23,24,25],
}

dataframe = pd.DataFrame(data)

# adding new colum to data
dataframe["job"] = ["cook", "cashier", "driver"]

# adding new row to data

new_row = pd.DataFrame([{"Name": "Person3", "Age": 24, "job": "Scientist"}])

dataframe = pd.concat([dataframe, new_row], ignore_index=True)

print(dataframe)

#Importing csv and json

# df = pd.read_csv("pokemonDB_dataset.csv")
# print(df)
#
# print(df.to_string())  # to display all data!


# to read a json file

# df = pd.read_json("pokemonDB_dataset.json")
#
# print(df.to_string())


df = pd.read_csv("pokemonDB_dataset.csv", index_col="Pokemon")  # index_col uses to default by name so its easy to find the detail
# SELECTION by column
# Pokemon is index now, so examples using df["Pokemon"] stay commented.
# print(df["Pokemon"].to_string())
#
# print(df["Catch Rate"].to_string())

# concatenate column
# row = df["Pokemon"]
# row1 = df["Catch Rate"]
# result = pd.concat([row, row1], axis=1).to_string()
# print(result)

# printing multiple column
# df = df[["Pokemon","Catch Rate"]]
#
# print(df.to_string())



# SELECTIOn by ROW
# these row examples print special text from Height/Weight, so they are better in notebook or UTF-8 terminal
# row = df.loc["Mewtwo"]
# row1 = df.loc[["Mewtwo","Pikachu"]].to_string() # multiple row location find (loc)
#
# print(row)
# print(row1)
# if we want to find specifix info in row
#
# row3 = df.loc["Mewtwo", ["Height", "Weight"]]
# print(row3)
#
# by slicing we can
# row3 = df.loc["Mewtwo":"Tynamo", ["Height", "Weight"]]
# print(row3)


#Small exercise ( finding pokemon stats by input user)

# stat = input("Enter Pokemon name: ")
#
# try:
#     print(df.loc[stat])
# except KeyError:
#     print(f"{stat} not found")
#

# Filtering

# we have to filter out Height >= 2 .

print(df["Height"].dtype)
# print(df["Height"].head(10))
print(pd.to_numeric(df["Height"], errors="coerce").describe())

df["Height_m"] = df["Height"].str.split().str[0].astype(float)
tall_pokemon = df[df["Height_m"] >= 2]
# print(tall_pokemon[["Species", "Height", "Height_m"]])


# Take the Height column, which has strings like "2.2 m (7′03″)".
# .str.split() splits each string by spaces: "2.2 m (7′03″)" → ["2.2", "m", "(7′03″)"]
# .str[0] takes the first piece from each row, which is "2.2".
# .astype(float) converts "2.2" into a numeric value.


# print(df["Height"].dtype)

# water_pokemon = df[df["Type"] == "Grass"]
# print(water_pokemon)


# aggregate function = Reduce a set values in a single summary value uses to
#                       summarize and analyze data often uses as groupby() function


# print(df.mean(numeric_only=True))   # numeric_only=True
# print(df.sum(numeric_only=True))   # numeric_only=True
# print(df.min(numeric_only=True))   # numeric_only=True
# print(df.max(numeric_only=True))   # numeric_only=True
print(df.count())  # count the column per item

# for single column

df["Height"] = df["Height"].str.split().str[0].astype(float) #"2.2 m (7′03″)". to numeric 2.2

print(df["Height"].mean())
print(df["Height"].sum())
print(df["Height"].min())
print(df["Height"].max())

#groupby() func
df["Catch Rate"] = df["Catch Rate"].str.extract(r"(\d+)").astype("Int64")
group = df.groupby("Type")
print(group["Catch Rate"].mean())
print(group["Catch Rate"].sum())
print(group["Catch Rate"].min())

print(df["Catch Rate"].head())

# Data Cleaning = The process of fixing/removing: incorrect, incomplete or irrelevant data. is done by data cleaning
# these examples change df in different ways, so try them one by one when you want practice


# Drop irrelevant columns
# df = df.drop(columns=["Type"])


# handing missing data(like removing if any column row item has NaN)
# df = df.dropna(subset=["Type"])  #in this data i think there is nowhere NAN but we can remember for later
# df = df.fillna({"Type": None}) # filling NaN value to None

# Fix inconsistent value
# df["Type"] = df["Type"].replace({"Dark": "DARK"})  # improving Dark to DARK
# print(df.to_string())

# Standardize text
# df["Pokemon"] = df["Pokemon"].str.lower()

# Fix data types
# df["Legendary"] = df["Legendary"].astype(bool)

# remove duplicate data
# print(df.head(5))
# df = df.drop_duplicates()
# print(df)
