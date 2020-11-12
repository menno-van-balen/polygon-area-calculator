class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        # Rectangle(width=10, height=3)
        return "Rectangle(width=" + str(self.width) + ", height="\
            + str(self.height) + ")"

    def set_width(self, width):
        if self.__class__ is Rectangle:
            self.width = width
        elif self.__class__ is Square:
            self.side = width
            self.width = width
            self.height = width

    def set_height(self, height):
        if self.__class__ is Rectangle:
            self.height = height
        elif self.__class__ is Square:
            self.side = height
            self.width = height
            self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        result = str()
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                result += self.width * "*" + "\n"
            result = result.rstrip("\n")
            return result

    def get_amount_inside(self, rect):
        w_times, h_times, total_times = int(), int(), int()
        w_times = self.width // rect.width
        h_times = self.height // rect.height
        total_times = w_times * h_times
        return total_times


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side=" + str(self.side) + ")"

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side


# rect = Rectangle(55, 5)
# rect.set_width(3)
# rect2 = Rectangle(1, 3)
# print("area:", rect.get_area())
# print("peri:", rect.get_perimeter())
# print("diag:", rect.get_diagonal())
# print("rect:", rect)
# print(rect.get_picture())
# print("fits:", rect.get_amount_inside(rect2))

# sq = Square(9)
# print("area:", sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# sq.set_width(2)
# print(sq)
# print(sq.get_picture())
