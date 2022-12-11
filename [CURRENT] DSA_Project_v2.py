# BY Ali Nisar AND Anas

from tkinter import *


G= {'Habib University': [('airport', 7.9), ('airport', 8.0), ('Balochistan Sajji', 2.7), ('Balochistan Sajji', 2.8), ('millenium mall', 3.7)], 'airport': [('Habib University', 7.9), ('Habib University', 8.0), ('Balochistan Sajji', 10.6), ('millenium mall', 2.3), ('millenium mall', 2.9), ('millenium mall', 3.5)], 'Balochistan Sajji': [('Habib University', 2.7), ('Habib University', 2.8), ('airport', 10.6), ('millenium mall', 1.8), ('National Stadium', 5.9), ('National Stadium', 6.5), ('National Stadium', 7.1)], 'millenium mall': [('Habib University', 6.6), ('airport', 5.3), ('airport', 5.0), ('Balochistan Sajji', 1.8),('National Stadium', 4.0)], 'National Stadium': [('Balochistan Sajji', 5.9), ('Balochistan Sajji', 5.6),('millenium mall', 4.0)],'shadi hall':[('millenium mall',2.5)]}
#graph contains all the routes and alternate routes

inp = 0
inp_2 = 0
shorted_path_cost = 0

input_root = Tk()
input_root.geometry("1280x720") # display size
input_root.title("DSA Project - Input tKinter")

canvas = Canvas(input_root, width=1280, height=720, bg="white")
canvas.place(x=0,y=0)


def action1(arg):
    global inp
    inp = arg
    print("Origin selected: ", inp)

def action2(arg):
    global inp_2
    inp_2 = arg
    print("Destination selected: ", inp_2)


