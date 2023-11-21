import customtkinter as ctk
from settings import *
import tkintermapview

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.geometry("1200x800+100+50")
        self.minsize(800,600)
        self.title("Map")
        self.iconbitmap("map.ico")
        
        self.rowconfigure(0, weight=1, uniform="a")
        self.columnconfigure(0, weight=2, uniform="a")
        self.columnconfigure(1, weight=8, uniform="a")

        self.map_widget = MapWidget(self)

        self.mainloop()

class MapWidget(tkintermapview.TkinterMapView):
    def __init__(self,parent):
        super().__init__(parent)
        self.grid(row=0,column=1,sticky="nsew")

        self.set_tile_server(TERRAIN_URL)

App()