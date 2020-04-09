import tkinter as tk
import pafy


def clicked():
    url=url_bar.get()
    video=pafy.new(url)
    best=video.getbest()
    filename = best.download()
    
window=tk.Tk()
window.geometry('300x300')
window.title("YouTube Downloader")
url_bar=tk.Entry(window, width=50)
url_bar.grid(column=2,row=1)
btn = tk.Button(window, text="Download", command=clicked)
btn.grid(column=2, row=2)


window.mainloop()
