from tkinter import *
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np

GUI = Tk()
GUI.title("LSES")
GUI.geometry("600x600")
GUI.iconbitmap("LSES-LOGO.ico")
GUI.resizable(False, False)
style = ttk.Style()
 
style.theme_create('pastel', settings={
    ".": {
        "configure": {
            "background": '#ffffff',
            "font": 'white'
        }
    },
    "TNotebook": {
        "configure": {
            "background":'#848a98',
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": '#d9ffcc',
            "font":"white"
        },
        "map": {
            "background": [("selected", '#ccffff')],
        }
    }
})
 
style.theme_use('pastel')

tabControl = ttk.Notebook(GUI)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")

font1 = ("Krungthep", 20)

result = StringVar()
result.set("(X,Y)")
coeff_x = IntVar()
coeff_y = IntVar()
equal = IntVar()
photo = PhotoImage(file = "LSES LOGO.png")
Button(tab1, image = photo).place(x=300, y=100, anchor="center")
e1 = ttk.Entry(tab1, textvariable= coeff_x, width=3, font=font1)
e1.place(x=150, y=200, anchor="center")

l1 = Label(tab1, text="X ", font= font1)
l1.place(x=200, y=200, anchor="center")

l3 = Label(tab1, text=" + ", font= font1)
l3.place(x=250, y=200, anchor="center")

e2 = ttk.Entry(tab1, textvariable= coeff_y, width=3, font=font1)
e2.place(x=300, y=200, anchor="center")

l2 = Label(tab1, text="Y ", font= font1)
l2.place(x=350, y=200, anchor="center")

l4 = Label(tab1, text=" = ", font= font1)
l4.place(x=400, y=200, anchor="center")

e2 = ttk.Entry(tab1, textvariable= equal, width=4, font=font1)
e2.place(x=450, y=200, anchor="center")

# Equation2
coeff_x2 = IntVar()
coeff_y2 = IntVar()
equal2 = IntVar()
e2 = ttk.Entry(tab1, textvariable= coeff_x2, width=3, font=font1)
e2.place(x=150, y=250, anchor="center")

l12 = Label(tab1, text="X ", font= font1)
l12.place(x=200, y=250, anchor="center")

l32 = Label(tab1, text=" + ", font= font1)
l32.place(x=250, y=250, anchor="center")

e22 = ttk.Entry(tab1, textvariable= coeff_y2, width=3, font=font1)
e22.place(x=300, y=250, anchor="center")

l22 = Label(tab1, text="Y ", font= font1)
l22.place(x=350, y=250, anchor="center")

l42 = Label(tab1, text=" = ", font= font1)
l42.place(x=400, y=250, anchor="center")

e22 = ttk.Entry(tab1, textvariable= equal2, width=4, font=font1)
e22.place(x=450, y=250, anchor="center")


#tab2
result_x_t2 = StringVar()
result_x_t2.set("X=_")
result_y_t2 = StringVar()
result_y_t2.set("Y=_")
result_z_t2 = StringVar()
result_z_t2.set("Z=_")
coeff_x_t2 = IntVar()
coeff_y_t2 = IntVar()
coeff_z_t2 = IntVar()
equal_t2 = IntVar()
Button(tab2, image = photo).place(x=300, y=100, anchor="center")
e1_t2 = ttk.Entry(tab2, textvariable= coeff_x_t2, width=3, font=font1)
e1_t2.place(x=70, y=200, anchor="center")

l1_t2 = Label(tab2, text="X ", font= font1)
l1_t2.place(x=120, y=200, anchor="center")

l3_t2 = Label(tab2, text=" + ", font= font1)
l3_t2.place(x=170, y=200, anchor="center")

e2_t2 = ttk.Entry(tab2, textvariable= coeff_y_t2, width=3, font=font1)
e2_t2.place(x=220, y=200, anchor="center")

l2_t2 = Label(tab2, text="Y ", font= font1)
l2_t2.place(x=270, y=200, anchor="center")

l3_t2 = Label(tab2, text=" + ", font= font1)
l3_t2.place(x=320, y=200, anchor="center")

e2_t2 = ttk.Entry(tab2, textvariable= coeff_z_t2, width=3, font=font1)
e2_t2.place(x=370, y=200, anchor="center")

l2_t2 = Label(tab2, text="Z ", font= font1)
l2_t2.place(x=420, y=200, anchor="center")

l4_t2 = Label(tab2, text=" = ", font= font1)
l4_t2.place(x=470, y=200, anchor="center")

e2_t2 = ttk.Entry(tab2, textvariable= equal_t2, width=4, font=font1)
e2_t2.place(x=520, y=200, anchor="center")

# Equation2
coeff_x2_t2 = IntVar()
coeff_y2_t2 = IntVar()
coeff_z2_t2 = IntVar()
equal2_t2 = IntVar()

e1_t2 = ttk.Entry(tab2, textvariable= coeff_x2_t2, width=3, font=font1)
e1_t2.place(x=70, y=250, anchor="center")

