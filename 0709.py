class Rac:
    wid = 0
    hei = 0

    def area(self):
        print(self.wid * self.hei)

    def per(self):
        print(2 * (self.wid + self.hei))

    def des(self, wid, hei):
        self.wid = wid; self.hei = hei
        print(f"Прмямоугольник: {self.wid}, высота {self.hei}")



rac = Rac()
rac.des(5, 5)
rac.area()
rac.per()