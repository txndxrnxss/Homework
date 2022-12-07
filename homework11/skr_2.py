class Temp:

    def __init__(self):
        self.C = 0
        self.K = 273.15
        self.F = 32

    def celsius(self, C):
        self.C = C
        self.K = C + 273.15
        self.F = C * (9 / 5) + 32

    def kelvin(self, K):
        self.K = K
        self.C = K - 273.15
        self.F = (K - 273.15) * (9 / 5) + 32

    def fahrenhei(self, F):
        self.F = F
        self.C = (F - 32) * (5 / 9)
        self.K = (F - 32) * (5 / 9) + 273.15

temp_1 = Temp()
temp_1.fahrenhei(59)
print(temp_1.C)
print(temp_1.K)