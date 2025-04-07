###########################################################
#                                                         #
#               YOUTUBE DOWNLOADER - PYTHON               #
#                                                         #
###########################################################

# IMPORT LIBRARIES #

import os
from tkinter import *           # Import the library to create the graphical interface
from tkinter import messagebox  # Import the messagebox module
from pytube import YouTube      # Import the library to download YouTube videos

# DESIGN AND OPEN WINDOW IN TKINTER #

# Create a graphical interface window
root = Tk()                                    # Create an instance of the main window
root.geometry('500x300')                       # Set the dimensions of the window (width x height)
root.resizable(0, 0)                           # Make the window non-resizable
root.title('⚡ YouTube Video Downloader ⚡')  # Assign a title to the window
root.configure(bg='#427CB5')                   # Configure the background color of the window

# Label to display the title
Label(root, text='YOUTUBE DOWNLOADER', font='Tahoma 20 bold', bg='#427CB5').place(x=80, y=30)

# StringVar variable to store the video link
link = StringVar()

# Label and entry field to paste the link
Label(root, text='Paste your link here:', font='Tahoma 13', bg='#427CB5').place(x=85, y=90) # Label
link_enter = Entry(root, width=54, textvariable=link).place(x=90, y=120)                    # Entry field

# FUNCTION DECLARATIONS #

# Function to download the video
def videoDownloader():
    messagebox.showinfo("", f"Downloading, please wait...\n\nThe process may take a few seconds, don't worry if the program window stops responding while downloading")  # Display a message in a pop-up window
    # Folder name where the videos will be saved
    folder_name = "mp4"
    # Check if the folder already exists
    if not os.path.exists(folder_name):
        # If it doesn't exist, create it
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created")
    else:
        print(f"Folder '{folder_name}' already exists")
    # Download the YouTube video
    try:
        url = YouTube(str(link.get()))  # Get the link entered by the user
        video = url.streams.get_highest_resolution()  # Select the highest available resolution
        video.download(output_path=folder_name)  # Download the video in the folder
        messagebox.showinfo("Success!", f"Video downloaded succesfully!")  # Display a success message in a pop-up window
    # If an error occurs during the download, display an error message
    except Exception as e:
        messagebox.showerror("Error", f"Error while downloading: {e}")  # Display an error message in a pop-up window
        print(f"Error downloading the video: {e}")

# Function to download the audio
def audioDownloader():
    messagebox.showinfo("", f"Downloading, please wait...\n\nThe process may take a few seconds, don't worry if the program window stops responding while downloading")  # Display a message in a pop-up window
    # Folder name where the videos will be saved
    folder_name = "mp3"
    # Check if the folder already exists
    if not os.path.exists(folder_name):
        # If it doesn't exist, create it
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created")
    else:
        print(f"Folder '{folder_name}' already exists")
    # Download the YouTube audio
    try:
        url = YouTube(str(link.get()))  # Get the link entered by the user
        # Filter the streams to get only the audio
        audio_stream = url.streams.filter(only_audio=True).first()
        # Get the file name without the extension
        file_name = audio_stream.default_filename[:-4]  # Remove the .mp4 extension
        # Download the audio with the .mp3 extension
        audio_stream.download(output_path=folder_name, filename=file_name + ".mp3") # Download the audio in the folder with the .mp3 extension
        messagebox.showinfo("Success!", f"Audio downloaded succesfully!")  # Display a success message in a pop-up window
    # If an error occurs during the download, display an error message
    except Exception as e:
        messagebox.showerror("Error", f"Error while downloading: {e}")  # Display an error message in a pop-up window
        print(f"Error downloading the audio: {e}")

# MAIN CODE #

# Buttons to start the download
Button(root, text='Download mp3', font='Tahoma 13 bold', fg='#060270', padx=2, command=audioDownloader).place(x=90, y=150)  # Download .mp3
Button(root, text='Download mp4', font='Tahoma 13 bold', fg='#060270', padx=2, command=videoDownloader).place(x=270, y=150) # Download .mp4

# Start the main loop of the graphical interface
root.mainloop() # This command keeps the window open and allows user interaction with the interface.