def inputAction1():
    HU_button = Button(input_root, text="Habib University", command=lambda: action1("Habib University"))
    airport_button = Button(input_root, text="Jinnah Int. Airport", command=lambda: action1("airport"))
    milleniumMall_button = Button(input_root, text="Millennium Mall", command=lambda: action1("millenium mall"))
    balochistanSajji_button = Button(input_root, text="Balochistan Sajji", command=lambda: action1("Balochistan Sajji"))
    nationalStadium_button = Button(input_root, text="National Stadium", command=lambda: action1("National Stadium"))

    HU_button.place(x=220, y=180)
    airport_button.place(x=25, y=280)
    milleniumMall_button.place(x=450, y=180)
    balochistanSajji_button.place(x=220, y=85)
    nationalStadium_button.place(x=350, y=15)


    canvas.create_line(315,185,450,185, fill="grey", width=2.5) # HU to mMall - MAIN_PATH
    canvas.create_line(445,180,450,185, fill="black", width=2.5) # HU to mMall - arrow_side1
    canvas.create_line(445,190,450,185, fill="black", width=2.5) # HU to mMall - arrow_side2

    canvas.create_line(315,200,450,200, fill="grey", width=2.5) # mMall to HU - MAIN PATH
    canvas.create_line(319,200,324,195, fill="black", width=2.5) # mMall to HU - arrow_side1
    canvas.create_line(319,200,324,205, fill="black", width=2.5) # mMall to HU - arrow_side2



    canvas.create_line(128,285,450,185, fill="grey", width=2.5) # airport to mMall - MAIN_PATH
    canvas.create_line(450,180,450,185, fill="black", width=2.5) # airport to mMall - arrow_side1
    canvas.create_line(450,190,450,185, fill="black", width=2.5) # airport to mMall - arrow_side2

    canvas.create_line(128,300,450,200, fill="grey", width=2.5) # mMall to airport - MAIN_PATH
    canvas.create_line(130,300,135,295, fill="black", width=2.5) # mMall to airport - arrow_side1
    canvas.create_line(130,300,135,305, fill="black", width=2.5) # mMall to airport - arrow_side2



    canvas.create_line(220,185,128,285, fill="grey", width=2.5) # HU to airport - MAIN_PATH
    canvas.create_line(130,285,130,278, fill="black", width=2.5) # HU to airport - arrow_side1
    canvas.create_line(130,285,137,282, fill="black", width=2.5) # HU to airport - arrow_side2



    canvas.create_line(260,180,260,110, fill="grey", width=2.5) # HU to B - MAIN_PATH
    canvas.create_line(255,115,260,110, fill="black", width=2.5) # HU to B - arrow_side1
    canvas.create_line(265,115,260,110, fill="black", width=2.5) # HU to B - arrow_side2

    canvas.create_line(280,110,280,180, fill="grey", width=2.5) # B to HU - MAIN_PATH
    canvas.create_line(275,173,280,178, fill="black", width=2.5) # B to HU - arrow_side1
    canvas.create_line(285,173,280,178, fill="black", width=2.5) # B to HU - arrow_side2



    canvas.create_line(65,280,220,92, fill="grey", width=2.5) # airport to B - MAIN_PATH
    canvas.create_line(215,92,220,92, fill="black", width=2.5) # airport to B - arrow_side1
    canvas.create_line(215,100,220,92, fill="black", width=2.5) # airport to B - arrow_side2

    canvas.create_line(220,105,80,280, fill="grey", width=2.5) # B to airport - MAIN_PATH
    canvas.create_line(80,270,80,278, fill="black", width=2.5) # B to airport - arrow_side1
    canvas.create_line(80,278,87,278, fill="black", width=2.5) # B to airport - arrow_side2



    canvas.create_line(260,85,350,25, fill="grey", width=2.5) # B to NS - MAIN_PATH
    canvas.create_line(342,25,348,25, fill="black", width=2.5) # B to NS - arrow_side1
    canvas.create_line(348,35,348,25, fill="black", width=2.5) # B to NS - arrow_side2


    canvas.create_line(350,35,280,85, fill="grey", width=2.5) # NS to B - MAIN_PATH
    canvas.create_line(280,84,280,77, fill="black", width=2.5) # NS to B - arrow_side1
    canvas.create_line(280,84,287,84, fill="black", width=2.5) # NS to B - arrow_side2



    canvas.create_line(485,180,375,25, fill="grey", width=2.5) # M to NS - MAIN_PATH
    canvas.create_line(385,40,385,50, fill="black", width=2.5) # M to NS - arrow_side1
    canvas.create_line(385,40,400,45, fill="black", width=2.5) # M to NS - arrow_side2


    canvas.create_line(510,180,400,25, fill="grey", width=2.5) # NS to M - MAIN_PATH
    canvas.create_line(507,178,503,173, fill="black", width=2.5) # NS to M - arrow_side1
    canvas.create_line(507,178,515,173, fill="black", width=2.5) # NS to M - arrow_side2



    canvas.create_line(485,180,315,100, fill="grey", width=2.5) # B to M - MAIN_PATH
    canvas.create_line(478,180,485,180, fill="black", width=2.5) # B to M - arrow_side1
    canvas.create_line(485,173,485,180, fill="black", width=2.5) # B to M - arrow_side2


    canvas.create_line(510,180,315,90, fill="grey", width=2.5) # M to B - MATH_PATH
    canvas.create_line(317,90,327,90, fill="black", width=2.5) # M to B - arrow_side1
    canvas.create_line(317,90,317,100, fill="black", width=2.5) # M to B - arrow_side2


