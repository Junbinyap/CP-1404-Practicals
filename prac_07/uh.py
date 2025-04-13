class Monitor:
    def __init__(self, model="", width=0, height=0):
        self.model = model
        self.width = width
        self.height= height

    def get_resolution(self):
        return self.width, self.height

    def get_total_pixel(self):
        return self.width * self.height

    def __eql__(self, other):
        return self.width == other.width and self.height == other.height


resolution = Monitor("marcus",4, 5)
solved = resolution.get_resolution()
r2 = resolution.get_total_pixel()
print(solved)
print(r2)