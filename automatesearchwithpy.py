import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

#Define the main window

root=tk.Tk()
root.title("Search Automation")

#Adding a background color

root.configure(bg='brown')

#Define the function to automate youtube search

def search_youtube():
    query=entry.get()
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
#Define the function to automate goggle search

def search_google():
    query=entry.get()
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    
#Define the function to automate instagram search

def search_instagram():

    Username=entry.get().replace('@',"")
    url=f"www.instagram.com/{Username}/"
    webbrowser.open(url)
    
#Define the function to automate amazon search

def search_amazon():

    productname=entry.get()
    url=f"https://www.amazon.in/s?k={productname}"
    webbrowser.open(url)
    
#Define the function to automate leetcode search

def search_leetcode():

    problemname=entry.get()
    url=f"https://leetcode.com/problemset/?search={problemname}&page=1"
    webbrowser.open(url)    
    
#create input field, Labels, and buttons

Label(root, text="Enter your search query:").pack(pady=10)
entry=Entry(root, width=50)
entry.pack(pady=10)
Button(root, text="Search on Youtube", command=search_youtube).pack(pady=5)
Button(root, text="Search on Google", command=search_google).pack(pady=5)
Button(root, text="Search on Instagram", command=search_instagram).pack(pady=5)
Button(root, text="Search on Amazon", command=search_amazon).pack(pady=5)
Button(root, text="Search on Leetcode", command=search_leetcode).pack(pady=5)

#Run the GUI event loop

root.mainloop()