l1_t2 = Label(tab2, text="X ", font= font1)
l1_t2.place(x=120, y=250, anchor="center")

l3_t2 = Label(tab2, text=" + ", font= font1)
l3_t2.place(x=170, y=250, anchor="center")

e2_t2 = ttk.Entry(tab2, textvariable= coeff_y2_t2, width=3, font=font1)
e2_t2.place(x=220, y=250, anchor="center")

l2_t2 = Label(tab2, text="Y ", font= font1)
l2_t2.place(x=270, y=250, anchor="center")

l3_t2 = Label(tab2, text=" + ", font= font1)
l3_t2.place(x=320, y=250, anchor="center")

e2_t2 = ttk.Entry(tab2, textvariable= coeff_z2_t2, width=3, font=font1)
e2_t2.place(x=370, y=250, anchor="center")

l2_t2 = Label(tab2, text="Z ", font= font1)
l2_t2.place(x=420, y=250, anchor="center")

l4_t2 = Label(tab2, text=" = ", font= font1)
l4_t2.place(x=470, y=250, anchor="center")

e2_t2 = ttk.Entry(tab2, textvariable= equal2_t2, width=4, font=font1)
e2_t2.place(x=520, y=250, anchor="center")


# Equation3
coeff_x3_t2 = IntVar()
coeff_y3_t2 = IntVar()
coeff_z3_t2 = IntVar()
equal3_t2 = IntVar()

e1_t2 = ttk.Entry(tab2, textvariable= coeff_x3_t2, width=3, font=font1)
e1_t2.place(x=70, y=300, anchor="center")

l1_t2 = Label(tab2, text="X ", font= font1)
l1_t2.place(x=120, y=300, anchor="center")

l3_t2 = Label(tab2, text=" + ", font= font1)
l3_t2.place(x=170, y=300, anchor="center")

e2_t2 = ttk.Entry(tab2, textvariable= coeff_y3_t2, width=3, font=font1)
e2_t2.place(x=220, y=300, anchor="center")

l2_t2 = Label(tab2, text="Y ", font= font1)
l2_t2.place(x=270, y=300, anchor="center")

l3_t2 = Label(tab2, text=" + ", font= font1)
l3_t2.place(x=320, y=300, anchor="center")

e2_t2 = ttk.Entry(tab2, textvariable= coeff_z3_t2, width=3, font=font1)
e2_t2.place(x=370, y=300, anchor="center")

l2_t2 = Label(tab2, text="Z ", font= font1)
l2_t2.place(x=420, y=300, anchor="center")

l4_t2 = Label(tab2, text=" = ", font= font1)
l4_t2.place(x=470, y=300, anchor="center")

e2_t2 = ttk.Entry(tab2, textvariable= equal3_t2, width=4, font=font1)
e2_t2.place(x=520, y=300, anchor="center")


def clear():
    coeff_x.set(0)
    coeff_y.set(0)
    equal.set(0)
    coeff_x2.set(0)
    coeff_y2.set(0)
    equal2.set(0)

def clear2():
    coeff_x_t2.set(0)
    coeff_y_t2.set(0)
    coeff_z_t2.set(0)
    equal_t2.set(0)
    coeff_x2_t2.set(0)
    coeff_y2_t2.set(0)
    coeff_z2_t2.set(0)
    equal2_t2.set(0)
    coeff_x3_t2.set(0)
    coeff_y3_t2.set(0)
    coeff_z3_t2.set(0)
    equal3_t2.set(0)

def det(a):
    if len(a) == 2:
        det = a[0,0]*a[1,1]-a[1,0]*a[0,1]
    elif len(a) == 3:
        det = a[0,0]*(a[1,1]*a[2,2]-a[2,1]*a[1,2]) - a[0,1]*(a[1,0]*a[2,2]-a[2,0]*a[1,2]) + a[0,2]*(a[1,0]*a[2,1]-a[2,0]*a[1,1])
    else:
        return "undefined"
    return det

def plot(eq, eq2, title, result_x= None, result_y= None):
    xs = []
    ys = []
    xs2 = []
    ys2 = []

    for i in range (int(-10), int(11)):
        yeq = (-x1)/y1*i + equal_result1/y1
        xs.append(i)
        ys.append(yeq)
    for i in range (int(-10), int(11)):
        yeq2 = (-x2)/y2*i + equal_result2/y2
        xs2.append(i)
        ys2.append(yeq2)

    plt.plot(xs,ys,label=eq)
    plt.plot(xs2,ys2,label=eq2)
    plt.title(title)

    if result_x != None:
        plt.scatter(result_x,result_y,label=(result_x,result_y))


    plt.xlabel('x axis')
    plt.ylabel('y axis')

    plt.grid(alpha=.4,linestyle='--')

    plt.legend()

    plt.show()

