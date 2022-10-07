class Pixel:
    def __init__(self,r=0, g=0, b=0) -> None:
        self.r = r
        self.g = g
        self.b = b
    
    def getPixelString(self):
        return str(self.r) + " " + str(self.g) + str(self.b)

class PPM:
    def __init__(self, rows = 2, cols = 2) -> None:
        self.rows = rows
        self.cols = cols
        p = Pixel()
        self.image = [p] * self.rows
        row = [p] * self.cols
        for r in range(self.rows):
            self.image[r] = row

    def printImage(self):
        p= self.image[0][0]
        print(p.getPixelString())

    def savePPM(self, file):
        with open(file,"a") as f:
            f.truncate(0)
            f.write("# PPM Image\n")
            info = "P3 " + str(self.cols) + " " + str(self.rows) + "\n"
            f.write(info)
            f.write("255\n")
           


p = PPM(3,5)
p.printImage()
p.savePPM("test.txt")



