import csv
#with type hints and doc type


class CSVStaticLoader:
    
    @staticmethod
    def loadFile_list(filename: str) -> list:
        """
        Loads a csv file and will return a **list**

        Args:

        'filename' : The filename of the csv file to be loaded 
            
        Returns:
            
        List
        """
        with open(filename, 'r') as f:
            data = list(csv.reader(f))
            return data

