from termcolor import colored
from pyfiglet import Figlet
def make_title():
    title = Figlet(font='standard')
    print(colored(title.renderText('DanTron'), 'green'))
    return(title)