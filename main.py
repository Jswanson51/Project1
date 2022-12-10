from gui import *


def main() -> None:
    """
    Main module
    :return: None
    """
    window = Tk()
    window.geometry('400x300')
    window.config(background='#838B8B')
    window.resizable(False, False)
    window.title('User Sign-in')

    widgets = GUI(window)

    window.mainloop()

if __name__ == '__main__':
    main()
