def countLines(name):
    file = open(name, encoding='utf8')
    return len(file.readlines())


def countLines2(name):
     return sum([1 for _ in open(name, encoding='utf8')])


def countChars(name):
    file = open(name, encoding='utf8')
    return len(file.read())


def test(name):
    print('name: %s, countLines: %i, countChars: %i' % (name, countLines(name), countChars(name)))

# print(x)

if __name__ == '__main__':
    test('mymod.py')
