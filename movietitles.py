#!/usr/bin/python3
import re
def movie_titles_match(titles):
    titles = ""
    movie_pattern = '(.*)\s((\d{4}))'
    
    is_movie_title = re.match(titles, movie_pattern)
    if is_movie_title:
        print(f"{titles} is a movie")
    else:
        print(f"{titles} is not a movie, please enter a proper movie name")


# test 
if __name__ == "__main__":
    titles = ""
    movie_titles_match(titles)