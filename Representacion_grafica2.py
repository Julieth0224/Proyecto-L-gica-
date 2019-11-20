import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage


def visualizacion(x,y):

    fig, cuad = plt.subplots()
    cuad.get_xaxis().set_visible(True)
    cuad.get_yaxis().set_visible(True)

    archivo_imagen = plt.imread("circle.png", format="png")
    circulo = OffsetImage(archivo_imagen, zoom = 0.206)
    circulo.image.axes = cuad

    archivo_imagen = plt.imread("valeria.png", format="png")
    imagen0 = OffsetImage(archivo_imagen, zoom = 0.08)
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
    direcciones[1] = [0.5, 0.9]#valeria


    direcciones[3] = [0.18, 0.765]#angel
    direcciones[4] = [0.3, 0.765]#cristian

    direcciones[5] = [0.12, 0.695]#laura
    direcciones[6] = [0.23, 0.695]#luisa
    direcciones[29] = [0.35, 0.695]#manuela

    direcciones[7] = [0.09, 0.625]#martin
    direcciones[8] = [0.2, 0.625]#tomas
    direcciones[9] = [0.29, 0.625]#Sara
    direcciones[10] = [0.4, 0.625]#sebastian

    direcciones[11] = [0.07, 0.555]#sergio
    direcciones[12] = [0.16, 0.555]#daniel
    direcciones[13] = [0.25, 0.555]#felipe
    direcciones[14] = [0.35, 0.555]#juliana
    direcciones[28] = [0.448, 0.555]#luis

    direcciones[15] = [0.07, 0.485]#paula
    direcciones[16] = [0.19, 0.485]#santiago
    direcciones[17] = [0.31, 0.485]#salome
    direcciones[18] = [0.42, 0.485]#natalia

    direcciones[19] = [0.09, 0.415]#nicolas
    direcciones[20] = [0.2, 0.415]#sofia
    direcciones[21] = [0.31, 0.415]#lorena
    direcciones[30] = [0.42, 0.415]#miguel

    direcciones[23] = [0.12, 0.345]#andres
    direcciones[24] = [0.22, 0.345]#carlos
    direcciones[25] = [0.32, 0.345]#david
    direcciones[22] = [0.4, 0.345]#ana

    direcciones[26] = [0.18, 0.275]#julieta
    direcciones[27] = [0.3, 0.275]#katherine

    direcciones[2] = [0.25, 0.22]#alejandra


    direcciones[31] = [0.25, 0.5]#circulo
    direcciones[32] = [0.75, 0.5]#circulo

# SEGUNDO CIRCULO
    direcciones[34] = [0.68, 0.765]#angel
    direcciones[35] = [0.8, 0.765]#cristian

    direcciones[36] = [0.62, 0.695]#laura
    direcciones[37] = [0.73, 0.695]#luisa
    direcciones[60] = [0.85, 0.695]#manuela

    direcciones[38] = [0.59, 0.625]#martin
    direcciones[39] = [0.7, 0.625]#tomas
    direcciones[40] = [0.79, 0.625]#Sara
    direcciones[41] = [0.9, 0.625]#sebastian

    direcciones[42] = [0.57, 0.555]#sergio
    direcciones[43] = [0.66, 0.555]#daniel
    direcciones[44] = [0.75, 0.555]#felipe
    direcciones[45] = [0.85, 0.555]#juliana
    direcciones[59] = [0.948, 0.555]#luis

    direcciones[46] = [0.57, 0.485]#paula
    direcciones[47] = [0.69, 0.485]#santiago
    direcciones[48] = [0.81, 0.485]#salome
    direcciones[49] = [0.92, 0.485]#natalia

    direcciones[50] = [0.59, 0.415]#nicolas
    direcciones[51] = [0.7, 0.415]#sofia
    direcciones[52] = [0.81, 0.415]#lorena
    direcciones[61] = [0.92, 0.415]#miguel

    direcciones[54] = [0.62, 0.345]#andres
    direcciones[55] = [0.72, 0.345]#carlos
    direcciones[56] = [0.82, 0.345]#david
    direcciones[53] = [0.9, 0.345]#ana

    direcciones[57] = [0.68, 0.275]#julieta
    direcciones[58] = [0.8, 0.275]#katherine

    direcciones[33] = [0.75, 0.22]#alejandra

    for q in range(31,33):
        ab = AnnotationBbox(circulo, direcciones[int(q)], frameon=False)
        cuad.add_artist(ab)


    ab = AnnotationBbox(imagen0, direcciones[1], frameon=False)
    cuad.add_artist(ab)



    for l in x:
            if x[l] == 0:
                for i in range(1,30):
                    Personas= AnnotationBbox(eval("imagen" + str(i)), direcciones[i+1], frameon = False)
                    cuad.add_artist(Personas)
            elif x[l] == 1:
                for q in range(1,30):
                    Personas2= AnnotationBbox(eval("imagen" + str(q)), direcciones[q+32], frameon = False)
                    cuad.add_artist(Personas2)


    fig.savefig("result_" + str(y) + ".png" )


prueba = {'j':1, 'b':0, 'm':0, 'h':1, 's':1, 'd':1, 'c':0, 't':0, 'e':1, 'f':0,
          'a':1, 'p':0, 'l':1, 'g':1}

visualizacion(prueba,10)
