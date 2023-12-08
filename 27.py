
from tkinter import * 

root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="lightblue")

label_planet = Label(root, text="Planet : ", bg="lightblue")
label_planet_name = Label(root,font=("courier",18,"bold"), bg="lightblue")
label_planet_image = Label(root,bg="gold2", highlightthickness=5, borderwidth=2,relief=SOLID)
label_planet_gravity_radius = Label(root,font=("castellar"), bg="lightblue")
label_planet_info = Label(root,font=("courier",10,"bold"), bg="lightblue", wraplength=500)

def PlanetInfo():
    print("hi")
    
btn = Button(root, text="Show Planet Info" , command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)


root.mainloop()

