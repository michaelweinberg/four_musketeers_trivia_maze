class Player:
    def __init__(self, y=0, x=0):
        self.__name = ""
        self.__x = x
        self.__y = y
        self.__is_dead = False

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def die(self):
        print("Our hero has died")