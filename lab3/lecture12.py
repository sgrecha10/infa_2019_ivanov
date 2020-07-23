# author: Grechnev Sergey
"""Module for test

"""


class FirstClass:
    def __init__(self, age, name):
        self.__age = age
        self.name = name
        assert type(age) == str, "Переменная равна строке"

    def __str__(self):
        return f"IPAddress: {self.name}"

    def modyfy(self):
        self.__age += 5

    def show(self):
        print(self.name, self.__age, end=" ")


class SecondClass(FirstClass):
    def __init__(self, age, name, height):
        super().__init__(age, name)
        # self.height = int(input("Введите рост:\n"))
        self.height = height

    def show(self):
        super().show()
        print("А ты высокий! - ", self.height)


ob = SecondClass(12, "sergey", 186)
# FirstClass.show(ob)
ob.modyfy()
# ob.input_height()
# ob.__age = 107
ob.show()
# print(dir(ob), sep='\n')
# print('\n'.join(dir(ob)))
# print(ob._FirstClass__age)