from tkinter import *
import requests
from urllib.request import urlopen
import io
from PIL import ImageTk,Image
import webbrowser

class NewsApp:

    def __init__(self):
        #fetch data
        self.data=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=dfda0e47e9664adf8cad493e6618e43b').json()
        #load basic gui
        self.load_gui()
        #load first news item
        self.load_news_item(0)

    def load_gui(self):
        self.root=Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.configure(background='#f5b5e9')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):
        #clear the screen for news item
        self.clear()

        try:
            img_url=self.data['articles'][index]['urlToImage']
            raw_data=urlopen(img_url).read()
            im=Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo=ImageTk.PhotoImage(im)

        except:
            image_url = 'https://cdn-60c35131c1ac185aa47dd21e.closte.com//wp-content/uploads/2020/06/cannot-load-photo.png'
            raw_data = urlopen(image_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        im_label=Label(self.root,image=photo)
        im_label.pack()

        heading=Label(self.root,text=self.data['articles'][index]['title'],bg='#f5b5e9',fg='white',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('Georgia',17))

        details=Label(self.root,text=self.data['articles'][index]['description'],fg='white',bg='#f5b5e9',wraplength=350,justify='center')
        details.pack(pady=(2,10))
        details.config(font=('Georgia',10))

        frame=Frame(self.root,bg='#f5b5e9')
        frame.pack(expand=True,fill=BOTH)

        if index!=0:
            prev=Button(frame,text='Previous',width=16,height=3,bg='#70045c',fg='white',command=lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read_more=Button(frame,text='Read_More',width=16,height=3,bg='#70045c',fg='white',command=lambda :self.open_link(self.data['articles'][index]['url']))
        read_more.pack(side=LEFT)

        if index<(len(self.data['articles'])-1):
            next=Button(frame,text='Next',width=16,height=3,bg='#70045c',fg='white',command=lambda :self.load_news_item(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)

app=NewsApp()



