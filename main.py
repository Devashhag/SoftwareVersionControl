##final  code to implement A* star on any device
'''
 start -->       9,65
 fb->9,48
second bloc-->     23,48
third block->      27,48
fourth block->      21,56
fifth->          31,56
design 6 ->      19,39
deisgn 7 ->      23,39
deisgn 8-> 
ninth->        35,42
tenth->       48,41
eleventh->     57,43
hubble->9,60
lib->       14,28
it ->26,28
barons->6,32
mac->6,40
food coure->30,59
ground->23,14
amphi  ->34,49
md guest house->10,30
frisco->26,51
gandhi chowk->    34,38
tulips=>50,37
boys ->53,35
lab->55,35
'''


from libraries import *
from colors import *
from shortest_distance import *
from stru import *## structure is boundaries



##main code

def onclick():
    global start
    global end
    sta = start_box.get().split(',')
    en_ = end_box.get().split(',')
    start = grid[int(sta[0])][int(sta[1])]
    end = grid[int(en_[0])][int(en_[1])]
    window_tk.quit()  # imp otherwise
    window_tk.destroy()


window_tk = Tk()
label = Label(window_tk, text='start(x,y)--> ')
start_box = Entry(window_tk)
new_label = Label(window_tk, text='endpos(x,y)->: ')
end_box = Entry(window_tk)


submit = Button(window_tk, text='Click Me', command=onclick)  # onclick fnctn

submit.grid(columnspan=3, row=3)
new_label.grid(row=1, pady=4)
end_box.grid(row=1, column=1, pady=4)
start_box.grid(row=0, column=1, pady=4)
label.grid(row=0, pady=4)

window_tk.update()
mainloop()

pygame.init()
openlist.append(start)  # add the start node


end.start(green, 0)
start.start(red, 0)

loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # RETURN COMMAND TO RUNN
                loop = False
                break

for i in range(cols):
    for j in range(rows):
        grid[i][j].update_neighbour(grid)


def main():
    end.start(lightgr, 0)
    # lowest is the current index
    while len(openlist) > 0:  # while destination is not reached
        lowestIndex = 0  # get the current node
        for i in range(len(openlist)):  # consider node with lowest f score
            if openlist[i].f < openlist[lowestIndex].f:
                lowestIndex = i

        # current is the lowest value as of now
        current = openlist[lowestIndex]
        if current == end:  # if its a final node
            print('done', current.f)  # stop algo
            start.start(red, 0)
            tempg = current.f  # temp is the current here
            for i in range(round(current.f)):  # putting current in closed list
                # while current is not the one
                current.closed = False  # add the current position
                current.start(blue, 0)
                current = current.previous  # previous node
            end.start(lightgr, 0)
            # if program executed show up message

            result = messagebox.askokcancel('program', ("executed"))
            if result == True:
                os.execl(sys.executable, sys.executable, *sys.argv)

            pygame.quit()
        # pushing and poping is done simultaenously to check node is done or not
        openlist.pop(lowestIndex)  # poping is done here
        closedlist.append(current)
# we can say neighbour or children
# neighbours=[]
        # setting neighbour of current node
        neighbors = current.neighbors

        for i in range(len(neighbors)):
            neighbor = neighbors[i]  # getting all the position neighbours
            # if its not in closed list  its in openlist (a)
            if neighbor not in closedlist:
                tempg = current.g + current.value  # temg g to calc the current position
                if neighbor in openlist:  # for open list
                    if neighbor.g > tempg:
                        neighbor.g = tempg
                else:
                    neighbor.g = tempg
                    # (a ) part here means neighbour is in openlist
                    openlist.append(neighbor)
                # calc the f,g,h values
            neighbor.h = heurestic_fn(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h
            # now this goes on till it find its path and checking neighbour updated value
            if neighbor.previous == None:
                neighbor.previous = current

    current.closed = True


while True:

    pygame.display.update()
    main()
