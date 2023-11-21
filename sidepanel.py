import customtkinter as ctk
from settings import *
from PIL import Image

class SidePanel(ctk.CTkFrame):
    def __init__(self,parent, set_style, update_map):
        super().__init__(parent,fg_color=SIDE_PANEL_BG)
        self.grid(row=0, column=0, sticky="nsew")

        ViewButtons(self, set_style)
        self.history_frame = HistoryFrame(self, update_map)

class HistoryFrame(ctk.CTkScrollableFrame):
    def __init__(self,parent,update_map):
        super().__init__(parent)
        self.pack(expand=True,fill="both",padx=5,pady=5)
        self.font = ctk.CTkFont(family=TEXT_FONT,size=TEXT_SIZE)
        self.update_map = update_map
    
    def add_location_entry(self, location):
        HistoryItem(self,location, self.font, self.update_map)

class HistoryItem(ctk.CTkFrame):
    def __init__(self,parent,location, font, update_map):
        super().__init__(parent)
        self.pack(fill="x")

        self.address = location.address
        town = self.address.split(",")[0]
        country = self.address.split(",")[-1]
        if town == country:
            address_string = town
        else:
            address_string = f"{town}, {country}"

        ctk.CTkButton(self,text=address_string,
                      font=font,anchor="w",
                      fg_color="transparent",
                      hover_color=HISTORY_HOVER_COLOR,
                      command=lambda: update_map(self.address),
                      text_color=TEXT_COLOR).pack(side="left")
        ctk.CTkButton(self,
                      text="x",
                      font=font,
                      anchor="e",
                      hover_color=HISTORY_HOVER_COLOR,
                      text_color=TEXT_COLOR,
                      width=10,
                      command=lambda:self.pack_forget(),
                      fg_color="transparent").pack(side="right")

class ViewButtons(ctk.CTkFrame):
    def __init__(self,parent, set_style):
        super().__init__(parent,fg_color="transparent")
        self.pack(side="bottom",fill="both",padx=5,pady=5)

        self.rowconfigure(0,weight=1)
        self.columnconfigure((0,1,2), weight=1, uniform="a")

        map_image = ctk.CTkImage(dark_image=Image.open(map_image_path),light_image=Image.open(map_image_path))
        terrain_image = ctk.CTkImage(dark_image=Image.open(terrain_image_path),light_image=Image.open(terrain_image_path))
        paint_image = ctk.CTkImage(dark_image=Image.open(paint_image_path),light_image=Image.open(paint_image_path))

        ctk.CTkButton(self,text="",image=map_image,command=lambda: set_style("map"),fg_color=BUTTON_COLOR,hover_color=BUTTON_HOVER_COLOR).grid(row=0,column=0,sticky="w")
        ctk.CTkButton(self,text="",image=terrain_image,command=lambda: set_style("terrain"),fg_color=BUTTON_COLOR,hover_color=BUTTON_HOVER_COLOR).grid(row=0,column=1)
        ctk.CTkButton(self,text="",image=paint_image,command=lambda: set_style("paint"),fg_color=BUTTON_COLOR,hover_color=BUTTON_HOVER_COLOR).grid(row=0,column=2,sticky="e")
