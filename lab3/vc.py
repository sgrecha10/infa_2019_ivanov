z = 0

def permute1(seq):
    global z
    z += 1
    if not seq:
        print('a) z: %s, IF RETURN' % z)
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]

            print('b) z: %s, i: %i, rest: %s' % (z, i, rest))

            for x in permute1(rest):
                n = seq[i:i+1] + x
                print('c) z: %s, i: %i, n: %s, x: %s' % (z, i, n, x))
                res.append(n)
                print('d) ', n)
                
    return res

print(permute1('a'))
