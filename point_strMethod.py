class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        added_x = self.x + other.x
        added_y = self.y + other.y
        combined = Point(added_x, added_y)
        return combined


p1 = Point(14, 31)

print("Your points are currently " + str(p1) + "\n")

ps = int((raw_input("What do you want to add to the first point?\n")))

pt = int((raw_input("What do you want to add to the second point?\n")))

p2 = Point(ps, pt)


print p1 + p2
print("Above are your new points")

