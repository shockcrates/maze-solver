from Window import *
from maze import *

def main():
    win = Window(800,800)

    point1 = Point(100, 100)
    point2 = Point(150, 100)
    point3 = Point(700, 700)
    point4 = Point(100, 700)

    Line1 = Line(point1, point2)
    Line2 = Line(point2, point3)
    Line3 = Line(point3, point4)
    Line4 = Line(point4, point1)

    #win.draw_line(Line1, "black")
    #win.draw_line(Line2, "black")
    #win.draw_line(Line3, "black")
    #win.draw_line(Line4, "black")

    """ cell1 = Cell(300, 300, 400 , 400, win)
    cell1.has_top_wall = False
    cell1.has_left_wall = False
    cell2 = Cell(300,200,400,300, win)
    cell2.has_bottom_wall = False
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2, False)
    cell3 = Cell(200,300,300,400,win)
    cell3.has_right_wall = False
    cell3.draw()
    cell1.draw_move(cell3,True) """
    
    Mazeee = Maze(100,100, 12, 12, 50, 50, win)
    Mazeee._break_entrance_and_exit()
    #win.draw_line(Line1, "red")
    Mazeee._break_walls_r(0,0)
    Mazeee._reset_cells_visited()
    Mazeee.solve()


    win.wait_for_close()

main()