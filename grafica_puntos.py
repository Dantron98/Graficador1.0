import os
import pandas as pd
import matplotlib.pyplot as plt
from ColumnVerifi_DF import column_verification
from Titulo import make_title
make_title()
path = input('Path of the file: ')
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

eje = input('What is the x axe? ')
column_verification(file, eje, 'x ')
ejex = eje
eje = input('What is the y axe? ')
column_verification(file, eje, 'y ')
ejey = eje
x = file[ejex]
y = file[ejey]
plt.figure()
figtitle = input('Title of the graphic ')
datlabel = input('Label of the plot ')
plt.title(figtitle)
plt.plot(x, y, 'ro', alpha=0.55, label=datlabel)
plt.grid(True)
xtitle = input('xs title ')
plt.xlabel(xtitle)
ytitle = input('ys title ')
plt.ylabel(ytitle)
namefig = input('Name of the graphic ')
plt.legend()
plt.savefig(namefig+'.png')
plt.show()
