from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()
    happy = simpledialog.askstring(title='Happy', prompt="Are you happy?")
    if happy == "yes":
        messagebox.showinfo(message="Keep doing whatever you're doing?")
    elif happy == "no":
        happy2 = simpledialog.askstring(title = 'Happy2',prompt="Do you want to be happpy?")
    if happy2 == "yes":
        messagebox.showinfo(message="Change something")
    elif happy2 == "no":
        messagebox.showinfo(message="Keep doing whatever you're doing?")
    pass
