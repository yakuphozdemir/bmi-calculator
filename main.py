import ttkbootstrap as tbs
from PIL import Image, ImageTk

#pyinstaller --onefile -w --icon="bmi1.ico" -n "BMI Calculator"  main.py
root = tbs.Window()
root.title("BMI Calculator")
root.geometry("700x800")
root.minsize(700,800)
root.iconbitmap("bmi1.ico")

"""
a = tbs.Style().theme_names()
print(a)
b=11
style = tbs.Style(a[b])
"""
bootstyle="primary"
style = tbs.Style("dev_theme")

def clear():
    entryW.delete(0, "end")
    entryH.delete(0, "end")
    resultLabel.configure(text="You do not exist at now")

var = tbs.StringVar(value=0)
i = 0
def metric():
    global var, labelH, labelW, i
    i = int(var.get())
    #print(i)
    #print(var.get())
    #print(type(i))
    if i == 0:
        labelW.configure(text="Weight(kg)")
        labelH.configure(text="Height(cm)")
    elif i == 1:
        labelW.configure(text="Weight(lbs)")
        labelH.configure(text="Height(inc)")

bmi = 0
def gauge(bmi):      
    global meter  
    if bmi < 18.5:                                      
        resultLabel.configure(text="Underweight", foreground="#2a9fd6")       #53C9F7
        meter.configure(bootstyle="primary")
    elif bmi >= 18.5 and bmi < 25:                      
        resultLabel.configure(text="Normal Weight", foreground="#00ff40")     #9BB50C
        meter.configure(bootstyle="success")
    elif bmi >= 25 and bmi < 30:
        resultLabel.configure(text="Overweight", foreground="#ffff20")        #F9C801
        meter.configure(bootstyle="info")
    elif bmi >= 30 and bmi < 40:
        resultLabel.configure(text="Obesite", foreground="#ff8800")           #F48B22
        meter.configure(bootstyle="warning")
    elif bmi >= 40:
        resultLabel.configure(text="Warning!!!\nExtreme Obesite", foreground="#cc0000" )     #F83E01
        meter.configure(bootstyle="danger")

#weight = tbs.StringVar()
#height = tbs.StringVar()
def bmiFunc():
    global weight, height, bmi, meter, i
    #weight = float(weight.get())
    #height = float(height.get())
    weight = float(entryW.get())
    height = float(entryH.get())
    bmi1 = float(weight / ((height/100)**2))
    bmi2 = float((703 * weight) / ((height)**2))
    if i == 0: #kg-cm(meter)
        meter.configure(amountused=f"{bmi1:.4}")
        gauge(bmi1)
    elif i == 1: #pound-inches(feet)
        meter.configure(amountused=f"{bmi2:.4}")
        gauge(bmi2)
    #meter.configure(amountused=f"{bmi:.4}")
    

meter = tbs.Meter(root, bootstyle="primary", subtext="BMI", subtextstyle=bootstyle, metertype="semi", amountused=bmi, amounttotal=40, stripethickness=2, meterthickness=55)
meter.place(relx=0.5, rely=0,x=-120, y=70)

resultLabel = tbs.Label(root, text="You do not exist at now", font=("Helvetica",16), justify="center", anchor="n", foreground="#2a9fd6")
resultLabel.place(in_=meter, relx=0.5, rely=1, anchor="n")

radio1 = tbs.Radiobutton(root, text="kg-cm", variable=var, value=0, command=metric)
radio1.place(in_=resultLabel, relx=0.5, rely=1, x=-50, y=20, anchor="n")

radio2 = tbs.Radiobutton(root, text="lbs-inc", variable=var, value=1, command=metric)
radio2.place(in_=radio1, relx=1, rely=0, x=20)

entryW = tbs.Entry(root, bootstyle=bootstyle, text="Weight(kg)")   #textvariable=weight
entryW.place(in_=resultLabel, relx=0.5,rely=1,x=-85, y=60)

entryH = tbs.Entry(root, bootstyle=bootstyle, text="Height(cm)")    #textvariable=height
entryH.place(in_=entryW,relx=0, rely=1, y=30)

labelW = tbs.Label(root,text="Weight(kg)")
labelW.place(in_=entryW, relx=0,rely=0, x=-85, y=3)

labelH = tbs.Label(root, text="Height(cm)")
labelH.place(in_=entryH, relx=0,rely=0, x=-85, y=3)

button = tbs.Button(root,command=bmiFunc, text="Calculate BMI")
button.place(in_=entryH, relx=0, rely=0, x=20, y=50)

clearButton = tbs.Button(root,command=clear, text="Clear Screen")
clearButton.place(in_=button, relx=0.05, rely=0, y=50)



image = Image.open("a.jpg") #839x95
image = image.resize((629,71), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
imageLabel = tbs.Label(root, image=image )
imageLabel.place(in_=clearButton,relx=0, rely=0.5, x=-260, y=50)

root.mainloop()