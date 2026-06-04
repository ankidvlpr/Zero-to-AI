# Messy CSV Cleaner (Titanic Dataset) 

A simple Python script built to clean a messy dataset of Titanic passengers using the built-in `csv` module.

The program reads an uncleaned CSV file, performs several data cleaning operations step-by-step, and outputs a properly formatted and cleaned CSV file.

## Cleaning Operations Performed

The script takes `uncleaned_titanic.csv` and applies the following fixes before saving it as `cleaned.csv`:

- **Fix Missing Ages**: Finds the median age from available data and fills all empty `Age` cells with it.
- **Remove Empty Cabins**: Finds all empty `Cabin` cells and replaces them with `"Unknown"`.
- **Fix Missing Ports**: Finds any empty `Embarked` cells and replaces them with `"S"` (the most common port).
- **Remove Extra Spaces**: Scans every single cell in the CSV and strips away unnecessary leading or trailing spaces (e.g., `" male "` becomes `"male"`).


## What I learned

This project helped me understand how to:

- Read and write CSV files using `csv.reader` and `csv.writer`
- Calculate the median of a numerical column (Age)
- Replace missing numerical data with the calculated median
- Handle missing text data

## How to run

Run the Python file:

```bash
python csv_cleaner.py
```