def get():
    try:
        global x1, y1, equal_result1, equal_result2, x2, y2
        x1 = coeff_x.get()
        y1 = coeff_y.get()
        equal_result1 = equal.get()
        x2 = coeff_x2.get()
        y2 = coeff_y2.get()
        equal_result2 = equal2.get()

    except Exception as error:
        messagebox.showerror("ERROR","Please fill in the correct numbers! No strings or letters!")
        clear()
        return

    if x1 == 0 & y1 == 0:
        messagebox.showwarning("Warning","Please fill in the Coefficient of X1 and Y1!")
        clear()
        return
    
    if x2 == 0 & y2 ==0:
        messagebox.showwarning("Warning","Please fill in the Coefficient of X2 and Y2!")
        clear()
        return

    A = np.array([
        [x1, y1],
        [x2, y2]
    ])

    A1 = np.array([
        [equal_result1, y1],
        [equal_result2, y2]
    ])

    A2 = np.array([
        [x1, equal_result1],
        [x2, equal_result2]
    ])

    det_A = det(A)
    det_A1 = det(A1)
    det_A2 = det(A2)
    print(det_A, det_A1, det_A2)
    print(det_A == 0, det_A1 == 0, det_A2 == 0)
    eq = "y = {}x+{}".format((-x1)/y1, equal_result1/y1)
    eq2 = "y = {}x+{}".format((-x2)/y2, equal_result2/y2)

    if det_A == 0 and det_A1 == 0 and det_A2 == 0:
        title = "Infinitely Many Solutions (overlapping lines)"
        result.set(title)
        plot(eq, eq2, title)

    elif det_A == 0 and det_A1 !=0 and det_A2 != 0:
        title = "No Solution (parallel lines)"
        result.set(title)
        plot(eq, eq2, title)

    else:
        result_x = det_A1/det_A
        result_y = det_A2/det_A
        title = "({},{})".format(result_x, result_y)
        result.set(title)
        plot(eq, eq2, title, result_x = result_x, result_y = result_y)

def get_t2():
    try:
        x1 = coeff_x_t2.get()
        y1 = coeff_y_t2.get()
        z1 = coeff_z_t2.get()
        e1 = equal_t2.get()
        x2 = coeff_x2_t2.get()
        y2 = coeff_y2_t2.get()
        z2 = coeff_z2_t2.get()
        e2 = equal2_t2.get()
        x3 = coeff_x3_t2.get()
        y3 = coeff_y3_t2.get()
        z3 = coeff_z3_t2.get()
        e3 = equal3_t2.get()

    except Exception as error:
        messagebox.showerror("ERROR","Please fill in the correct numbers! No strings or letters!")
        clear2()
        return
    if x1 == 0 & y1 == 0 & z1 == 0:
        messagebox.showwarning("Warning","Please fill in the Coefficient of X1, Y1 and Z1!")
        clear2()
        return
    
    if x2 == 0 & y2 ==0 & z2 == 0:
        messagebox.showwarning("Warning","Please fill in the Coefficient of X2, Y2, and Z2!")
        clear2()
        return
    
    if x3 == 0 & y3 ==0 & z3 == 0:
        messagebox.showwarning("Warning","Please fill in the Coefficient of X3, Y3, and Z3!")
        clear2()
        return

    A = np.array([
        [x1, y1, z1],
        [x2, y2, z2],
        [x3, y3, z3]
    ])

    AX = np.array([
        [e1, y1, z1],
        [e2, y2, z2],
        [e3, y3, z3]
    ])

    AY = np.array([
        [x1, e1, z1],
        [x2, e2, z2],
        [x3, e3, z3]
    ])

    AZ = np.array([
        [x1, y1, e1],
        [x2, y2, e2],
        [x3, y3, e3]
    ])

    det_A = det(A)
    det_AX = det(AX)
    det_AY = det(AY)
    det_AZ = det(AZ)
    if det_A != 0:
        X = det_AX/det_A
        Y = det_AY/det_A
        Z = det_AZ/det_A
    else:
        X = "-"
        Y = "-"
        Z = "-"
    result_x_t2.set(f"X={X}")
    result_y_t2.set(f"Y={Y}")
    result_z_t2.set(f"Z={Z}")
    print("////")
    print(det_A, det_AX, det_AY, det_AZ)
    print(X,Y,Z)

    # print(X,Y,Z)
    # result_x_t2
    # result_y_t2
    # result_z_t2

b1 = Button(tab1, text="Solve", command = get, bg="green")
b1.place(x=300, y=325,anchor="center", width=50, height=35)

Label(tab1, text="Solution", font=font1).place(x=300, y=385, anchor="center")
result_label = Label(tab1, textvariable= result, font=font1)
result_label.place(x=300, y=415, anchor="center")

b1 = Button(tab2, text="Solve", command = get_t2, bg="green")
b1.place(x=300, y=375,anchor="center", width=50, height=35) #75

Label(tab2, text="Solution", font=font1).place(x=300, y=435, anchor="center")#60

Label(tab2, textvariable= result_x_t2, font=font1).place(x=300, y=465, anchor="center")#30

Label(tab2, textvariable= result_y_t2, font=font1).place(x=300, y=495, anchor="center")#30

Label(tab2, textvariable= result_z_t2, font=font1).place(x=300, y=525, anchor="center")#30

GUI.mainloop()