def inputAction2():
    HU_button = Button(input_root, text="Habib University", command=lambda: action2("Habib University"))
    airport_button = Button(input_root, text="Jinnah Int. Airport", command=lambda: action2("airport"))
    milleniumMall_button = Button(input_root, text="Millennium Mall", command=lambda: action2("millenium mall"))
    balochistanSajji_button = Button(input_root, text="Balochistan Sajji", command=lambda: action2("Balochistan Sajji"))
    nationalStadium_button = Button(input_root, text="National Stadium", command=lambda: action2("National Stadium"))
    
    HU_button.place(x=220, y=180)
    airport_button.place(x=25, y=280)
    milleniumMall_button.place(x=450, y=180)
    balochistanSajji_button.place(x=220, y=85)
    nationalStadium_button.place(x=350, y=15)


    canvas.create_line(315,185,450,185, fill="grey", width=2.5) # HU to mMall - MAIN_PATH
    canvas.create_line(445,180,450,185, fill="black", width=2.5) # HU to mMall - arrow_side1
    canvas.create_line(445,190,450,185, fill="black", width=2.5) # HU to mMall - arrow_side2

    canvas.create_line(315,200,450,200, fill="grey", width=2.5) # mMall to HU - MAIN PATH
    canvas.create_line(319,200,324,195, fill="black", width=2.5) # mMall to HU - arrow_side1
    canvas.create_line(319,200,324,205, fill="black", width=2.5) # mMall to HU - arrow_side2



    canvas.create_line(128,285,450,185, fill="grey", width=2.5) # airport to mMall - MAIN_PATH
    canvas.create_line(450,180,450,185, fill="black", width=2.5) # airport to mMall - arrow_side1
    canvas.create_line(450,190,450,185, fill="black", width=2.5) # airport to mMall - arrow_side2

    canvas.create_line(128,300,450,200, fill="grey", width=2.5) # mMall to airport - MAIN_PATH
    canvas.create_line(130,300,135,295, fill="black", width=2.5) # mMall to airport - arrow_side1
    canvas.create_line(130,300,135,305, fill="black", width=2.5) # mMall to airport - arrow_side2



    canvas.create_line(220,185,128,285, fill="grey", width=2.5) # HU to airport - MAIN_PATH
    canvas.create_line(130,285,130,278, fill="black", width=2.5) # HU to airport - arrow_side1
    canvas.create_line(130,285,137,282, fill="black", width=2.5) # HU to airport - arrow_side2



    canvas.create_line(260,180,260,110, fill="grey", width=2.5) # HU to B - MAIN_PATH
    canvas.create_line(255,115,260,110, fill="black", width=2.5) # HU to B - arrow_side1
    canvas.create_line(265,115,260,110, fill="black", width=2.5) # HU to B - arrow_side2

    canvas.create_line(280,110,280,180, fill="grey", width=2.5) # B to HU - MAIN_PATH
    canvas.create_line(275,173,280,178, fill="black", width=2.5) # B to HU - arrow_side1
    canvas.create_line(285,173,280,178, fill="black", width=2.5) # B to HU - arrow_side2



    canvas.create_line(65,280,220,92, fill="grey", width=2.5) # airport to B - MAIN_PATH
    canvas.create_line(215,92,220,92, fill="black", width=2.5) # airport to B - arrow_side1
    canvas.create_line(215,100,220,92, fill="black", width=2.5) # airport to B - arrow_side2

    canvas.create_line(220,105,80,280, fill="grey", width=2.5) # B to airport - MAIN_PATH
    canvas.create_line(80,270,80,278, fill="black", width=2.5) # B to airport - arrow_side1
    canvas.create_line(80,278,87,278, fill="black", width=2.5) # B to airport - arrow_side2



    canvas.create_line(260,85,350,25, fill="grey", width=2.5) # B to NS - MAIN_PATH
    canvas.create_line(342,25,348,25, fill="black", width=2.5) # B to NS - arrow_side1
    canvas.create_line(348,35,348,25, fill="black", width=2.5) # B to NS - arrow_side2


    canvas.create_line(350,35,280,85, fill="grey", width=2.5) # NS to B - MAIN_PATH
    canvas.create_line(280,84,280,77, fill="black", width=2.5) # NS to B - arrow_side1
    canvas.create_line(280,84,287,84, fill="black", width=2.5) # NS to B - arrow_side2



    canvas.create_line(485,180,375,25, fill="grey", width=2.5) # M to NS - MAIN_PATH
    canvas.create_line(385,40,385,50, fill="black", width=2.5) # M to NS - arrow_side1
    canvas.create_line(385,40,400,45, fill="black", width=2.5) # M to NS - arrow_side2


    canvas.create_line(510,180,400,25, fill="grey", width=2.5) # NS to M - MAIN_PATH
    canvas.create_line(507,178,503,173, fill="black", width=2.5) # NS to M - arrow_side1
    canvas.create_line(507,178,515,173, fill="black", width=2.5) # NS to M - arrow_side2



    canvas.create_line(485,180,315,100, fill="grey", width=2.5) # B to M - MAIN_PATH
    canvas.create_line(478,180,485,180, fill="black", width=2.5) # B to M - arrow_side1
    canvas.create_line(485,173,485,180, fill="black", width=2.5) # B to M - arrow_side2


    canvas.create_line(510,180,315,90, fill="grey", width=2.5) # M to B - MATH_PATH
    canvas.create_line(317,90,327,90, fill="black", width=2.5) # M to B - arrow_side1
    canvas.create_line(317,90,317,100, fill="black", width=2.5) # M to B - arrow_side2


