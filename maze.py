from Window import Point, Line, Cell, Window
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.__num_cols):
            curr_col = []
            for j in range(self.__num_rows):
                curr = Cell(self.__win)
                curr_col.append(curr)
            self._cells.append(curr_col)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        if self.__win == None:
            return
        print( i + j)
        x = self.__x1 + self.__cell_size_x * i
        print("x: " + str(x))
        x2 = x + self.__cell_size_x
        y = self.__y1 + self.__cell_size_y * j
        y2 = y + self.__cell_size_y
        self._cells[i][j].draw(x, y, x2, y2)
        self._animate()

    def _animate(self):
        if self.__win == None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_left = self._cells[0][0]
        top_left.has_top_wall = False
        self._draw_cell(0,0)

        bottom_right = self._cells[self.__num_cols -1][self.__num_rows - 1]
        bottom_right.has_bottom_wall = False
        self._draw_cell(self.__num_cols - 1, self.__num_rows - 1)