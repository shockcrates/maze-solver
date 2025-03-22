from Window import Point, Line, Cell, Window
import time
import random



class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, Seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self._create_cells()
        random.seed(Seed)

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
        #print( i + j)
        x = self.__x1 + self.__cell_size_x * i
        #print("x: " + str(x))
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
    
    def _break_walls_r(self, i, j):
        #print(f"i: {i}, j: {j}")
        self._cells[i][j].visited = True
        while(True):
            to_visit = []
            #check which neighbors need to be visited and add to list
            if i > 0: 
                if self._cells[i-1][j].visited == False:
                    to_visit.append((i-1,j))
            if i < self.__num_cols - 1:
                if self._cells[i+1][j].visited == False:
                    to_visit.append((i+1,j))
            if j > 0:
                if self._cells[i][j-1].visited == False:
                    to_visit.append((i,j-1))
            if j < self.__num_rows - 1:
                if self._cells[i][j+1].visited == False:
                    to_visit.append((i,j + 1))
            
            if not to_visit:
                self._draw_cell(i, j)
                #print("RETURNING")
                return

            direction_index = random.randint(0, 1000)  % len(to_visit)
            direction = to_visit[direction_index]
            next_cell = self._cells[direction[0]][direction[1]]

            #print(f"CURRENT CELL: {i}, {j} ..... NEXT CELL: {direction[0]}, {direction[1]}")

            if i < direction[0]:
                #print("Going right")
                self._cells[i][j].has_right_wall = False
                self._draw_cell(i,j)
                next_cell.has_left_wall = False
                self._draw_cell(direction[0],direction[1])
            if i > direction[0]:
                #print("Going left")
                self._cells[i][j].has_left_wall = False
                self._draw_cell(i,j)
                next_cell.has_right_wall = False
                self._draw_cell(direction[0],direction[1])
            if j < direction[1]:
                #print("Going down")
                self._cells[i][j].has_bottom_wall = False
                self._draw_cell(i,j)
                next_cell.has_top_wall = False
                self._draw_cell(direction[0],direction[1])
            if j > direction[1]:
                #print("Going up")
                self._cells[i][j].has_top_wall = False
                self._draw_cell(i,j)
                next_cell.has_bottom_wall = False
                self._draw_cell(direction[0],direction[1])
            
            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        solved = self._solve_r(0,0)
        if solved:
            return True
        else:
            return False
        
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.__num_cols -1 and j == self.__num_rows - 1:
            return True
        
        if i > 0:
            if self._cells[i][j].has_left_wall == False and self._cells[i-1][j].visited == False:
                self._cells[i][j].draw_move(self._cells[i-1][j],False)
                solved = self._solve_r(i-1, j)
                if solved:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i-1][j], True)
        if i < self.__num_cols - 1:
            if self._cells[i][j].has_right_wall == False and self._cells[i + 1][j].visited == False:
                self._cells[i][j].draw_move(self._cells[i+1][j],False)
                solved = self._solve_r(i+1, j)
                if solved:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i+1][j], True)
        if j > 0:
            if self._cells[i][j].has_top_wall == False and self._cells[i][j-1].visited == False:
                self._cells[i][j].draw_move(self._cells[i][j-1],False)
                solved = self._solve_r(i, j-1)
                if solved:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j-1], True)
        if j < self.__num_rows - 1:
            if self._cells[i][j].has_bottom_wall == False and self._cells[i][j + 1].visited == False:
                self._cells[i][j].draw_move(self._cells[i][j + 1],False)
                solved = self._solve_r(i, j + 1)
                if solved:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        return False