selectInput1_button = Button(input_root, text="Select origin", command=inputAction1)
selectInput2_button = Button(input_root, text="Select destination", command=inputAction2)
confirmButton = Button(input_root, text="Confirm", command=input_root.destroy)


selectInput1_button.place(x=650, y=350)
selectInput2_button.place(x=650, y=400)
confirmButton.place(x=800, y=350)


input_root.mainloop()

# ---------------------------------------------------------------------------------------------------------------




start=Tk()
start.geometry("1280x720")
start.title("DSA Project - Shortest Path")


canvas = Canvas(start, width=1280, height=720, bg="white")
canvas.place(x=0,y=0)

# these do nothing; they are there to keep consistency
HU_button = Button(start, text="Habib University")
airport_button = Button(start, text="Jinnah Int. Airport")
milleniumMall_button = Button(start, text="Millennium Mall")
balochistanSajji_button = Button(start, text="Balochistan Sajji")
nationalStadium_button = Button(start, text="National Stadium")


HU_button.place(x=220, y=180)
airport_button.place(x=25, y=280)
milleniumMall_button.place(x=450, y=180)
balochistanSajji_button.place(x=220, y=85)
nationalStadium_button.place(x=350, y=15)


canvas.create_line(315,185,450,185, fill="grey", width=2.5) # HU to mMall - MAIN_PATH
canvas.create_line(445,180,450,185, fill="black", width=2.5) # HU to mMall - arrow_side1
canvas.create_line(445,190,450,185, fill="black", width=2.5) # HU to mMall - arrow_side2

canvas.create_line(315,200,450,200, fill="grey", width=2.5) # mMall to HU - MAIN PATH
canvas.create_line(319,200,324,195, fill="black", width=2.5) # mMall to HU - arrow_side1
canvas.create_line(319,200,324,205, fill="black", width=2.5) # mMall to HU - arrow_side2



canvas.create_line(128,285,450,185, fill="grey", width=2.5) # airport to mMall - MAIN_PATH
canvas.create_line(450,180,450,185, fill="black", width=2.5) # airport to mMall - arrow_side1
canvas.create_line(450,190,450,185, fill="black", width=2.5) # airport to mMall - arrow_side2

canvas.create_line(128,300,450,200, fill="grey", width=2.5) # mMall to airport - MAIN_PATH
canvas.create_line(130,300,135,295, fill="black", width=2.5) # mMall to airport - arrow_side1
canvas.create_line(130,300,135,305, fill="black", width=2.5) # mMall to airport - arrow_side2



canvas.create_line(220,185,128,285, fill="grey", width=2.5) # HU to airport - MAIN_PATH
canvas.create_line(130,285,130,278, fill="black", width=2.5) # HU to airport - arrow_side1
canvas.create_line(130,285,137,282, fill="black", width=2.5) # HU to airport - arrow_side2



canvas.create_line(260,180,260,110, fill="grey", width=2.5) # HU to B - MAIN_PATH
canvas.create_line(255,115,260,110, fill="black", width=2.5) # HU to B - arrow_side1
canvas.create_line(265,115,260,110, fill="black", width=2.5) # HU to B - arrow_side2

canvas.create_line(280,110,280,180, fill="grey", width=2.5) # B to HU - MAIN_PATH
canvas.create_line(275,173,280,178, fill="black", width=2.5) # B to HU - arrow_side1
canvas.create_line(285,173,280,178, fill="black", width=2.5) # B to HU - arrow_side2



