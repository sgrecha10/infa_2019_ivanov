class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        #attrs = self.__dict__
        #return attrs
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())


class Person(AttrDisplay):
    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay + self.pay * percent)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus= .10):
        Person.giveRaise(self, percent + bonus)


class Manager2:
    def __init__(self, name, pay):
        self.name = name
        self.p = Person(name, 'mgr', pay)

    def giveRaise(self, percent=.5):
        self.p.giveRaise(percent)

    def __repr__(self):
        return str(self.p)



#grecha = Person('Sergey Grechnev', 'dev', 100000)
#anna = Manager('Anna Chernysheva', 100000)
#vasy = Manager2('Vasy Pupkin', 100000)

#print(grecha)
#print(anna)
#print(vasy)





if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    x, y = TopTest(), SubTest()
    z = SubTest()
    #print(x)
    #print(y)
    #print(z)



