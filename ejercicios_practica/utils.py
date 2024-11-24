
'''
Archivo con utilidades para la app
---------------------------
Autor: Ing.Jesús Matías González
Version: 2.0

Descripcion:
En este programa se encuentran distitas herramientas
de ayuda para utilizar en la aplicación
'''

import io
import base64

import matplotlib
matplotlib.use('Agg')   # Para multi-thread, non-interactive backend (avoid run in main loop)
import matplotlib.pyplot as plt
# Para convertir matplotlib a imagen y luego a datos binarios
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg


def graficar(x, y):
    ''' 
        Crear el grafico que se desea mostrar en HTML
    '''
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.suptitle('Comparativa de edades', fontsize=14, c='purple')
    ax.plot(x, y)
    ax.plot(y, c='pink', marker='.')
    ax.grid(ls='dashed')
    ax.set_xlabel('PERSONAS')
    ax.set_ylabel('EDADES')
    ax.set_facecolor('whitesmoke')

    #ax.get_xaxis().set_visible(False)

    # Convertir ese grafico en una imagen para enviar por HTTP
    # y mostrar en el HTML
    image_html = io.BytesIO()
    FigureCanvas(fig).print_png(image_html)
    plt.close(fig)  # Cerramos la imagen para que no consuma memoria del sistema
    return image_html
