class Pelicula:
    def __init__(self,titulo,url,nota,year):
        self.titulo = titulo
        self.url = url
        self.nota = nota
        self.year = year
    def datos_peli(self):
        return str("Título: " + str(self.titulo) + " Año: " + str(self.year) + " Nota: " + str(self.nota))