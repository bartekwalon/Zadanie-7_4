
class Movie:
    
    def __init__(self, title, release, genre, views):
        self.title, self.release, self.genre, self.views = title, release, genre, views
        self.played = 0

    def play(self):
        self.played += 1
    
    def __str__(self):
        return f'{self.title} ({self.release}) {self.genre}, views:{self.views}'

    __repr__ = __str__

class Episode(Movie):

    def __init__(self, title, release, genre, views, episode, season):
        super().__init__(title, release, genre, views)
        self.episode, self.season = episode, season
        self.played = 0

    def play(self):
        self.played += 1

    def __str__(self):
        return f'S{self.season:02d}E{self.episode:02d} {self.title} ({self.release} {self.genre}, views:{self.views})'

    __repr__ = __str__


def get_movies(library):
    return [
        item for item
        in sorted(library, key=lambda item: item.title.lower())
        if not isinstance(item, Episode)
    ]

def get_series(library):
    return [
        item for item
        in sorted(library, key=lambda item: item.title.lower())
        if isinstance(item, Episode)
    ]

def generate_views(library):
    import random
    return random.choices(library, k=1)

def search(bibl):
    index = bibl.index()
    return f'{index}'

if __name__ == '__main__':
    from random import randint, random, choice
    from faker import Faker
    fake = Faker('pl_PL')

    library = [
        Movie (
            fake.name(), randint(1940, 2921), choice(('comedy', 'horror')), 0
        ) if random() > 0.75 else Episode(
            fake.name(), randint(1940, 2021), choice(('comedy', 'horror')), 0, randint(1, 15), randint(1, 6)
        ) for _ in range(randint(20, 35))
    ]

    print(get_movies(library))

if __name__ == '__main__':
    from random import randint, random, choice
    from faker import Faker
    fake = Faker('pl_PL')

    bibl = [
        Movie('Matrix', 1999, 'fiction', 0),
        Episode('Friend', 2099, 'comedy', 0, 5, 26)
    ]

    
