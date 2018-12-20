import math
print ("1, easy")
class Triangle ():
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx
        self.Cy = Cy
        self.AB = round (math.sqrt(int (math.fabs(((By - Ay)**2) + ((Bx - Ax)**2)))),2)
        self.BC = round(math.sqrt(int(math.fabs(((Cy - By) ** 2) + ((Cx - Bx) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((Ay - Cy) ** 2) + ((Ax - Cx) ** 2)))), 2)

    def Per(self):
        self.Per = round((self.AB + self.BC + self.CA),3)
        return (self.Per)

    def Sq(self):
        self.Per /=2
        self.Sq =  round(math.sqrt(self.Per*(self.Per - self.AB)*(self.Per - self.BC)* (self.Per - self.CA)),2)
        return (self.Sq)

    def H(self):
        self.Sq *=2
        self.H =  round((self.Sq / self.CA),2)
        return (self.H)
primer = Triangle(0,1,20,30,40,50)
print('Периметр = {}'.format(primer.Per()))
print('Площадь = {}'.format(primer.Sq()))
print('Высота = {}'.format(primer.H()))
print()
print("2, easy")
class Trapeciya ():
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Cx = Cx
        self.Cy = Cy
        self.Dx = Dx
        self.Dy = Dy
        self.AB = round (math.sqrt(int (math.fabs(((By - Ay)**2) + ((Bx - Ax)**2)))),3)
        self.BC = round(math.sqrt(int(math.fabs(((Cy - By) ** 2) + ((Cx - Bx) ** 2)))), 3)
        self.CD = round(math.sqrt(int(math.fabs(((Dy - Cy) ** 2) + ((Dx - Cx) ** 2)))), 3)
        self.DA = round(math.sqrt(int(math.fabs(((Ay - Dy) ** 2) + ((Ax - Dx) ** 2)))), 3)
    def Proverka(self):
        if self.AB == self.CD and math.sqrt((self.AB**2-(self.DA-self.BC)**2/4)) == (math.sqrt(self.CD**2-(self.DA-self.BC)**2/4)):
            print("Ravnobochnaya trapeciya")
        else:
            print("Neravnobochnaya trap")
    def Per(self):
        self.Per = round((self.AB + self.BC + self.CD + self.DA),3)
        return self.Per
    def H(self):
        self.H = round(math.sqrt(self.AB**2 - (self.DA - self.BC)**2 / 4), 3)
        return(self.H)
    def Sq(self):
        self.Sq = round(((self.DA + self.BC) / 2 * math.sqrt(self.AB**2-(self.DA-self.BC)**2/4)),3)
        return self.Sq
primer = Trapeciya(0,0,1,10,11,10,12,0)
primer.Proverka()
print('Периметр = {}'.format(primer.Per()))
print('Площадь = {}'.format(primer.Sq()))
print('Высота = {}'.format(primer.H()))
print()
            
