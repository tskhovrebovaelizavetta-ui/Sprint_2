class Movies:
    def __init__(self):
        self.movies = []
    def add_movie(self, movie):
        self.movies.append(movie)
    

class Comedy(Movies):
    def add_movie(self, movie):           # Переопределяем
        super().add_movie(movie)          # Добавляем через родителя
        return f"Комедии: {self.movies}"  # Возвращаем обновлённый список

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: {self.movies}"
    
comedy = Comedy()
print(comedy.add_movie('Большой куш'))
drama = Drama()
print(drama.add_movie('Оружейный барон'))