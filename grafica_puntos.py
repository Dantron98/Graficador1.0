import matplotlib.pyplot as plt
from ColumnVerifi_DF import column_verification
from Titulo import make_title
from MinCuadrados import minicua
from VerifPath import verfy_path

make_title()
path = input('Path of the file: ')
file = verfy_path(path)
eje = input('What is the x axe? ')
column_verification(file, eje, 'x ')
ejex = eje
eje = input('What is the y axe? ')
column_verification(file, eje, 'y ')
ejey = eje
x = file[ejex]
y = file[ejey]
answer = str(input('Do you want do a linear fit? (y/n) '))
if answer == 'y':
    m, b, em, eb = minicua(x, y)
    print(m, b, em, eb)
plt.figure()
figtitle = input('Title of the graphic ')
datlabel = input('Label of the plot ')
plt.title(figtitle)
plt.plot(x, y, 'ro')
plt.grid(True)
xtitle = input('xs title ')
plt.xlabel(xtitle)
ytitle = input('ys title ')
plt.ylabel(ytitle)
namefig = input('Name of the graphic ')
plt.legend()
plt.savefig(namefig+'.png')
plt.show()
