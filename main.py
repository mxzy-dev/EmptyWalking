import random as r
import graph as g
import os
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def Show(Graph):
    print("\n".join(" ".join(map(str, row)) for row in Graph))
def Inp():
    Key = open("key.txt","w")
    CurKey = input()
    Key.write(CurKey)
    Key.close()
    return Key
def Log(Graph):
    Logy = open("logy.txt","r")
    Logz = open("logz.txt","r")
    Key = open("key.txt", "r")
    y = int(Logy.read())
    z = int(Logz.read())
    Pos = [y,z]
    Graph[Pos[0]][Pos[1]] = g.E
    Pos = Move(Pos,Key.read())
    Logy = open("logy.txt","w")
    Logz = open("logz.txt","w")
    Logy.write(str(Pos[0]))
    Logz.write(str(Pos[1]))
    Logy.close()
    Logz.close()
    return Pos
def Info(Pos):
    print("Position: ",(Pos[0] -  17),"-",(Pos[1] - 11))
    fps = 16
    print(fps)
    print("info-completed")
def Move(Pos, Key):
    if Key.lower() == "w":
        Pos[0] = Pos[0] - 1
    elif Key.lower() == "a":
        Pos[1] = Pos[1] - 1
    elif Key.lower() == "s":
        Pos[0] = Pos[0] + 1
    elif Key.lower() == "d":
        Pos[1] = Pos[1] + 1
    return Pos
def Frame(Graph):
    Pos = Log(Graph)
    Graph[Pos[0]][Pos[1]] = g.L
    Show(Graph)
    Info(Pos)
    Key = Inp()
def Fps():
    while True:
        Graph = g.Pad
        Frame(Graph)
        Clear()
with open("logy.txt","w") as Logy:
    Logy.write(str(r.randint(5,30)))
with open("logz.txt","w") as Logz:
    Logz.write(str(r.randint(5,20)))
Fps()