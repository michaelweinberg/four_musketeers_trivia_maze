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

    def move_west(self):
        self.set_x(self.__x - 1)

    def move_east(self):
        self.set_x(self.__x + 1)

    def move_north(self):
        self.set_y(self.__y - 1)

    def move_south(self):
        self.set_y(self.__y + 1)

    def __str__(self):
        print("player" + str(self.__y), str(self.__x))