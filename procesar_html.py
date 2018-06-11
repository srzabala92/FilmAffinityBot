from bs4 import BeautifulSoup
import urllib3
import urllib.parse
import pelicula
from pelicula import Pelicula


def busqueda (cadena):
    dir_html = "https://www.filmaffinity.com/es/search.php?stext=" + urllib.parse.quote_plus(cadena)
    #urllib.parse.quote_plus(dir_html)
    contenido_html = urllib3.connection_from_url(dir_html)
    data = contenido_html.urlopen('GET',dir_html)
    bs = BeautifulSoup(data.data.decode('utf-8'), 'html.parser')
    ##print(bs.prettify())
    return listar_pelis2(bs)#Devuelve lista de peliculas
    '''string = ""
    for peli in listar_pelis(bs.prettify(),bs):
        string = string + Pelicula.datos_peli(peli)
    return string'''
#Función que lista las pelis resultantes de una búsqueda (si las hay)
'''def listar_pelis(data,bs):
    lista_peliculas = []
    for busqueda in bs('div', {'id': 'title-result'}):
        i = 0#Contador de años
        years_array = busqueda('div', {'class': 'ye-w'})#array con los años ordenados de cada película
        for div in busqueda('div',{'class':'movie-card movie-card-1'}):#Obtenemos todas las películas de la búsqueda
            year = years_array[i].string#Obtenemos el año
            i = i + 1#Índice para los años
            a = div('a')
            titulo = a[0]['title']
            #print(titulo)
            for img in a[0]('img'):#Para cada película sacar la imagen (campo 'a')
                ruta = img['src']
                #print (ruta)
            for nota in div('div',{'class':'avgrat-box'}):#Para cada película sacamos la nota
                #print(nota.string)
                calif = nota.string
            #Creamos un objeto de la clase 'Película'
            #peli = Pelicula(titulo,ruta,nota.string,year)
            lista_peliculas.append(Pelicula(titulo,ruta,calif,year))
            #print ("------------------------------------- \n")
    return lista_peliculas
   ##print(bs('div',{'class':'movie-card movie-card-1'}))
'''
#Obtener las url de todas las peliculas cuyas palabras clave han sido buscadas
def listar_pelis2(bs):
    lista_peliculas = []
    url = bs('link',{'rel':'canonical'})[0]['href']
    if "www.filmaffinity.com/es/search.php?stext" in url:
        for busqueda in bs('div', {'class': 'main-search-wrapper'}):
            for div in busqueda('div',{'class':'mc-title'}):
                a = div('a')
                dir = a[0]['href']
                dir_html = "https://www.filmaffinity.com"+dir
                # urllib.parse.quote_plus(dir_html)
                contenido_html = urllib3.connection_from_url(dir_html)
                data = contenido_html.urlopen('GET', dir_html)
                bs = BeautifulSoup(data.data.decode('utf-8'), 'html.parser')
                lista_peliculas.append(obtener_info(bs,url))
    else: #Probar 1 resultado
        lista_peliculas.append(obtener_info(bs, url))
    return lista_peliculas
#Obtener toda la información de una pelicula dada su url, devuelve un objeto película
def obtener_info(bs,url):
    titulo = "Titulo"
    year = "1900"
    rating = "0,0"
    #Obtener titulo
    for h1 in bs('h1',{'id':'main-title'}):
        titulo = h1('span')[0].string
        print (titulo)
        #titulo[0].string
    #Obtener Año
    for info in bs('dl',{'class':'movie-info'}):
        for dd in info('dd',{'itemprop':'datePublished'}):
            year = dd.string
            print(year)
    #Obtener rating
    rating = bs('div',{'id':'movie-rat-avg'})[0].string
    print(rating)
    print(url)
    return Pelicula(titulo,url,rating,year)
