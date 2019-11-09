import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage


def visualizacion(y):

    fig, cuad = plt.subplots()
    cuad.get_xaxis().set_visible(True)
    cuad.get_yaxis().set_visible(True)

    archivo_imagen = plt.imread("circle.png", format="png")
    circulo = OffsetImage(archivo_imagen, zoom = 0.15)
    circulo.image.axes = cuad

    archivo_imagen = plt.imread("valeria.png", format="png")
    imagen0 = OffsetImage(archivo_imagen, zoom = 0.07)
    imagen0.image.axes = cuad

    archivo_imagen = plt.imread("alejandra.png", format="png")
    imagen1 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen1.image.axes = cuad

    archivo_imagen = plt.imread("angel.png", format="png")
    imagen2 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen2.image.axes = cuad

    archivo_imagen = plt.imread("cristian.png", format="png")
    imagen3 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen3.image.axes = cuad

    archivo_imagen = plt.imread("laura.png", format="png")
    imagen4 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen4.image.axes = cuad

    archivo_imagen = plt.imread("luisa.png", format="png")
    imagen5 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen5.image.axes = cuad

    archivo_imagen = plt.imread("martin.png", format="png")
    imagen6 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen6.image.axes = cuad

    archivo_imagen = plt.imread("tomas.png", format="png")
    imagen7 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen7.image.axes = cuad

    archivo_imagen = plt.imread("sara.png", format="png")
    imagen8 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen8.image.axes = cuad

    archivo_imagen = plt.imread("sebastian.png", format="png")
    imagen9 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen9.image.axes = cuad

    archivo_imagen = plt.imread("sergio.png", format="png")
    imagen10 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen10.image.axes = cuad

    archivo_imagen = plt.imread("daniel.png", format="png")
    imagen11 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen11.image.axes = cuad

    archivo_imagen = plt.imread("felipe.png", format="png")
    imagen12 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen12.image.axes = cuad

    archivo_imagen = plt.imread("juliana.png", format="png")
    imagen13 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen13.image.axes = cuad

    archivo_imagen = plt.imread("paula.png", format="png")
    imagen14 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen14.image.axes = cuad

    archivo_imagen = plt.imread("santiago.png", format="png")
    imagen15 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen15.image.axes = cuad

    archivo_imagen = plt.imread("salome.png", format="png")
    imagen16 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen16.image.axes = cuad

    archivo_imagen = plt.imread("natalia.png", format="png")
    imagen17 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen17.image.axes = cuad

    archivo_imagen = plt.imread("nicolas.png", format="png")
    imagen18 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen18.image.axes = cuad

    archivo_imagen = plt.imread("sofia.png", format="png")
    imagen19 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen19.image.axes = cuad

    archivo_imagen = plt.imread("lorena.png", format="png")
    imagen20 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen20.image.axes = cuad

    archivo_imagen = plt.imread("ana.png", format="png")
    imagen21 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen21.image.axes = cuad

    archivo_imagen = plt.imread("andres.png", format="png")
    imagen22 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen22.image.axes = cuad

    archivo_imagen = plt.imread("carlos.png", format="png")
    imagen23 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen23.image.axes = cuad

    archivo_imagen = plt.imread("david.png", format="png")
    imagen24 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen24.image.axes = cuad

    archivo_imagen = plt.imread("julieta.png", format="png")
    imagen25 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen25.image.axes = cuad

    archivo_imagen = plt.imread("katherine.png", format="png")
    imagen26 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen26.image.axes = cuad

    archivo_imagen = plt.imread("luis.png", format="png")
    imagen27 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen27.image.axes = cuad

    archivo_imagen = plt.imread("manuela.png", format="png")
    imagen28 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen28.image.axes = cuad

    archivo_imagen = plt.imread("miguel.png", format="png")
    imagen29 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen29.image.axes = cuad


    direcciones = {}
    direcciones[1] = [0.5, 0.9]

    direcciones[2] = [0.2, 0.66]
    direcciones[3] = [0.1, 0.812]
    direcciones[4] = [0.2, 0.86]
    direcciones[5] = [0.28, 0.812]
    direcciones[6] = [0.2, 0.76]
    direcciones[7] = [0.1, 0.712]
    direcciones[8] = [0.3, 0.712]
    direcciones[9] = [0.1, 0.612]
    direcciones[10] = [0.28, 0.612]
    direcciones[11] = [0.2, 0.56]

    direcciones[12] = [0.5, 0.46]
    direcciones[13] = [0.4, 0.412]
    direcciones[14] = [0.58, 0.412]
    direcciones[15] = [0.5, 0.36]
    direcciones[16] = [0.4, 0.312]
    direcciones[17] = [0.6, 0.312]
    direcciones[18] = [0.5, 0.26]
    direcciones[19] = [0.4, 0.212]
    direcciones[20] = [0.6, 0.212]

    direcciones[21] = [0.8, 0.86]
    direcciones[22] = [0.7, 0.812]
    direcciones[23] = [0.88, 0.812]
    direcciones[24] = [0.8, 0.76]
    direcciones[25] = [0.7, 0.712]
    direcciones[26] = [0.88, 0.712]
    direcciones[27] = [0.8, 0.66]
    direcciones[28] = [0.7, 0.612]
    direcciones[29] = [0.88, 0.612]
    direcciones[30] = [0.8, 0.56]

    direcciones[31] = [0.2, 0.7]
    direcciones[32] = [0.5, 0.3]
    direcciones[33] = [0.8, 0.7]



    for q in range(31,34):
        ab = AnnotationBbox(circulo, direcciones[int(q)], frameon=False)
        cuad.add_artist(ab)


    ab = AnnotationBbox(imagen0, direcciones[1], frameon=False)
    cuad.add_artist(ab)

    for i in range(1,30):
        Personas= AnnotationBbox(eval("imagen" + str(i)), direcciones[i+1], frameon = False)
        cuad.add_artist(Personas)


    fig.savefig("result_" + str(y) + ".png" )


#prueba = {1:1, 2:1, }

visualizacion(2)
