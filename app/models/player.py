class Player:
    def __init__(self, y=1, x=1):
        self.__name = ""
        self.__x = x
        self.__y = y
        self.__score = 0
        # self.__is_dead = False

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score += score

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    # def die(self):
    #     print("Our hero has died")

    def move(self, y, x):
        self.set_x(x)
        self.set_y(y)

    # def move_east(self):
    #     self.set_x(self.__x + 1)
    #
    # def move_north(self):
    #     self.set_y(self.__y - 1)
    #
    # def move_south(self):
    #     self.set_y(self.__y + 1)
    def generate_player(self, name):
        self.set_name(name)
        self.set_x(1)
        self.set_y(1)

    def __str__(self):
        print("player:" + self.__name + "\nscore:" + str(self.__score) + "\nx,y:" + str(self.__x) + str(self.__y))
