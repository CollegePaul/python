
def area(length: float, width: float) -> float:
    """My area function"""
    if isinstance(length, complex) or isinstance(width, complex):
        return length * width
    try:
        length = float(length)
        width = float(width)
        if (length < 0 or width < 0):
            return "Error: Must be postive"
        return length * width
    except:
        return "Error: must be a number"

#code to run
#print(area(4,6))

#the function could return -1 if error....