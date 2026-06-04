import csv
import io

class CSVDataLoader:
    """Load and inspect CSV file content.

    This class reads CSV data from a file path and provides helper
    methods for validation, sampling, splitting, and basic statistics.

    Attributes:
        path: Path to the CSV file.
        data: Raw file content loaded from the CSV file.
    """

    def __init__(self, path):
        """Initialize the loader with a file path.

        Args:
            path: Path to the CSV file.
        """
        self.path = path
        self.data = None

    def load(self):
        """Read the CSV file and store its raw content.

        Returns:
            CSVDataLoader: The current loader instance.
        """
        with open(self.path, "r", encoding="utf-8") as file:
            content = file.read()
            self.data = content
            return self

    def validate(self):
        """Validate that data has been loaded and is not blank.

        Returns:
            CSVDataLoader: The current loader instance.

        Raises:
            ValueError: If data is not loaded or the file is empty.
        """

        if self.data is None:
            raise ValueError("Data is not loaded")
        if self.data.strip() == "":
            raise ValueError("Blank/Empty file")

        return self

    def _get_lines(self):
        """Return the loaded data as a list of lines.

        Returns:
            list[str]: The loaded file content split into lines.

        Raises:
            ValueError: If data is not loaded or the file is empty.
        """
        self.validate()
        return self.data.splitlines()


    def sample(self, n):
        """Return the first n lines from the loaded data.

        Args:
            n: Number of lines to return.

        Returns:
            list[str]: The first n lines from the file.

        Raises:
            TypeError: If n is not an integer.
            ValueError: If n is negative or data is invalid.
        """
        self.validate()
        if not isinstance(n, int):
            raise TypeError('n must be integer')
        if n < 0:
            raise ValueError('n must be >= 0')

        lines = self._get_lines()
        return lines[:n]

    def split(self, ratio):
        """Split the CSV rows into train and test sets.

        The header row is excluded before splitting.

        Args:
            ratio: Fraction of rows to include in the train split.

        Returns:
            tuple[list[str], list[str]]: Train rows and test rows.

        Raises:
            TypeError: If ratio is not numeric.
            ValueError: If ratio is outside the range 0 to 1 or data is invalid.
        """
        self.validate()

        if not isinstance(ratio, (int, float)):
            raise TypeError('ratio must be numeric')

        if ratio < 0 or ratio > 1:
            raise ValueError('ratio must be between 0 and 1')

        lines = self._get_lines()
        header = lines[0]
        rows = lines[1:]
        split = int(len(rows) * ratio)

        train_data = rows[:split]
        test_data = rows[split:]

        return train_data, test_data

    def stats(self):
        """Return basic statistics about the loaded CSV data.

        Returns:
            dict[str, int]: A dictionary with row and column counts.

        Raises:
            ValueError: If the CSV data is empty or invalid.
        """
        self.validate()

        reader = csv.reader(io.StringIO(self.data))
        rows = list(reader)

        if not rows:
            raise ValueError('Empty Data')
        lines = self._get_lines()

        columns = len(rows[0])
        rows_count = len(rows)

        return {"rows": rows_count,
                "columns": columns
                }

if __name__ == "__main__":
    loader1 = CSVDataLoader("titanic.csv")
    loader1.load()
    print(loader1.sample(3))
