class Rectangle():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return  "Rectangle: width={width} height={height}" \
                " Area={area}, square={square}" \
            .format(width = self.width,
                    height= self.height,
                    area = self.get_area(),
                    square = self.is_square())
    
    def get_area(self):
        return self.width * self.height
    
    def is_square(self):
        return self.width == self.height
        
if __name__ == '__main__':
    r1 = Rectangle(width = 4, height = 6)
    r2 = Rectangle(width = 2, height = 2)

    print(r1)
    print(r2)


