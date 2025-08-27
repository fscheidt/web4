import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from rich import print 
from tmdb.service import MovieService

if __name__ == "__main__":
    movie = MovieService.find_by_id(218)
    print(movie)