canvas.create_line(65,280,220,92, fill="grey", width=2.5) # airport to B - MAIN_PATH
canvas.create_line(215,92,220,92, fill="black", width=2.5) # airport to B - arrow_side1
canvas.create_line(215,100,220,92, fill="black", width=2.5) # airport to B - arrow_side2

canvas.create_line(220,105,80,280, fill="grey", width=2.5) # B to airport - MAIN_PATH
canvas.create_line(80,270,80,278, fill="black", width=2.5) # B to airport - arrow_side1
canvas.create_line(80,278,87,278, fill="black", width=2.5) # B to airport - arrow_side2



canvas.create_line(260,85,350,25, fill="grey", width=2.5) # B to NS - MAIN_PATH
canvas.create_line(342,25,348,25, fill="black", width=2.5) # B to NS - arrow_side1
canvas.create_line(348,35,348,25, fill="black", width=2.5) # B to NS - arrow_side2


canvas.create_line(350,35,280,85, fill="grey", width=2.5) # NS to B - MAIN_PATH
canvas.create_line(280,84,280,77, fill="black", width=2.5) # NS to B - arrow_side1
canvas.create_line(280,84,287,84, fill="black", width=2.5) # NS to B - arrow_side2



canvas.create_line(485,180,375,25, fill="grey", width=2.5) # M to NS - MAIN_PATH
canvas.create_line(385,40,385,50, fill="black", width=2.5) # M to NS - arrow_side1
canvas.create_line(385,40,400,45, fill="black", width=2.5) # M to NS - arrow_side2


canvas.create_line(510,180,400,25, fill="grey", width=2.5) # NS to M - MAIN_PATH
canvas.create_line(507,178,503,173, fill="black", width=2.5) # NS to M - arrow_side1
canvas.create_line(507,178,515,173, fill="black", width=2.5) # NS to M - arrow_side2



canvas.create_line(485,180,315,100, fill="grey", width=2.5) # B to M - MAIN_PATH
canvas.create_line(478,180,485,180, fill="black", width=2.5) # B to M - arrow_side1
canvas.create_line(485,173,485,180, fill="black", width=2.5) # B to M - arrow_side2


canvas.create_line(510,180,315,90, fill="grey", width=2.5) # M to B - MATH_PATH
canvas.create_line(317,90,327,90, fill="black", width=2.5) # M to B - arrow_side1
canvas.create_line(317,90,317,100, fill="black", width=2.5) # M to B - arrow_side2



def getShortestPath_list (graph,initial,final):
    if initial==final:
      return "You are already on your destination"
    if initial not in graph:
      return 'Node does not exist in graph'
    if final not in graph:
      return 'Node does not exist in graph'
    path = {}
    adj_node = {}
    queue = [initial]
    for node in graph:
        path[node] = float("inf")
        adj_node[node] = None    
    path[initial] = 0
    while queue:
        cur = queue.pop(0)
        for i,j in graph[cur]:
            alternate = j + path[cur]
            if path[i] > alternate:
                path[i] = alternate
                adj_node[i] = cur
                queue.insert(BinarySearch(i, path, queue),i)
    if path[final]==float('inf'):
      return 'No such path exists'
    l=[]
    x = final
    while x!=None:
        l.insert(0,(adj_node[x],x))
        x=adj_node[x]   
    return l[1:]
def BinarySearch(x, gr, l):
  start, end = 0, len(l) - 1
  while end >= start:
    mid = (start+end) // 2
    if gr[l[mid]] == gr[x]:
      return mid
    elif gr[l[mid]] > gr[x]:
      end = mid - 1  
    else:
      start = mid + 1
  return end+1
def Dijkstra(G,initial,final):
    path = {}
    adj_node = {}
    queue = [initial]
    for node in G:
        path[node] = float("inf")
        adj_node[node] = []    
    path[initial] = 0
    while queue:
        cur = queue.pop(0)
        for i,j in G[cur]:
            alternate = j + path[cur]
            if path[i] > alternate:
                path[i] = alternate
                adj_node[i] = [cur]
                queue.insert(BinarySearch(i, path, queue),i)
            elif alternate == path[i] and cur not in adj_node[i]:
                adj_node[i].append(cur)
    if path[final]==float('inf'):
      return False
    return (path,adj_node)


