class DataLoader:

    def __init__(self, path):
        self.path = path 
        self.data = None

    def load(self):
        with open(self.path, "r") as file:  
            content = file.read()
            self.data = content 
            return self #store data in content
            
    def validate(self):
        if not self.data:  # check if self.data is empty return False
            raise ValueError("Data is empty or not loaded")
        return self                 #chaining
    
    def sample(self, n):
        if self.data is None:   # check is data is None raise error
            raise ValueError("Please load the data")
        lines = self.data.splitlines()
        return lines[:n]
    
    def split(self, ratio):
        if self.data is None:
            raise ValueError("Please load the data")
        '''get split lines then find 
          the index of split for train_dat and test_data
        '''
        lines = self.data.splitlines() 
        split = int(len(lines)*ratio)     ## 

        train_data = lines[:split]
        test_data = lines[split:]

        return train_data, test_data
    
    def stats(self):
        if self.data is None:
            raise ValueError("Please load the data")                    
        """ finding row and columns """
        lines = self.data.splitlines()
        find_column = lines[0].split(",")
        column = len(find_column)

        rows = len(lines)
        return {"rows": rows,
                "columns" : column
                }

    
    
loader1 = DataLoader("titanic.csv")
loader1.load()
# print(loader1.sample(3))
print(loader1.split(0.8))
print(loader1.stats())
    