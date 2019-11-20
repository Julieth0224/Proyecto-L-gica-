import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage


def visualizacion(x,y):

    fig, cuad = plt.subplots()
    cuad.get_xaxis().set_visible(False)
    cuad.get_yaxis().set_visible(False)

    archivo_imagen = plt.imread("circle.png", format="png")
    circulo = OffsetImage(archivo_imagen, zoom = 0.206)
    circulo.image.axes = cuad

    archivo_imagen = plt.imread("valeria.png", format="png")
    imagenv = OffsetImage(archivo_imagen, zoom = 0.08)
    imagenv.image.axes = cuad

    archivo_imagen = plt.imread("alejandra.png", format="png")
    imagena = OffsetImage(archivo_imagen, zoom = 0.04)
    imagena.image.axes = cuad

    archivo_imagen = plt.imread("angel.png", format="png")
    imagenb = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenb.image.axes = cuad

    archivo_imagen = plt.imread("cristian.png", format="png")
    imagenc = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenc.image.axes = cuad

    archivo_imagen = plt.imread("laura.png", format="png")
    imagenl = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenl.image.axes = cuad

    archivo_imagen = plt.imread("luisa.png", format="png")
    imageng = OffsetImage(archivo_imagen, zoom = 0.04)
    imageng.image.axes = cuad

    archivo_imagen = plt.imread("martin.png", format="png")
    imagenm = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenm.image.axes = cuad

    archivo_imagen = plt.imread("tomas.png", format="png")
    imagent = OffsetImage(archivo_imagen, zoom = 0.04)
    imagent.image.axes = cuad

    archivo_imagen = plt.imread("sara.png", format="png")
    imagen1 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen1.image.axes = cuad

    archivo_imagen = plt.imread("sebastian.png", format="png")
    imagen2 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen2.image.axes = cuad

    archivo_imagen = plt.imread("sergio.png", format="png")
    imagen3 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen3.image.axes = cuad

    archivo_imagen = plt.imread("daniel.png", format="png")
    imagend = OffsetImage(archivo_imagen, zoom = 0.04)
    imagend.image.axes = cuad

    archivo_imagen = plt.imread("felipe.png", format="png")
    imagenf = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenf.image.axes = cuad

    archivo_imagen = plt.imread("juliana.png", format="png")
    imagenj = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenj.image.axes = cuad

    archivo_imagen = plt.imread("paula.png", format="png")
    imagenp = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenp.image.axes = cuad

    archivo_imagen = plt.imread("santiago.png", format="png")
    imagenh = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenh.image.axes = cuad

    archivo_imagen = plt.imread("salome.png", format="png")
    imagens = OffsetImage(archivo_imagen, zoom = 0.04)
    imagens.image.axes = cuad

    archivo_imagen = plt.imread("natalia.png", format="png")
    imagenn = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenn.image.axes = cuad

    archivo_imagen = plt.imread("nicolas.png", format="png")
    imagenz = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenz.image.axes = cuad

    archivo_imagen = plt.imread("sofia.png", format="png")
    imagen4 = OffsetImage(archivo_imagen, zoom = 0.04)
    imagen4.image.axes = cuad

    archivo_imagen = plt.imread("lorena.png", format="png")
    imagene = OffsetImage(archivo_imagen, zoom = 0.04)
    imagene.image.axes = cuad

    archivo_imagen = plt.imread("ana.png", format="png")
    imageni = OffsetImage(archivo_imagen, zoom = 0.04)
    imageni.image.axes = cuad

    archivo_imagen = plt.imread("andres.png", format="png")
    imageno = OffsetImage(archivo_imagen, zoom = 0.04)
    imageno.image.axes = cuad

    archivo_imagen = plt.imread("carlos.png", format="png")
    imagenq = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenq.image.axes = cuad

    archivo_imagen = plt.imread("david.png", format="png")
    imagenr = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenr.image.axes = cuad

    archivo_imagen = plt.imread("julieta.png", format="png")
    imagenu = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenu.image.axes = cuad

    archivo_imagen = plt.imread("katherine.png", format="png")
    imagenk = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenk.image.axes = cuad

    archivo_imagen = plt.imread("luis.png", format="png")
    imagenw = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenw.image.axes = cuad

    archivo_imagen = plt.imread("manuela.png", format="png")
    imagenx = OffsetImage(archivo_imagen, zoom = 0.04)
    imagenx.image.axes = cuad

    archivo_imagen = plt.imread("miguel.png", format="png")
    imageny = OffsetImage(archivo_imagen, zoom = 0.04)
    imageny.image.axes = cuad

    direcciones = {}
    direcciones['v'] = [0.5, 0.9]  # Valeria


    direcciones['b'] = [0.18, 0.765]  # Angel
    direcciones['c'] = [0.3, 0.765]  # Cristian

    direcciones['l'] = [0.12, 0.695]  # Laura
    direcciones['g'] = [0.23, 0.695]  # Luisa
    direcciones['x'] = [0.35, 0.695]  # Manuela

    direcciones['m'] = [0.09, 0.625]  # Martin
    direcciones['t'] = [0.2, 0.625]  # Tomas
    direcciones['1'] = [0.29, 0.625]  # Sara
    direcciones['2'] = [0.4, 0.625]  # Sebastian

    direcciones['3'] = [0.07, 0.555]  # Sergio
    direcciones['d'] = [0.16, 0.555]  # Daniel
    direcciones['f'] = [0.25, 0.555]  # Felipe
    direcciones['j'] = [0.35, 0.555]  # Juliana
    direcciones['w'] = [0.448, 0.555]  # Luis

    direcciones['p'] = [0.07, 0.485]  # Paula
    direcciones['h'] = [0.19, 0.485]  # Santiago
    direcciones['s'] = [0.31, 0.485]  # Salome
    direcciones['n'] = [0.42, 0.485]  # Natalia

    direcciones['z'] = [0.09, 0.415]  # Nicolas
    direcciones['4'] = [0.2, 0.415]  # Sofia
    direcciones['e'] = [0.31, 0.415]  # Lorena
    direcciones['y'] = [0.42, 0.415]  # Miguel

    direcciones['o'] = [0.12, 0.345]  # Andres
    direcciones['q'] = [0.22, 0.345]  # Carlos
    direcciones['r'] = [0.32, 0.345]  # David
    direcciones['i'] = [0.4, 0.345]  # Ana

    direcciones['u'] = [0.18, 0.275] # Julieta
    direcciones['k'] = [0.3, 0.275]  #  Katherine

    direcciones['a'] = [0.25, 0.22] # Alejandra


    direcciones[31] = [0.25, 0.5] # Circulo
    direcciones[32] = [0.75, 0.5] # Circulo

 #  SEGUNDO CIRCULO

    direcciones['b*'] = [0.68, 0.765] # Angel
    direcciones['c*'] = [0.8, 0.765] # Cristian

    direcciones['l*'] = [0.62, 0.695] # Laura
    direcciones['g*'] = [0.73, 0.695] # Luisa
    direcciones['x*'] = [0.85, 0.695] # Manuela

    direcciones['m*'] = [0.59, 0.625] # Martin
    direcciones['t*'] = [0.7, 0.625] # Tomas
    direcciones['1*'] = [0.79, 0.625] # Sara
    direcciones['2*'] = [0.9, 0.625] # Sebastian

    direcciones['3*'] = [0.57, 0.555] # Sergio
    direcciones['d*'] = [0.66, 0.555] # Daniel
    direcciones['f*'] = [0.75, 0.555] # Felipe
    direcciones['j*'] = [0.85, 0.555] # Juliana
    direcciones['w*'] = [0.948, 0.555] # Luis

    direcciones['p*'] = [0.57, 0.485] # Paula
    direcciones['h*'] = [0.69, 0.485] # Santiago
    direcciones['s*'] = [0.81, 0.485] # Salome
    direcciones['n*'] = [0.92, 0.485] # Natalia

    direcciones['z*'] = [0.59, 0.415] # Nicolas
    direcciones['4*'] = [0.7, 0.415] # Sofia
    direcciones['e*'] = [0.81, 0.415] # Lorena
    direcciones['y*'] = [0.92, 0.415] # Miguel

    direcciones['o*'] = [0.62, 0.345] # Andres
    direcciones['q*'] = [0.72, 0.345] # Carlos
    direcciones['r*'] = [0.82, 0.345] # David
    direcciones['i*'] = [0.9, 0.345] # Ana

    direcciones['u*'] = [0.68, 0.275] # Julieta
    direcciones['k*'] = [0.8, 0.275] # Katherine

    direcciones['a*'] = [0.75, 0.22] # Alejandra

    for q in range(31,33): # Inserta circulos
        ab = AnnotationBbox(circulo, direcciones[int(q)], frameon=False)
        cuad.add_artist(ab)


    ab = AnnotationBbox(imagenv, direcciones['v'], frameon=False) # Inserta Valeria
    cuad.add_artist(ab)


    for l in x: # Depende de el valor de x, inserta nombre correspondiente
            if x[l] == 0:
                Personas= AnnotationBbox(eval("imagen" + l), direcciones[l], frameon = False)
                cuad.add_artist(Personas)
            elif x[l] == 1:
                Personas2= AnnotationBbox(eval("imagen" + l), direcciones[l + '*'], frameon = False)
                cuad.add_artist(Personas2)


    fig.savefig("result_" + str(y) + ".png" )


prueba = {'j':1, 'b':0, 'm':0, 'h':1, 's':1, 'd':1, 'c':0, 't':0, 'e':1, 'f':0,
          'a':1, 'p':0, 'l':1, 'g':1}

visualizacion(prueba,"ok")
