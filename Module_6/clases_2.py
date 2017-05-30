class Tomato():
    color = ""
    weight = 0
    name = ""

    def changecolor(self, newcolor):
        self.color = newcolor

    def isweight(self, newweight):
        self.weight = newweight

    def isname(self, newname):
        self.name = newname


print(Tomato.name)

tomato_chery = Tomato()

tomato_chery.isname('Chery')
tomato_chery.changecolor('red')
tomato_chery.isweight(20)
print(tomato_chery.name, tomato_chery.color, tomato_chery.weight)


class BigTomato(Tomato):
    # super.name = name

    pass



tomato_two = BigTomato()

tomato_two.isname('Blue_yeart')
tomato_tree = BigTomato()
tomato_tree.isname("New sort")

print(tomato_two.name)
print(tomato_tree.name)
