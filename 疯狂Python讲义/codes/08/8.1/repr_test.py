class Apple:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def __repr__(self):
        return 'Appple[color=' + self.color + ',weight=' + str(self.weight) + ']'


a = Apple('红色', 5.68)
print(a)
