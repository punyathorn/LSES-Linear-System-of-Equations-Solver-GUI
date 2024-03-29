from tkinter import *
import tkinter
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

GUI = Tk()
GUI.title("System of Equations Solver")
GUI.geometry("500x500")
GUI.iconbitmap("LSES-LOGO.ico")

font1 = (None, 15)

result = StringVar()
result.set("(X,Y)")
coeff_x = StringVar()
coeff_y = StringVar()
equal = StringVar()
e1 = ttk.Entry(GUI, textvariable= coeff_x, width=3, font=font1)
e1.place(x=100, y=100, anchor="center")
l1 = Label(GUI, text="X ", font= font1)
l1.place(x=150, y=100, anchor="center")
l3 = Label(GUI, text=" + ", font= font1)
l3.place(x=200, y=100, anchor="center")
e2 = ttk.Entry(GUI, textvariable= coeff_y, width=3, font=font1)
e2.place(x=250, y=100, anchor="center")
l2 = Label(GUI, text="Y ", font= font1)
l2.place(x=300, y=100, anchor="center")
l4 = Label(GUI, text=" = ", font= font1)
l4.place(x=350, y=100, anchor="center")
e2 = ttk.Entry(GUI, textvariable= equal, width=4, font=font1)
e2.place(x=400, y=100, anchor="center")

# Equation2
coeff_x2 = StringVar()
coeff_y2 = StringVar()
equal2 = StringVar()
e2 = ttk.Entry(GUI, textvariable= coeff_x2, width=3, font=font1)
e2.place(x=100, y=150, anchor="center")
l12 = Label(GUI, text="X ", font= font1)
l12.place(x=150, y=150, anchor="center")
l32 = Label(GUI, text=" + ", font= font1)
l32.place(x=200, y=150, anchor="center")
e22 = ttk.Entry(GUI, textvariable= coeff_y2, width=3, font=font1)
e22.place(x=250, y=150, anchor="center")
l22 = Label(GUI, text="Y ", font= font1)
l22.place(x=300, y=150, anchor="center")
l42 = Label(GUI, text=" = ", font= font1)
l42.place(x=350, y=150, anchor="center")
e22 = ttk.Entry(GUI, textvariable= equal2, width=4, font=font1)
e22.place(x=400, y=150, anchor="center")

def get():
    xs = []
    ys = []
    xs2 = []
    ys2 = []
    x = coeff_x.get()
    y = coeff_y.get()
    equal_result = equal.get()
    x2 = coeff_x2.get()
    y2 = coeff_y2.get()
    equal_result2 = equal2.get()
    if x == "":
        messagebox.showwarning("Warning","Please fill in the Coefficient of x1!")
        return
    elif y == "":
        messagebox.showwarning("Warning","Please fill in the Coefficient of y1!")
        return
    elif x2 == "":
        messagebox.showwarning("Warning","Please fill in the Coefficient of x2!")
        return
    elif y2 == "":
        messagebox.showwarning("Warning","Please fill in the Coefficient of y2!")
        return
    elif equal_result == "":
        messagebox.showwarning("Warning","Please fill in the result of equation 1!")
        return
    elif equal_result2 == "":
        messagebox.showwarning("Warning","Please fill in the result of equation2!")
        return
    coeff_x.set("")
    coeff_y.set("")
    equal.set("")
    coeff_x2.set("")
    coeff_y2.set("")
    equal2.set("")
    x = int(x)
    y = int(y)
    equal_result = int(equal_result)
    x2 = int(x2)
    y2 = int(y2)
    equal_result2 = int(equal_result2)
    # equation = (-x+equal_result)/y
    eq = "{}x+{}".format((-x)/y, equal_result/y)
    d1 = (equal_result*y2)-(equal_result2*y)
    d2 = (x*y2)-(x2*y)
    d3 = (x*equal_result2) - (x2*equal_result)
    if d1 == 0 and d2 == 0 and d3 == 0:
        result.set("Infinitely Many Solutions (overlapping lines)")
        eq = "y = {}x+{}".format((-x)/y, equal_result/y)
        eq2 = "y = {}x+{}".format((-x2)/y2, equal_result2/y2)
        for i in range (int(-10), int(11)):
            yeq = (-x)/y*i + equal_result/y
            xs.append(i)
            ys.append(yeq)
        for i in range (int(-10), int(11)):
            yeq2 = (-x2)/y2*i + equal_result2/y2
            xs2.append(i)
            ys2.append(yeq2)
        plt.plot(xs,ys,label=eq)
        plt.plot(xs2,ys2,label=eq2)
        plt.title('Infinitely Many Solutions (overlapping lines)')

        # Add X and y Label
        plt.xlabel('x axis')
        plt.ylabel('y axis')

        # Add a grid
        plt.grid(alpha=.4,linestyle='--')

        # Add a Legend
        plt.legend()

        # Show the plot
        plt.show()
    elif d2 == 0 and d1 !=0 and d3 != 0:
        result.set("No Solution (parallel lines)")
        eq = "y = {}x+{}".format((-x)/y, equal_result/y)
        eq2 = "y = {}x+{}".format((-x2)/y2, equal_result2/y2)
        for i in range (int(-10), int(11)):
            yeq = (-x)/y*i + equal_result/y
            xs.append(i)
            ys.append(yeq)
        for i in range (int(-10), int(11)):
            yeq2 = (-x2)/y2*i + equal_result2/y2
            xs2.append(i)
            ys2.append(yeq2)
        plt.plot(xs,ys,label=eq)
        plt.plot(xs2,ys2,label=eq2)
        plt.title('No Solution (parallel lines)')

        # Add X and y Label
        plt.xlabel('x axis')
        plt.ylabel('y axis')

        # Add a grid
        plt.grid(alpha=.4,linestyle='--')

        # Add a Legend
        plt.legend()

        # Show the plot
        plt.show()
    else:
        result_x = d1/d2
        result_y = d3/d2
        result.set("({},{})".format(result_x, result_y))
        eq = "y = {}x+{}".format((-x)/y, equal_result/y)
        eq2 = "y = {}x+{}".format((-x2)/y2, equal_result2/y2)
        for i in range (int(-10+round(result_x)), int(11+round(result_x))):
            yeq = (-x)/y*i + equal_result/y
            xs.append(i)
            ys.append(yeq)
        for i in range (int(-10+round(result_x)), int(11+round(result_x))):
            yeq2 = (-x2)/y2*i + equal_result2/y2
            xs2.append(i)
            ys2.append(yeq2)
        plt.plot(xs,ys,label=eq)
        plt.plot(xs2,ys2,label=eq2)
        plt.scatter(result_x,result_y,label=(result_x,result_y))
        # Add a title
        plt.title('1 Solution ({},{})'.format(result_x,result_y))

        # Add X and y Label
        plt.xlabel('x axis')
        plt.ylabel('y axis')

        # Add a grid
        plt.grid(alpha=.4,linestyle='--')

        # Add a Legend
        plt.legend()

        # Show the plot
        plt.show()
b1 = ttk.Button(GUI, text="Solve", command= get)
b1.place(x=250, y=225, anchor="center")


result_label = Label(GUI, textvariable= result, font=font1)
result_label.place(x=250, y=300, anchor="center")

GUI.mainloop()