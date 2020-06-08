import requests,bs4
from tkinter import *
window=Tk()
window.title("covid19:india")
window.geometry('300x600')
window.config(bg="black")
i=1
def search():
 try:    
  url='https://www.worldometers.info/coronavirus/country/'
  c_name=n_entry.get()
  i=1
  if c_name=='total':
     res=requests.get('https://www.worldometers.info/coronavirus/')
     res.raise_for_status()
  else:

   res=requests.get(url+c_name+'/')
  soup=bs4.BeautifulSoup(res.text,'html.parser')
  cases=soup.find_all("div",class_="maincounter-number")
  dcases=soup.find_all("h1")
  for cases in cases:
   if(i==1):
       comm=c_name+'---------->'+'total'
   elif(i==2):
       comm='deaths'
   else:
       comm='recovered'
   i+=1
   t=comm+cases.get_text()
   b=Label(window,text=t)
   b.config(font=20,fg="green",bg='cyan',width=20,relief=RAISED)
   b.grid()
  vari=StringVar()
  line=Message(window,textvariable=vari,width=300)
  vari.set("--------------")
  line.config(bg='blue',font=20)
  line.grid()
 except:
   var=StringVar()
   w=Message(window,textvariable=var,relief=RAISED,width=100)
   var.set("ERROR!")
   w.config(fg='red',bg='blue',font=20)
   w.grid()
n=Label(window,text="ENTER COUNTRY NAME:")
n.config(font=20)
n.grid()
m=StringVar()
n_entry=Entry(window,textvariable=m,width=50)
n_entry.grid()
button=Button(window,text="SEARCH",bg="red",width='15',command=search)
button.grid()
a=Label(window,text="total cases:")
a.config(font=20)
a.grid()
window.mainloop()

