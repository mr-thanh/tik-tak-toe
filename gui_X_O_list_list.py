
from tkinter import Button,Label,Tk,Frame,StringVar, messagebox, PhotoImage

map_to_tick = [['1', '2', '3'],
                        ['4', '5', '6'],
                        ['7', '8', '9']]

win_dict = {"x":["X wins this game",0],"o":["O wins this game",0]}
var_count = 0
btn1_dis = 1
btn2_dis = 1
btn3_dis = 1
btn4_dis = 1
btn5_dis = 1
btn6_dis = 1
btn7_dis = 1
btn8_dis = 1
btn9_dis = 1
dis_button = {'1':btn1_dis,'2':btn2_dis,'3':btn3_dis,'4':btn4_dis,'5':btn5_dis,'6':btn6_dis,'7':btn7_dis,'8':btn8_dis,'9':btn9_dis}
current_x_o = ""
# print(map_to_tick)

def replace_all_value_array(array,old_value,new_value):
    dimension = len(array[0])
    for i in range(dimension):
        for j in range(dimension):
            if array[i][j] == old_value:
                array[i][j] = new_value

def alternate():
    while True:
        yield "x"
        yield "o"

x_o = alternate()

def resetall():
    global map_to_tick
    global var_count
    var_count = 0
    for position in range(1,10):
        dis_button[str(position)] = 1
    for i in (btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9):
        i.config(image=image_default)
    win_dict["x"][1] = 0
    win_dict["o"][1] = 0
    var_result.set(">> XXX 0 - 0 OOO <<")
    map_to_tick = [['1', '2', '3'],
                            ['4', '5', '6'],
                            ['7', '8', '9']]

def refresh():
    global map_to_tick
    global var_count
    var_count = 0
    for position in range(1,10):
        dis_button[str(position)] = 1
    for i in (btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9):
        i.config(image=image_default,state="normal")
    map_to_tick = [['1', '2', '3'],
                            ['4', '5', '6'],
                            ['7', '8', '9']]

def is_win(array):
    x_win = ["x","x","x"]
    o_win = ["o","o","o"]
    temp = []
    diagonal_1 = []
    diagonal_2 = []
    dimension = len(array[0])
    # get row
    for row in array:
        temp.append(row)
    # get column
    for i in range(dimension):
        temp_col = []
        for j in range(dimension):
            temp_col.append(array[j][i])
        temp.append(temp_col)
    # get first diagonal
    for i in range(dimension):
        diagonal_1.append(array[i][i])
    temp.append(diagonal_1)
    # get second diagonal
    for i in range(dimension):
        diagonal_2.append(array[dimension - 1 - i][i])
    temp.append(diagonal_2)
    if (x_win in temp) or (o_win in temp):
        for position in range(1, 10):
            dis_button[str(position)] = 2
        return True
    return False

def result():
    if is_win(map_to_tick):
        win_dict[current_x_o][1] += 1
        var_result.set(f">> XXX {win_dict['x'][1]} - {win_dict['o'][1]} OOO <<")
        messagebox.showinfo("Notice",win_dict[current_x_o][0])
    elif var_count == 9:
        messagebox.showinfo("Notice","It's draw!\nPress Replay to renew game.")
    else:
        pass

def click(button,position):
    global var_count
    global btn1_dis
    global current_x_o
    if dis_button[position] == 1:
        dis_button[position] += 1
        var_count += 1
        current_x_o = next(x_o)
        button.configure(image=dict_image[current_x_o])
        replace_all_value_array(map_to_tick,position,current_x_o)
        result()
        # print(map_to_tick,var_count)

window = Tk()
window.title("TikTakToe")
window.geometry("300x300")

window.iconbitmap(r"footage\tiktaktoe.ico")

image_x = PhotoImage(file=r"footage\x.png").subsample(11,11)
image_o = PhotoImage(file=r"footage\o.png").subsample(11,11)
image_default = PhotoImage(file=r"footage\default.png").subsample(5,5)


dict_image = {"x":image_x,"o":image_o}

var_result = StringVar()
var_result.set(">> XXX 0 - 0 OOO <<")

frm_master = Frame(window)
frm_master.pack()

lbl_score = Label(frm_master,textvariable=var_result,font=('Times New Roman',17,'bold'))
lbl_score.grid(row=0,columnspan=2)

frm_main = Frame(frm_master)
frm_main.grid(row=1,column=0,columnspan=2,pady=10)
btn_replay = Button(frm_master,text="Replay",font=('Times New Roman',15,'bold'),width=7,height=1,command=refresh )
btn_replay.grid(row=2,column=0,pady=10,sticky="s")
btn_resetall = Button(frm_master,text="Reset All",font=('Times New Roman',15,'bold'),width=7,height=1,command= resetall)
btn_resetall.grid(row=2,column=1)

btn1 = Button(frm_main,image=image_default,command= lambda : click(btn1,"1"))
btn1.grid(row=0,column=0)
btn2 = Button(frm_main,image=image_default,command= lambda : click(btn2,"2"))
btn2.grid(row=0,column=1)
btn3 = Button(frm_main,image=image_default,command= lambda : click(btn3,"3"))
btn3.grid(row=0,column=2)
btn4 = Button(frm_main,image=image_default,command= lambda : click(btn4,"4"))
btn4.grid(row=1,column=0)
btn5 = Button(frm_main,image=image_default,command= lambda : click(btn5,"5"))
btn5.grid(row=1,column=1)
btn6 = Button(frm_main,image=image_default,command= lambda : click(btn6,"6"))
btn6.grid(row=1,column=2)
btn7 = Button(frm_main,image=image_default,command= lambda : click(btn7,"7"))
btn7.grid(row=2,column=0)
btn8 = Button(frm_main,image=image_default,command= lambda : click(btn8,"8"))
btn8.grid(row=2,column=1)
btn9 = Button(frm_main,image=image_default,command= lambda : click(btn9,"9"))
btn9.grid(row=2,column=2)


window.mainloop()



