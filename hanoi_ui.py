"""hanoi_ui.py"""

import random
import time
import tkinter



#TODO: This for a second version with dragable disks..
#--Start code to make draggable, from: https://stackoverflow.com/questions/37280004/tkinter-how-to-drag-and-drop-widgets
def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)
def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y
def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)
#--End code to make draggable


class HanoiTowers:
    def __init__(self, numberOfDisks, window):
        self.numberOfDisk = numberOfDisks
        self.window = window
        self.towers={
            "A": [],
            "B": [],
            "C": []
        }
        self.poles_x_position=[]
        self.poles_y_position = 100
        self.pole_space = (numberOfDisks+3)*10
        self.disk_height = 10
        self.stop=False
        self.create_poles()
        self.create_disks()

    def reset_towers(self,number_of_disks):
        for disks in self.towers.values():
            print(f' soy {disks}')
            for disk in disks:
                disk.destroy()

        try:
            number = int(number_of_disks)
            self.numberOfDisk = number_of_disks
            self.create_poles()
        except ValueError:
            print("Only numbers pleaseee!!")
            
        self.towers={
            "A": [],
            "B": [],
            "C": []
        }
        self.stop=False
        self.create_disks()

    def hanoi_pole(self,position_x,position_y):
        self.pole_height = (self.numberOfDisk+2)*self.disk_height
        print(f'pole height: {self.numberOfDisk+4}')
        return tkinter.Label(
            self.window, 
            text = "p", 
            bg = "black", 
            fg="black",
            ).place(
                x=position_x, 
                y=position_y,
                width=self.disk_height,
                height=self.pole_height
                )
    
    def create_poles(self):
        for pole in range(3):
            x_position = (pole+1)*self.pole_space
            print(f'pole space: {x_position}')
            self.hanoi_pole(x_position,100)
            self.poles_x_position.append(x_position)
        return

    def hanoi_disk(self,text,width,color):

        disk = tkinter.Label(
            self.window, 
            text = text, 
            bg = color, 
            fg="white",
            )
        disk.place(
                x=self.poles_x_position[0] - (width*5/2) + 5, #importante
                y=text*10 + self.poles_y_position + 5, #importante
                height=10,
                width=width*5, 
                )
        return disk
    
    def create_disks(self):
        
        for disk in range(self.numberOfDisk):
            color = f'#{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'
            print(disk)
            disk_width = (self.numberOfDisk - disk + 1)*2
            self.towers["A"].append(
                self.hanoi_disk(
                    text=self.numberOfDisk - disk,
                    width=disk_width, 
                    color=color
                    )
                )
        return

    def move_disk(self,source,destination):
        source_last_index = len(self.towers[source])-1
        time.sleep(0.001)
        x_destiny = self.poles_x_position[list(self.towers).index(destination)]
        width_disk = self.towers[source][source_last_index].winfo_width()
        x_disk = self.towers[source][source_last_index].winfo_x() + ((width_disk-5)*2/5)

        if x_destiny == x_disk:
            new_y = self.towers[source][source_last_index].winfo_y() +1
            if new_y<85 + self.pole_height  - (len(self.towers[destination])*10):
                # y=text*10 + self.poles_y_position + 5,
                print(f'new_y: {new_y} || pole_height: {self.pole_height} || ?: {(len(self.towers[destination])*10)}')
                print('Bajando')
                self.towers[source][source_last_index].place_configure(y=new_y)  
                self.window.update()
                self.move_disk(source,destination)
            else:
                print('ready!')
                self.towers[destination].append(self.towers[source][source_last_index])
                self.towers[source].pop()
        elif self.stop:
            return
        else:
            new_y = self.towers[source][source_last_index].winfo_y() -1
            if not new_y<80:
                print('subiendo')
                print(new_y)
                self.towers[source][source_last_index].place_configure(y=new_y)  
                self.window.update()
                self.move_disk(source,destination)
            else:
                if x_destiny - x_disk > 0:
                    #mover right
                    new_x = self.towers[source][source_last_index].winfo_x() +1
                    print('derecha')
                    print(new_x)
                    self.towers[source][source_last_index].place_configure(x=new_x)  
                    self.window.update()
                    self.move_disk(source,destination)
                else:
                    #mover left
                    new_x = self.towers[source][source_last_index].winfo_x() -1
                    print('izquierda')
                    print(new_x)
                    self.towers[source][source_last_index].place_configure(x=new_x)  
                    self.window.update()
                    self.move_disk(source,destination)
            return
            
        return

    def hanoi(self, n , source, auxiliary, destination):
        if n==1:
            self.move_disk(source,destination)
            return
        elif self.stop:
            return
        self.hanoi(n-1, source, destination, auxiliary)
        self.move_disk(source,destination)
        self.hanoi(n-1, auxiliary, source, destination)
        return

    def resolve(self):
        if self.stop:
            self.reset_towers(self.numberOfDisk)
        self.hanoi(self.numberOfDisk,"A","B","C")
        return
        
    def stopResolve(self):
        self.stop=True
        self.hanoi(self.numberOfDisk,"A","B","C")
        return    


