from tkinter import Tk, BOTH, Canvas


class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    

    def draw(self, canvas, color="black"):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill = color, width=2)


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "The Big Show"
        self.__canvas = Canvas(self.__root, bg = "White", height= height, width=width)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__canvas.update_idletasks()
        self.__canvas.update()
        
    def wait_for_close(self):
        self.__running = True

        while self.__running == True:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)


class Cell():
    def __init__(self,  window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = window
        self.visited = False

    def draw(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y, color="black"):
        if self.__win == None:
            return
        
        self.__x1 = top_left_x
        self.__y1 = top_left_y
        self.__x2 = bottom_right_x
        self.__y2 = bottom_right_y

        left_line = Line(Point(self.__x1, self.__y1),Point(self.__x1, self.__y2))
        right_line = Line(Point(self.__x2, self.__y1),Point(self.__x2, self.__y2))
        top_line = Line(Point(self.__x1, self.__y1),Point(self.__x2, self.__y1))
        bottom_line = Line(Point(self.__x1, self.__y2),Point(self.__x2, self.__y2))

        if self.has_left_wall == True:
            self.__win.draw_line(left_line,color)
        else:
            self.__win.draw_line(left_line,"white")
        if self.has_right_wall == True:
            self.__win.draw_line(right_line,color)
        else:
            self.__win.draw_line(right_line, "white")
        if self.has_top_wall == True:
            self.__win.draw_line(top_line,color)
        else:
            #print("HERE")
            self.__win.draw_line(top_line, "white")
        if self.has_bottom_wall == True:
            self.__win.draw_line(bottom_line,color)
        else:
            self.__win.draw_line(bottom_line, "white")

    def draw_move(self, to_cell,undo=False):
        if self.__win == None:
            return
        center = self.get_center()
        other_center = to_cell.get_center()
        center_line = Line(center, other_center)
        color = "red" if undo == False else "gray"
        self.__win.draw_line(center_line,color)

    def get_center(self):
        return Point(self.__x1 + (abs(self.__x2 - self.__x1) // 2), self.__y1 + (abs(self.__y2 - self.__y1) // 2))