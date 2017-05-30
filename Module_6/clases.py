class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduse(self):
        return 'sefef'


class Employe(Human):
    def introduse(self):
        super().introduse()
        return 'f3f3!!!'


if __name__ == '__main__':
    hu1 = Human('eefe', 25)
    hu2 = Employe('rf4f!!!!', 22)

    print(hu1.introduse())
    print(hu2.introduse())

