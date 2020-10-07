from graphics import *

def main():
  win = GraphWin("Glenn's Window", 500, 500)
 
  c = Circle(Point(50,50), 10)
  c.draw(win)

  win.getMouse()  
  win.close()

main()
