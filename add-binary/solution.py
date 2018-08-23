class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = [i == '1' for i in a[::-1]]
        y = [i == '1' for i in b[::-1]]
        r = []
        carry = False

        if len(x) > len(y):
            y += [False] * (len(x) - len(y))
        else:
            x += [False] * (len(y) - len(x))

        for d in range(len(x)):
            s, carry = self.full_adder(x[d], y[d], carry)
            r += [s]
        if carry:
            r += [True]

        r.reverse()
        return ''.join(['1' if i else '0' for i in r])

    def half_adder(self, a, b):
        return a ^ b, a & b

    def full_adder(self, a, b, cin):
        s1, c1 = self.half_adder(a, b)
        s2, c2 = self.half_adder(s1, cin)
        return s2, c1 | c2
