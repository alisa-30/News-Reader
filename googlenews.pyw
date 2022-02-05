import tkinter as tk
from PIL import ImageTk,Image

w=tk.Tk()
w.title("MY NEWS WINDOW")
C = tk.Canvas(w,height=10,width=10)
filename = ImageTk.PhotoImage(Image.open(r'ne.png'))
background_label = tk.Label(w,image=filename )
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack(side="bottom",)
w.geometry("1000x1000")
i1=tk.StringVar()
i2=tk.StringVar()
i1.set("ENTER NEWS TOPIC")
i2.set("PASTE THE LINK HERE TO GO THE NEWS PAGE")
tk.Label(w,text="LATEST NEWS",font=("Forte", 30),foreground='red').pack(pady=10)
entry1=tk.Entry(w,textvariable=i1,borderwidth=3,relief="sunken")
entry1.pack(ipadx=120,ipady=10,padx=0,pady=30)
def news():
     from GoogleNews import GoogleNews
     u=i1.get()
     if u=="":
         from tkinter import messagebox
         messagebox.showerror("ERROR", "BLANK INPUT")
     f=open("googlenews1.txt","w")
     f.truncate(0)
     googlenews =GoogleNews(encode='utf-8')
     googlenews.search(u)
     result=googlenews.result()
     for x in result:
         a="_"*120
         b="Title--"
         c=x['title']
         d="Date/Time--"
         e=x['date']
         f1="Description--"
         g=x['desc']
         
         h="Link--"
         i=x['link']
         f.write(a)
         f.write("\n")
         f.write(b)
         f.write(c)
         f.write("\n")
         f.write(d)
         f.write(e)
         f.write("\n")
         f.write(f1)
         f.write(g)
         f.write("\n")
         f.write(h)
         f.write(i)
         f.write("\n")
     f.close()
def reload():
    my_text.configure(state='normal')
    my_text.delete("1.0","end")
    file=open("googlenews1.txt","r+")
    stuff=file.read()
    my_text.insert(tk.END,stuff)
    my_text.configure(state="disabled")
    file.close()
    

def link():
    r=i2.get()
    import webbrowser
    webbrowser.open(r)


te=tk.Button(w,text="ENTER",command=news,foreground ="black",background='pink',relief="sunken",borderwidth=4,font = ("Times New Roman", 15,'bold'))
te1=tk.Button(w,text="TAP TO READ THE NEWS",command=reload,foreground ="black",background='pink',relief="sunken",borderwidth=4,font = ("Times New Roman", 15,'bold'))
te.pack(pady=10)
te1.pack()
tk.Button(w,text="Click",command=link,foreground ="black",background='pink',relief="sunken",borderwidth=4,font = ("Times New Roman", 15,'bold')).pack(side="bottom")
entry=tk.Entry(w,textvariable=i2,borderwidth=3,relief="sunken")
entry.pack(ipadx=150,ipady=5,padx=100,pady=20,side="bottom")
my_text=tk.Text(w,width=250,height=50,font=("Times New Roman", 15))
my_text.pack(pady=20,fill="both")
my_text.insert(tk.END,"NEWS...WILL APPEAR HERE")
my_text.configure(state="disabled")


w.mainloop()
