import time
import tkinter as tk
from tkinter import ttk
from pytube import YouTube

# -- Screen Size -- #
SCREEN_SIZE = "320x480"

# -- Fonts -- #
TitleFont = ("JetBrains Mono", 14)
NormalFont = ("JetBrains Mono", 12)
SmallFont = ("JetBrains Mono", 10)

# -- Colors -- #
BACKGROUND_COLOR = "#1a1a19"
FOREGROUND_COLOR = "#d1d1d1"

# -Normal- #
BLACK = '#333332'
RED = '#ff968c'
GREEN = '#61957f'
YELLOW = '#ffc591'
BLUE = '#8db4d4'
MAGENTA = '#de9bc8'
CYAN = '#7bb099'
WHITE = '#d1d1d1'
BUTTON_RED = '#bd493e'
BUTTON_RED_2 = '#c75c52'

# -Bright- #
BRIGHT_BLACK = '#4c4c4b'
BRIGHT_RED = '#ffafa5'
BRIGHT_GREEN = '#7aae98'
BRIGHT_YELLOW = '#ffdeaa'
BRIGHT_BLUE = '#a6cded'
BRIGHT_MAGENTA = '#f7b4e1'
BRIGHT_CYAN = '#94c9b2'
BRIGHT_WHITE = '#eaeaea'
BRIGHTBRIGHT_WHITE = '#f9f9f9'

button_style = {
    'font': NormalFont,
    'background': BUTTON_RED,
    'foreground': BRIGHTBRIGHT_WHITE,
    'activebackground': RED,
    'highlightthickness': 0,
    'border': 0,
    'width': 10
}


# --- GUI Class --- #
class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(SCREEN_SIZE)
        self.root.title("vegy's YT Downloader")
        self.root.resizable(False, False)
        self.root.configure(background=BACKGROUND_COLOR)
        # -- Title Text -- #
        self.title_label = tk.Label(self.root, text="vegy's YT Downloader", font=TitleFont,
                                    foreground=BRIGHTBRIGHT_WHITE, background=BACKGROUND_COLOR)
        self.title_label.pack(padx=4, pady=4, side=tk.TOP)

        # -- Link Text --#
        self.link_label = tk.Label(self.root, text="Paste your Link:", font=SmallFont,
                                   foreground=WHITE, background=BACKGROUND_COLOR)
        self.link_label.pack(padx=6, pady=2, anchor=tk.W)

        # -- Text Box -- #
        self.LinkTBox = tk.Text(self.root, height=2, font=NormalFont, background=BLACK,
                                foreground=BRIGHTBRIGHT_WHITE, border=0, highlightthickness=0)
        self.LinkTBox.pack(padx=10)

        self.LabelMessage = tk.Label(self.root, text="", font=SmallFont,
                                     foreground=WHITE, background=BACKGROUND_COLOR)

        # -- Buttons Frame -- #
        self.buttons_frame = tk.Frame(self.root, background=BACKGROUND_COLOR)
        self.buttons_frame.pack(pady=15, side=tk.BOTTOM)

        # -- Start Button -- #
        self.StartButton = tk.Button(self.buttons_frame, text="Download", command=self.StartD, **button_style)
        self.StartButton.pack(side=tk.LEFT, padx=5)
        self.StartButton.bind("<Enter>", self.change_color_on_hover)
        self.StartButton.bind("<Leave>", self.restore_color_on_hover)

        # -- Close Button -- #
        self.CloseButton = tk.Button(self.buttons_frame, text="Exit", command=self.CloseD, **button_style)
        self.CloseButton.pack(side=tk.RIGHT, padx=5)
        self.CloseButton.bind("<Enter>", self.change_color_on_hover)
        self.CloseButton.bind("<Leave>", self.restore_color_on_hover)

        # -- MainLoop -- #
        self.root.mainloop()

    def change_color_on_hover(self, event):
        event.widget.config(background=BUTTON_RED_2, foreground=BLACK)

    def restore_color_on_hover(self, event):
        event.widget.config(background=BUTTON_RED, foreground=BRIGHTBRIGHT_WHITE)

    def StartD(self):
        if "https://www.youtube.com/watch?v=" or "https://youtu.be/" in self.LinkTBox.get("1.0", 'end-1c'):
            self.LabelMessage.config(text="Downloading...")
            self.LabelMessage.pack(padx=5, pady=5)
            yt = YouTube(str(self.LinkTBox.get("1.0", 'end-1c')))
            video = yt.streams.get_highest_resolution()
            video.download()

            self.LabelMessage.config(text="Download Successful")

        else:
            self.LabelMessage.config(text="False Input")
            self.LabelMessage.pack(padx=5, pady=5)

    def CloseD(self):
        self.root.quit()


MyGUI()
quit()
