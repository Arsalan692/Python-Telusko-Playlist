

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            var1 = self.num
            self.num += 1
            return var1
        else:
            quit()



some = TopTen()
for i in some:
    print(i)
