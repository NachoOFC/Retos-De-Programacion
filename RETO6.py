#*Difícil
#6 ASPECT RATIO DE UNA IMAGEN
""""
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
"""
#! reto pendiente

import wget
from PIL import Image


def aspect_ratio(url):
    file_name = wget.download(url)
    print('Image Successfully Downloaded: ', file_name)

    img = Image.open(file_name)
    ancho , alto = img.size



    aspect_ratio = ancho/alto
    return print(aspect_ratio)


url = input('ingresa url imagen (string):')
aspect_ratio(url)