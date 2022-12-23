import OpenGL
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-500,500.0,-500,500.0)

def plotaxes():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(0,-500)
    glVertex2f(0,500)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(500,0)
    glVertex2f(-500,0)
    glEnd()

def plotgrid():
    glColor3f(0.202, 0.202, 0.202)
    for i in range(-500,500,50):
        if i != 0:
            glBegin(GL_LINES)
            glVertex2f(i,500)
            glVertex2f(i,-500)
            glEnd()
            glBegin(GL_LINES)
            glVertex2f(500,i)
            glVertex2f(-500,i)
            glEnd()
        
def plotTraingle(x1,x2,x3,y1,y2,y3):
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x3,y3)
    glVertex2f(x1,y1)
    glEnd()

print("\nEnter co-ordinates of triangle :")
x1=float(input("\n\tX1: "))
y1=float(input("\n\tY1: "))
x2=float(input("\n\tX2: "))
y2=float(input("\n\tY2: "))
x3=float(input("\n\tX3: "))
y3=float(input("\n\tY3: "))

points = [[x1,y1],[x2,y2],[x3,y3]]

while 1 :
    print("\nChoose Transformations:\n\t1.Translation\n\t2.Rotation\n\t3.Scale\n\t4.Reflection\n\t5.EXIT")
    choice=int(input("\nYour Choice: "))
    
    if choice == 1:
        tx=int(input("\nX translation: "))
        ty=int(input("\nY translation: "))
        nlist = []
        nlist.append(points[len(points)-3])
        nlist.append(points[len(points)-2])
        nlist.append(points[len(points)-1])
        for point in nlist:
            points.append([point[0]+tx,point[1]+ty])
    
    elif choice == 2:
        nlist = []
        nlist.append(points[len(points)-3])
        nlist.append(points[len(points)-2])
        nlist.append(points[len(points)-1])
        theta= (math.pi/180) * int(input("\nEnter Degress to be rotated: "))
        for point in nlist:
            points.append([round(point[0]* math.cos(theta) - point[1] * math.sin(theta)), round(point[0] * math.sin(theta) + point[1] * math.cos(theta))])
    
    elif choice == 3:
        nlist = []
        nlist.append(points[len(points)-3])
        nlist.append(points[len(points)-2])
        nlist.append(points[len(points)-1])   
        tx= int(input("\nEnter Scale along x: "))
        ty= int(input("\nEnter Scale along y: "))
        for point in nlist:
            points.append([point[0]*tx,point[1]*ty])

    elif choice == 4:
        nlist = []
        nlist.append(points[len(points)-3])
        nlist.append(points[len(points)-2])
        nlist.append(points[len(points)-1])
        print("Enter the type of reflection : ")
        ch = int(input("1. Reflection about x axis\n2. Reflection about y axis\n3. Reflection about origin\n4. Reflection about x=y line\n5. Reflection about x=-y line\n"))
        for point in nlist:
            if(ch==1):
                points.append([point[0], -point[1]])
            elif(ch==2):
                points.append([-point[0], point[1]])
            elif(ch==3):
                points.append([-point[0], -point[1]])
            elif(ch==4):
                points.append([point[1], point[0]])
            elif(ch==5):
                points.append([-point[1], -point[0]])
    
    elif choice == 5:
        break
    
    else :
        print("Enter a valid choice :") 

def draw(points):
    plotaxes()
    plotgrid()
    glColor3f(1, 1, 0)
    plotTraingle(points[0][0],points[1][0],points[2][0],points[0][1],points[1][1],points[2][1])
    glColor3f(1, 0, 0)
    ran = int(len(points)/3)
    for r in range(1,ran) :
        if r==ran-1 :
            glColor3f(1,0,1)
        plotTraingle(points[3*r][0],points[3*r + 1][0],points[3*r + 2][0],points[3*r + 0][1],points[3*r + 1][1],points[3*r + 2][1])
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500)
glutInitWindowPosition(50,50)
glutCreateWindow("Adarsh Anand (21MC3025) Question 2")
glutDisplayFunc(lambda: draw(points))
glutIdleFunc(lambda: draw(points))
init()
glutMainLoop()