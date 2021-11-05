import os
import pandas as pd
def verfy_path(path):
    while True:
        if os.path.isfile(path) == True:
            file = pd.read_csv(path)
            print('This is the correct file?')
            print(file)
            answer = input('y/n ')
            while True:
                if answer == 'y' or answer == 'n':
                    break
                else:
                    answer = input('y/n ')
            if answer == 'y':
                break
            else:
                path = input('Path of the file: ')
        else:
            print('Error, the file not exits')
            path = input('Path of the file: ')
    return(file)
