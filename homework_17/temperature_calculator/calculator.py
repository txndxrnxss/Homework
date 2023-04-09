class Calculator:
    
    def __init__(self):
        self.F = 32
        self.K = 273.15
        self.C = 0

    def Celsius(self, C):
        self.C = C
        self.K = C + 273.15
        self.F = C * (9 / 5) + 32

    def Kelvin(self, K):
        self.K = K
        self.C = K - 273.15
        self.F = (K - 273.15) * (9 / 5) + 32

    def Fahrenhei(self, F):
        self.F = F
        self.C = (F - 32) * (5 / 9)
        self.K = (F - 32) * (5 / 9) + 273.15