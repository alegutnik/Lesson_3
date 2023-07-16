class English:
    @staticmethod
    def greeting():
        print("Hello")


class Spain:
    @staticmethod
    def greeting():
        print("Hola")


def hello_friend():
    english = English
    spain = Spain
    english.greeting()
    spain.greeting()


hello_friend()
