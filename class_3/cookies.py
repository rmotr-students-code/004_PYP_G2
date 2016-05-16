



class Cookie(object):
    DEFAULT_COLOR = 'red'
    
    def __init__(self, b1=None, b2=None):
        if b1 is None:
            b1 = Cookie.DEFAULT_COLOR
        if b2 is None:
            b2 = Cookie.DEFAULT_COLOR

        self.button1 = b1
        self.button2 = b2

    def randomize_second_button(self):
        self.button2 = 'yellow'

    @classmethod
    def build_me_some_instances(cls, number_of_instances):
        cookies = []
        for i in range(number_of_instances):
            # new_instance = Cookie()
            # cookies.append(new_instance)

            new_instance = cls()
            cookies.append(new_instance)
        return cookies


# User:


cookies = Cookie.build_me_some_instances(number_of_instances=5)
print("C1, button1: {}".format(cookies[0].button1))




"""


class CookieFactory(object):
    def __init__(self, number_of_instances):
        self.number_of_instances = number_of_instances

    def build(self):
        cookies = []
        for i in range(self.number_of_instances):
            cookies.append(Cookie())
        return cookies


### User :

c1 = Cookie()
print("C1 button2 is: {}".format(c1.button2))

Cookie.DEFAULT_COLOR = 'yellow'

c2 = Cookie()
print("C2 button2 is: {}".format(c2.button2))

"""


# c2 = Cookie('red', 'blue')  # button2 == 'blue'
# print("C2 button2 is: {}".format(c2.button2))
# print("Cookie ID {} button2 is: {}".format(c2.cookie_id, c2.button2))


# c2.randomize_second_button()
# print("C1 button2 is: {}".format(c1.button2))
# print("C2 button2 is: {}".format(c2.button2))

