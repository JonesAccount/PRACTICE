d = {"num1": 4, "num2": 2, "num3": 1, "num4": 5, "num5": 3}
l = []

class Edit:

    def init(self, d, l):
        
        for k, v in d.items():
            print(f"{k}: {v}", end="|")
        print()
            
        for i in d.values():
            l.append(i)
        l.sort()
        print(l)
        
        for i in range(len(l)):
            d["num" + str(i + 1)] = l[i]
        
        print()
        for k, v in d.items():
            print(f"{k}: {v}", end="|")
        print()
        
edit = Edit(d, l)