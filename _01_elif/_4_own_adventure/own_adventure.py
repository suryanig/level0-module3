from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    person = simpledialog.askinteger(title='Who do you want to be?', prompt="Do you want to be 1) normal or 2) famous.")
    if person == 1:
        age = simpledialog.askinteger(title='How old do you want to be?', prompt="Do you want to be 1) a child or 2) an adult?")
        if age == 1:
            school = simpledialog.askinteger(title='What level of school are you in?', prompt="Do you want to be im 1) elementary school, 2) middle school, or 3) high school?")
            if school == 1:
                messagebox.showinfo(message="Congratulations! You are a young child in elementary school living your best life. You enjoy the fun of being young. But careful, the good years of school are ending soon.")
            elif school == 2:
                messagebox.showinfo(message="Congratulations! You are an adolescent in the hard years of middle school. It's going roughly and good friends are hard to find, nut it will most likely get better.")
            elif school == 3:
                messagebox.showinfo(message="Congratulations! You are stressing over everything in the inferno people call high school. Luckily you have amazing friends, even though you are drowning in work.")
        elif age == 2:
            home = simpledialog.askinteger(title='Where do you want to live?', prompt="Do you want to live in 1) the city, or 2) a suburban area?")
            if home == 1:
                messagebox.showinfo(message="Congratulations! You live in the always busy city and are barely holding on. You are comfortable, but never get a minute of silence in the city that never sleeps.")
            elif home ==2:
                messagebox.showinfo(message="Congratulations! You live in a beautiful lush area where everything you need is a 10 minute drive away. It's not super busy or expensive so you live perfectly and the weather is never too hot or too cold.")
    elif person == 2:
        job = simpledialog.askinteger(title='What job do you want?', prompt="Do you want to be 1) a singer or 2) and actor?")
        if job == 1:
            type = simpledialog.askinteger(title="What type of music do you sing?", prompt="Do you want ot be 1) a pop singer, or 2) a country singer?")
            if type == 1:
                messagebox.showinfo(message="Congratulations! You are a successful singer that even Taylor Swift is jealous of.")
            elif type == 2:
                messagebox.showinfo(message="Congratulations! Because you are a country singer and no one likes that, you don't get enough money to get by.")
        elif job == 2:
            actor = simpledialog.askinteger(title='How old of an actor are you?', prompt="Do you want to be 1) a child actor, or 2) an adult actor?")
            if actor == 1:
                messagebox.showinfo(message="Congratulations! You starred in a few Disney Channel shows before growing up to be a complete weirdo. I hope you are proud of yourself.")
            elif actor == 2:
                messagebox.showinfo(message="Congratulations! You starred in the hit action + romance movie which became a hit, so you are doing very well in life.")
