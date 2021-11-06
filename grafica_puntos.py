import matplotlib.pyplot as plt
from ColumnVerifi_DF import column_verification
from Titulo import make_title
from MinCuadrados import minicua
from VerifPath import verfy_path

make_title()
path = input('Path of the file: ')
file = verfy_path(path)
eje = input('What is the x axe? ')
ejex = column_verification(file, eje, 'x ')
eje = input('What is the y axe? ')
ejey = column_verification(file, eje, 'y ')
x = file[ejex]
y = file[ejey]
answer = str(input('Do you want do a linear fit? (y/n) '))
if answer == 'y':
    m, b, em, eb = minicua(x, y)

plt.figure()
figtitle = input('Title of the graphic ')
datlabel = input('Label of the plot ')
plt.title(figtitle)
plt.plot(x, y, 'ro', label=datlabel)
mlen = str(m.round(5))
blen = str(b.round(5))
equation = str('y=' + mlen + 'x+' + blen)
plt.plot(x, x*m+b, label=equation, )
plt.grid(True)
xtitle = input('xs title ')
plt.xlabel(xtitle)
ytitle = input('ys title ')
plt.ylabel(ytitle)
namefig = input('Name of the graphic ')
plt.scatter(x[0], y[0], color='green', alpha=0.95, marker='o', s=30, label='Inicio:({},{})'.format(x[0].round(4),
                                                                                                y[0].round(4)))
plt.scatter(x[19], y[19], color='green', alpha=0.95, marker='o', s=30, label='Fin({},{})'.format(x[19].round(4),
                                                                                                y[19].round(4)))
plt.legend()
plt.savefig(namefig+'.png')
plt.show()
