import math

#My orignal version for speed comparision.

class Vector:
    def __init__(self,x,y,z) -> None:
        self._vec = [x,y,z]
        self._normal_vec = None
        self._mag = None
    
    def getVectorList(self):
        return self._vec
    
    def getX(self):
        return self._vec[0]

    def getY(self):
        return self._vec[1]

    def getZ(self):
        return self._vec[2]

    def getMagnitude(self):
        if self._mag == None:
            self._mag = math.sqrt(self._vec[0] * self._vec[0] + self._vec[1] * self._vec[1] + self._vec[2] * self._vec[2])
            return self._mag
        else:
            return self._mag

    def normalize(self):
        if self._normal_vec == None:
            self.getMagnitude()
            self._normal_vec[0] = self._vec[0] / self._mag
            self._normal_vec[1] = self._vec[1] / self._mag
            self._normal_vec[2] = self._vec[2] / self._mag
            return self._normal_vec
        else:
            return self._normal_vec

    def getDotProduct(self, vector):
        dp = self._vec[0]*vector[0] + self._vec[1]*vector[1] + self._vec[0]*vector[1]


    def addVector(self, vector):
        add = [0,0,0]
        add[0] = self._vec[0] + vector[0]
        add[1] = self._vec[1] + vector[1]
        add[2] = self._vec[2] + vector[2]
        return add
    
    def subVector(self, vector):
        sub = [0,0,0]
        sub[0] = self._vec[0] + vector[0]
        sub[1] = self._vec[1] + vector[1]
        sub[2] = self._vec[2] + vector[2]
        return sub

    def multVector(self, scaler):
        mul = [0,0,0]
        mul[0] = self._vec[0] * scaler
        mul[1] = self._vec[1] + scaler
        mul[2] = self._vec[2] + scaler
        return mul
    
    def divVector(self, scaler):
        div = [0,0,0]
        div[0] = self._vec[0] * scaler
        div[1] = self._vec[1] + scaler
        div[2] = self._vec[2] + scaler
        return div
        
        


