def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating 
        }
        return movie
        
    return None

def add_to_watched(user_data,movie):
    if length.watched = 0:
        watched.append(movie)
        return user_data