def all_shortest_paths(gr,fin,ini,visited,paths):
    visited.insert(0,fin)
    if fin==ini:
        paths.append(visited[:])
    else:
        for i in gr[fin]:
            if i not in visited:
                all_shortest_paths(gr,i,ini,visited,paths)
    visited.remove(fin)


def  getShortestPath (G, initial, final):
    global shorted_path_cost
    if initial not in G:
      print('Node does not exist in graph')
    if final not in G:
      print('Node does not exist in graph')
    paths=[]
    rpm=Dijkstra(G,initial,final)
    if rpm==False:
      return 'No such Path exists'
    path,adj_node=rpm[0],rpm[1]
    all_shortest_paths(adj_node,final,initial,[],paths)
    print('The shortest path between {:} and {:} costs {:} and can be achieved through:'.format(initial,final,path[final]))
    shorted_path_cost = path[final]
    for i in paths:
        for j in i[:-1]:
            print('{:} ---> '.format(j),end='')
        print(i[-1],end='')
getShortestPath (G, inp, inp_2)
print()
s_path = getShortestPath_list(G,inp,inp_2)
print(s_path)

origin_text_label = Label(start, text="Origin selected: ")
origin_text_label.place(x=700, y=50)
origin_print_label = Label(start, text=inp, bg="white")
origin_print_label.place(x=800, y=50)

destination_text_label = Label(start, text="Destination selected: ")
destination_text_label.place(x=700, y=75)
destination_print_label = Label(start, text=inp_2, bg="white")
destination_print_label.place(x=825, y=75)

text_output_print_label = Label(start, text="The shorted path followed takes the following vertices, in that order:")
text_output_print_label.place(x=700, y=120)

arrow_label1 = Label(start, text="--->", bg = "white")
arrow_label2 = Label(start, text="--->", bg = "white")

arrow_label1.place(x=800, y=150)

vertex_label1 = Label(start, text=s_path[0][0], bg = "white")
vertex_label1.place(x=700,y=150)

vertex_label2 = Label(start, text=s_path[0][1], bg = "white")
vertex_label2.place(x=825,y=150)

cost_label = Label(start, text = "The shorted path is of the distance (in km): ")
cost_label.place(x=700, y=200)

cost_print_label = Label(start, text=shorted_path_cost, bg="white")
cost_print_label.place(x=950, y=200)


if len(s_path) == 1:
  print("two vertices")



  if s_path[0][0] == "Habib University":
    if s_path[0][1] == "millenium mall":
      canvas.create_line(315,185,450,185, fill="blue", width=2.5) # HU to mMall
    elif s_path[0][1] == "airport":
      canvas.create_line(220,185,128,285, fill="blue", width=2.5) # HU to airport
    elif s_path[0][1] == "Balochistan Sajji":
      canvas.create_line(260,180,260,110, fill="blue", width=2.5) # HU to B
  
  if s_path[0][0] == "airport":
    if s_path[0][1] == "Balochistan Sajji":
      canvas.create_line(65,280,220,92, fill="blue", width=2.5) # airport to B
    elif s_path[0][1] == "millenium mall":
      canvas.create_line(128,285,450,185, fill="blue", width=2.5) # airport to mMall
  
  if s_path[0][0] == "Balochistan Sajji":
    if s_path[0][1] == "National Stadium":
      canvas.create_line(260,85,350,25, fill="blue", width=2.5) # B to NS
    elif s_path[0][1] == "millenium mall":
      canvas.create_line(485,180,315,100, fill="blue", width=2.5) # B to M
    elif s_path[0][1] == "Habib University":
      canvas.create_line(280,110,280,180, fill="blue", width=2.5) # B to HU
    elif s_path[0][1] == "airport":
      canvas.create_line(220,105,80,280, fill="blue", width=2.5) # B to airport

  if s_path[0][0] == "millenium mall":
    if s_path[0][1] == "airport":
      canvas.create_line(128,300,450,200, fill="blue", width=2.5) # mMall to airport
    elif s_path[0][1] == "Habib University":
      canvas.create_line(315,200,450,200, fill="blue", width=2.5) # mMall to HU
    elif s_path[0][1] == "Balochistan Sajji":
      canvas.create_line(510,180,315,90, fill="blue", width=2.5) # M to B
    elif s_path[0][1] == "National Stadium":    
      canvas.create_line(485,180,375,25, fill="blue", width=2.5) # M to NS
    
  if s_path[0][0] == "National Stadium":
    if s_path[0][1] == "Balochistan Sajji":
      canvas.create_line(350,35,280,85, fill="blue", width=2.5) # NS to B
    elif s_path[0][1] == "millenium mall":
      canvas.create_line(510,180,400,25, fill="blue", width=2.5) # NS to M


