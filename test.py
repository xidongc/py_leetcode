class Sol(object):

    def test(self):

        t = {}
        t.setdefault(1, (0,1,2))
        return t.get(1)

s = Sol()
print(s.test())




