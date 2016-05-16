COLORS = {
    'blue': 'ab1909',
    'red': 'c9c9c9',
}


class Food(object):
    def __init__(self, color):
        self.color = COLORS[color.lower()]

    @classmethod
    def create_instances(cls, color, instances):
        pieces = []
        for i  in range(instances):
            pieces.append(cls(color))
        return pieces


class Cookie(Food):
    def __init__(self, color, number_of_buttons=3):
        super(Cookie, self).__init__(color)
        self.number_of_buttons = number_of_buttons


class Apple(Food):
    pass


cookies = Cookie.create_instances("blue", instances=2)
apples = Apple.create_instances("blue", instances=3)

print(cookies)
print(apples)


"""
c = Cookie(color="Blue", number_of_buttons=2)
print("Cookie's color: {}".format(c.color))

a = Apple(color="Red")
print("Apple's color: {}".format(a.color))
"""