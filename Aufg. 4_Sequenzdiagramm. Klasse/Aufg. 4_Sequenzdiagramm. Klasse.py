# Aufg. 4_Sequenzdiagramm. Klasse.

class A:
    def __init__(self, b):
        self.b = b

    def methode1(self, value):
        if value == 0:
            self.b.methode1()

        elif value == 1:
            self.b.methode2()

        else:
            self.methode2()

    def methode2(self):
        print("A: methode2")


class B:
    def __init__(self, c):
        self.c = c

    def methode1(self):
        print("B: methode1")

    def methode2(self):
        print("B: methode2")
        self.c.methode1()


class C:
    def methode1(self):
        print("C: methode1")

# Test
c = C()
b = B(c)
a = A(b)

a.methode1(0)
a.methode1(1)
a.methode1(2)