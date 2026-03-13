# Messy CSV Cleaner (Titanic Dataset) 🧹

A simple Python script built to clean a messy dataset of Titanic passengers using the built-in `csv` module.

The program reads an uncleaned CSV file, performs several data cleaning operations step-by-step, and outputs a properly formatted and cleaned CSV file.

## Cleaning Operations Performed

The script takes [uncleaned_titanic.csv](cci:7://file:///c:/Users/ankit/Desktop/Zero-to-AI/week4-messy_csv_cleaner/uncleaned_titanic.csv:0:0-0:0) and applies the following fixes before saving it as [cleaned.csv](cci:7://file:///c:/Users/ankit/Desktop/Zero-to-AI/week4-messy_csv_cleaner/cleaned.csv:0:0-0:0):

- **Fix Missing Ages**: Finds the median age from available data and fills all empty `Age` cells with it.
- **Remove Empty Cabins**: Finds all empty `Cabin` cells and replaces them with `"Unknown"`.
- **Fix Missing Ports**: Finds any empty `Embarked` cells and replaces them with `"S"` (the most common port).
- **Remove Extra Spaces**: Scans every single cell in the CSV and strips away unnecessary leading or trailing spaces (e.g., `" male "` becomes `"male"`).


## What I learned

This project helped me understand how to:

- Reads and writes CSV files using `csv.reader` and `csv.writer`
- Calculates the median of a numerical column (Age)
- Replaces missing numerical data with the calculated median
- Handles missing text data 

## How to run

Run the Python file:

```bash
python csv_cleaner.py
```