from tkinter import simpledialog, Tk
from playsound import playsound

can_play_sounds = False


def play_mister_zee():
    if can_play_sounds:
        playsound('shiny-objects.wav')
    else:
        print("Mister Zee requires shiny objects")


def many_shiny_objects():
    # TODO 1) Call the method above to play Mister Zee

    # TODO 2) Ask the user how many shiny objects they want
    number = simpledialog.askinteger(title='Shiny Objects', prompt="How many shiny objects do you want?")
    # TODO 3) Play the sound that many times
    for i in range (number):
        play_mister_zee()
    pass


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    many_shiny_objects()
