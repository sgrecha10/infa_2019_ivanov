#import mypkg.mymod
#mypkg.mymod.test('gun.py')
#from mypkg.mymod import *
#test('gun.py')


class Testclass:
    def __init__(self, x):
        self.x = x

    def dysplay(self):
        print(self.x, self.y)


a = Testclass('grecha')
a.y = 'anna'
a.dysplay()