def create_frame_for_towers(window,number_of_disks):

    frame_hanoi_towers_show =tkinter.Frame(
        window, 
        height=(number_of_disks*10)+220, 
        width=(number_of_disks+3)*42
        )
    frame_hanoi_towers_show.pack(fill = tkinter.Y, expand=True)
    return frame_hanoi_towers_show
    
    return

def frame_for_control_towers(window,hanoi_tower_ui,hanoi):
    frame_towers_control = tkinter.Frame(
    window,
    pady=50
    )
    lbl_input_number = tkinter.Label(
        frame_towers_control,
        text = "Write the number of disks:",
        font=("Arial", 12)
        )
    
    entry_number_of_disks = tkinter.Entry(
        frame_towers_control, 
        font=("Arial", 12)
        )

    btn_play_towers = tkinter.Button(
        frame_towers_control,
        text= "Solve the Towers",
        bg="green",
        command= lambda: hanoi.resolve(),
        
    )

    btn_create = tkinter.Button(
        frame_towers_control,
        text= "Create New Towers",
        command= lambda: create_hanoi_towers_ui(window,entry_number_of_disks.get(),hanoi_tower_ui,frame_towers_control)
    )

    btn_stop = tkinter.Button(
        frame_towers_control,
        text= "Stop",
        bg= "red",
        command= lambda: hanoi.stopResolve(),
        
    )

    lbl_input_number.grid(
        row=2,
        column=0,
        columnspan = 2
        )
    
    entry_number_of_disks.grid(
        row=3, 
        column=0
        )

    btn_create.grid(
        row=3, 
        column=1, 
        sticky="ew"
        )
    
    btn_play_towers .grid(
        row=4, 
        column=1,
        sticky="ew"
        )

    btn_stop.grid(
        row=4, 
        column=0, 
        )

    frame_towers_control.pack()
    return

def create_hanoi_towers_ui(window,number_of_disks,hanoi_tower_ui=0,hanoi_control_ui=0):
    try:
        number_of_disks = int(number_of_disks)
        if hanoi_tower_ui:
            hanoi_tower_ui.destroy()
            hanoi_control_ui.destroy()
        hanoi_tower_ui = create_frame_for_towers(window,number_of_disks)
        hanoi = HanoiTowers(
            number_of_disks,
            hanoi_tower_ui
            )
        hanoi_control_ui = frame_for_control_towers(window,hanoi_tower_ui,hanoi)
        return hanoi_control_ui
    except:
        print("This is not a number!!")
        return
    


if __name__ == "__main__":
    
    number_of_disks=4
    hanoi_window = tkinter.Tk()
    hanoi_window.title('Hanoi Towers by David Silva')
    # hanoi_window.geometry("500x500")
 
    title_presentation = tkinter.Label(
        hanoi_window, 
        text = (
            " Hey! This is a recursion program for Artificial Intelligence class, @ThomasMoreGeel "
            ),
        font=("Arial", int(80/number_of_disks))
        )

    subtitle_made_by = tkinter.Label(
        hanoi_window, 
        text = "Made by: David Silva Troya",
        font=("Arial", int(60/number_of_disks))
        )

    title_presentation.pack()
    subtitle_made_by.pack()
    
    create_hanoi_towers_ui(hanoi_window,number_of_disks)
 
    hanoi_window.mainloop()

    