class Calculator(object):
    """
    Arithmetic calculation for two numbers
    """

    def __init__(self, a, b):
        """

        :param a:
        :param b:
        """
        self._a = a
        self._b = b

    def add(self):
        """
        Method add 2 numbers
        :return: result
        """
        return self._a + self._b

    def div(self):
        """

        :return: result
        """
        result = None
        try:
            result = self._a / float(self._b)
        except ZeroDivisionError as e:
            print(e)
        return result

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

operation = Calculator(33,5)
print(operation.add())
print(operation.div())
operation.a = 5
operation.b = 22
print(operation.add())
