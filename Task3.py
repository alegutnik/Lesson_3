class Temperature:
    def __init__(self, cel=0):
        self._cel = cel

    @property
    def cel(self):
        print("Градусов Цельсия:")
        return self._cel

    @cel.setter
    def cel(self, value):
        self._cel = value

    @property
    def far(self):
        print("Градусов Фаренгейт:")
        return (self._cel * 9 / 5) + 32

    @far.setter
    def far(self, value):
        self._cel = (value - 32) * 5 / 9



temp = Temperature()
temp.cel = 5
print(temp.cel)
print(temp.far)

print("=" * 10)

temp.far = 5
print(temp.cel)
print(temp.far)