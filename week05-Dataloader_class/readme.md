# Week 5: DataLoader Class (Titanic Dataset)

This week, I focused on building a custom `DataLoader` class in Python to understand how real data pipelines start from basic file handling and structured method design.

Instead of using external libraries, I implemented everything with core Python so the logic stays clear and easy to debug.

## What I Learned

The main things I learned in this project:

- Loading data from a file and storing it in object state (`self.data`).
- Passing data between methods using class attributes.
- Applying validation conditions before processing, so the code does not run on empty or unloaded data.
- Using slicing for sampling (`lines[:n]`) and train/test style splitting.
- Writing a reusable class design with method chaining (`load().validate()` pattern).
- Calculating basic dataset statistics (rows and columns) without pandas.

## Implemented Methods

- `load()`: Reads the CSV/text file and stores the content in memory.
- `validate()`: Checks whether data is loaded; raises a clear error for invalid cases.
- `sample(n)`: Returns the first `n` lines for quick inspection.
- `split(ratio)`: Divides data into two parts based on the given ratio (train/test style).
- `stats()`: Returns total rows and number of columns.

## Visual Workflow

```text
Start
  |
  v
Create DataLoader(path)
  |
  v
load() -> file content stored in self.data
  |
  v
validate()
  |
  +--> If data is empty/not loaded -> Raise ValueError
  |
  v
Choose operation
  |
  +--> sample(n)      -> Return first n lines
  |
  +--> split(ratio)   -> Return train_data, test_data
  |
  +--> stats()        -> Return rows and columns
  |
  v
End
```

## Learning Value

Someone reading this project can quickly learn:

- How to structure data utilities inside a reusable Python class.
- How to guard methods with validation to avoid invalid operations.
- How slicing can support both quick previews and dataset partitioning.
- How to build a simple but extensible data pipeline without external libraries.

## How to Run

```bash
python dataloader.py
```

## Project Files

- `dataloader.py` - main class implementation and basic execution
- `titanic.csv` - dataset used for loading and testing

## Next Improvements

- Use the `csv` module for more reliable parsing than manual line splitting.
- Handle headers separately from data rows during splitting.
- Add more validations (invalid ratio, empty file, wrong path).
- Write unit tests for each method.

---
