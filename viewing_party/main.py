def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating 
        }
        return movie
        
    return None