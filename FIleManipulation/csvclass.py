import csv
#with type hints and doc type


class CSVloader:
    """This class handels the loading of a csv file

       Args:

       'filename' : The name of the csv file to load
    
    """
    def __init__(self,filename: str ) -> None:
        self.filename = filename
    
    def loadFile_list(self) -> list:
        """
        Loads a csv file and will return a **list**
            
        Returns:
            
        List
        """
        with open(self.filename, 'r') as f:
            data = list(csv.reader(f))
            return data


