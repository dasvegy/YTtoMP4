import os
import time
import tkinter as tk
import dotenv
import tkinter.filedialog
from tkinter import ttk
from pytube import YouTube

# -- Screen Size -- #
SCREEN_SIZE = "320x480"

# -- Fonts -- #
TitleFont = ("JetBrains Mono", 14)
NormalFont = ("JetBrains Mono", 12)
SmallFont = ("JetBrains Mono", 10)

# -- Variables -- #
format = "MP4"
color_theme = "Red"

# -- Colors -- #
BACKGROUND_COLOR = "#1a1a19"
FOREGROUND_COLOR = "#d1d1d1"

# -Normal- #
BLACK = '#333332'
RED = '#ff968c'
WHITE = '#d1d1d1'
BUTTON_RED = '#bd493e'
BUTTON_RED_2 = '#c75c52'
BUTTON_BLACK = '#000000'

# -Bright- #
BRIGHT_BLACK = '#4c4c4b'
BRIGHT_RED = '#ffafa5'
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

button_format_style = {
    'font': NormalFont,
    'background': BUTTON_RED,
    'foreground': BRIGHTBRIGHT_WHITE,
    'activebackground': RED,
    'highlightthickness': 0,
    'border': 0,
    'width': 5
}

button_style_large = {
    'font': NormalFont,
    'background': BUTTON_RED,
    'foreground': BRIGHTBRIGHT_WHITE,
    'activebackground': RED,
    'highlightthickness': 0,
    'border': 0,
    'width': 20
}

dotenv.load_dotenv()
current_dir = os.getenv("DIR")


# --- GUI Class --- #
class MyGUI:
    def update_format_label(self):
        self.format_label.config(text=f"Format: {format}")

    def mp4_button_pressed(self):
        global format
        format = "MP4"
        self.update_format_label()

    def mp3_button_pressed(self):
        global format
        format = "MP3"
        self.update_format_label()

    def change_theme_spezi(self):
        global color_theme
        color_theme = "Spezi"

    def wav_button_pressed(self):
        global format
        format = "WAV"
        self.update_format_label()

    def change_color_on_hover(self, event):
        event.widget.config(background=BUTTON_RED_2, foreground=BUTTON_BLACK)

    def restore_color_on_hover(self, event):
        event.widget.config(background=BUTTON_RED, foreground=BRIGHTBRIGHT_WHITE)

    def download(self):
        self.LabelMessage.config(text="Downloading...")
        if format == "MP4":
            self.LabelMessage.pack(padx=5, pady=5)
            yt = YouTube(str(self.LinkTBox.get("1.0", 'end-1c')))
            video = yt.streams.get_highest_resolution()
            video.download(output_path=current_dir)
        elif format == "MP3":
            self.LabelMessage.pack(padx=5, pady=5)
            yt = YouTube(str(self.LinkTBox.get("1.0", 'end-1c')))
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(filename=f"{yt.title}.mp3", output_path=current_dir)
        elif format == "WAV":
            self.LabelMessage.pack(padx=5, pady=5)
            yt = YouTube(str(self.LinkTBox.get("1.0", 'end-1c')))
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(filename=f"{yt.title}.wav", output_path=current_dir)
        else:
            pass

        self.LabelMessage.config(text="Download Successful")

    def secret_settings(self):
        self.settingsroot = tk.Tk()
        self.settingsroot.geometry("250x350")
        self.settingsroot.title("Settings")
        self.settingsroot.resizable(False, False)
        self.settingsroot.configure(background=BACKGROUND_COLOR)

        self.settingslabel = tk.Label(self.settingsroot, text="Settings", font=TitleFont,
                                      foreground=BRIGHTBRIGHT_WHITE, background=BACKGROUND_COLOR)
        self.settingslabel.pack(padx=4, pady=4, side=tk.TOP)

        self.dir_btn = tk.Button(self.settingsroot, text="Select Directory", **button_style_large)
        self.dir_btn.pack(side=tk.TOP, padx=5)
        self.dir_btn.bind("<Enter>", self.change_color_on_hover)
        self.dir_btn.bind("<Leave>", self.restore_color_on_hover)

    def StartD(self):
        # -- Checks if a YouTube Link is inserted and then Starts the Download or shows Error -- #
        if "https://www.youtube.com/watch?v=" in self.LinkTBox.get("1.0", 'end-1c'):
            self.download()
        elif "https://youtu.be/" in self.LinkTBox.get("1.0", 'end-1c'):
            self.download()
        elif "Settings" in self.LinkTBox.get("1.0", 'end-1c'):
            self.secret_settings()
        # -- Error -- #
        else:
            self.LabelMessage.config(text="False Input")
            self.LabelMessage.pack(padx=5, pady=5)

    def CloseD(self):
        self.root.quit()

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(SCREEN_SIZE)
        self.root.title("vegy's YT Downloader")
        self.root.resizable(False, False)
        self.root.configure(background=BACKGROUND_COLOR)
        self.icon = tk.PhotoImage(file="assets/img/icon.png")
        self.root.iconphoto(False, self.icon)

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

        # -- Format Buttons -- #
        self.format_buttons_frame = tk.Frame(self.root, background=BACKGROUND_COLOR)
        self.format_buttons_frame.pack(pady=10, side=tk.TOP)

        self.mp4_button = tk.Button(self.format_buttons_frame, text="MP4",
                                    command=self.mp4_button_pressed, **button_format_style)
        self.mp4_button.pack(side=tk.LEFT, padx=5)
        self.mp4_button.bind("<Enter>", self.change_color_on_hover)
        self.mp4_button.bind("<Leave>", self.restore_color_on_hover)

        self.wav_button = tk.Button(self.format_buttons_frame, text="WAV",
                                    command=self.wav_button_pressed, **button_format_style)
        self.wav_button.pack(side=tk.RIGHT, padx=5)
        self.wav_button.bind("<Enter>", self.change_color_on_hover)
        self.wav_button.bind("<Leave>", self.restore_color_on_hover)

        self.mp3_button = tk.Button(self.format_buttons_frame, text="MP3",
                                    command=self.mp3_button_pressed, **button_format_style)
        self.mp3_button.pack(side=tk.RIGHT, padx=5)
        self.mp3_button.bind("<Enter>", self.change_color_on_hover)
        self.mp3_button.bind("<Leave>", self.restore_color_on_hover)

        self.format_label = tk.Label(self.root, text=f"Format: {format}", font=SmallFont,
                                     foreground=WHITE, background=BACKGROUND_COLOR)
        self.format_label.pack(padx=10)

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


MyGUI()