elif len(s_path) == 2:
  print("three vertices")

  arrow_label2.place(x=925, y=150)
  vertex_label3 = Label(start, text=s_path[1][1], bg = "white")
  vertex_label3.place(x=960,y=150)


  if s_path[0][0] == "Habib University" or s_path[1][0] == "Habib University":
    if s_path[0][1] == "millenium mall" or s_path[1][1] == "millenium mall":
      canvas.create_line(315,185,450,185, fill="blue", width=2.5) # HU to mMall
    elif s_path[0][1] == "airport" or s_path[1][1] == "airport":
      canvas.create_line(220,185,128,285, fill="blue", width=2.5) # HU to airport
    elif s_path[0][1] == "Balochistan Sajji" or s_path[1][1] == "Balochistan Sajji":
      canvas.create_line(260,180,260,110, fill="blue", width=2.5) # HU to B
  
  if s_path[0][0] == "airport" or s_path[1][0] == "airport":
    if s_path[0][1] == "Balochistan Sajji" or s_path[1][1] == "Balochistan Sajji":
      canvas.create_line(65,280,220,92, fill="blue", width=2.5) # airport to B
    elif s_path[0][1] == "millenium mall" or s_path[1][1] == "millenium mall":
      canvas.create_line(128,285,450,185, fill="blue", width=2.5) # airport to mMall
  
  if s_path[0][0] == "Balochistan Sajji" or s_path[1][0] == "Balochistan Sajji":
    if s_path[0][1] == "National Stadium" or s_path[1][1] == "National Stadium":
      canvas.create_line(260,85,350,25, fill="blue", width=2.5) # B to NS
    elif s_path[0][1] == "millenium mall" or s_path[1][1] == "millenium mall":
      canvas.create_line(485,180,315,100, fill="blue", width=2.5) # B to M
    elif s_path[0][1] == "Habib University" or s_path[1][1] == "Habib University":
      canvas.create_line(280,110,280,180, fill="blue", width=2.5) # B to HU
    elif s_path[0][1] == "airport" or s_path[1][1] == "airport":
      canvas.create_line(220,105,80,280, fill="blue", width=2.5) # B to airport

  if s_path[0][0] == "millenium mall" or s_path[1][0] == "millenium mall":
    if s_path[0][1] == "airport" or s_path[1][1] == "airport":
      canvas.create_line(128,300,450,200, fill="blue", width=2.5) # mMall to airport
    elif s_path[0][1] == "Habib University" or s_path[1][1] == "Habib University":
      canvas.create_line(315,200,450,200, fill="blue", width=2.5) # mMall to HU
    elif s_path[0][1] == "Balochistan Sajji" or s_path[1][1] == "Balochistan Sajji":
      canvas.create_line(510,180,315,90, fill="blue", width=2.5) # M to B
    elif s_path[0][1] == "National Stadium" or s_path[1][1] == "National Stadium":    
      canvas.create_line(485,180,375,25, fill="blue", width=2.5) # M to NS
    
  if s_path[0][0] == "National Stadium" or s_path[1][0] == "National Stadium":
    if s_path[0][1] == "Balochistan Sajji" or s_path[1][1] == "Balochistan Sajji":
      canvas.create_line(350,35,280,85, fill="blue", width=2.5) # NS to B
    elif s_path[0][1] == "millenium mall" or s_path[1][1] == "millenium mall":
      canvas.create_line(510,180,400,25, fill="blue", width=2.5) # NS to M


start.mainloop()

