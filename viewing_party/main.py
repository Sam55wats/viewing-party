def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating 
        }
        return movie
        
    return None

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data 

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
       if title == movie['title']:
            user_data['watchlist'].remove(movie)
            user_data['watched'].append(movie)
       
    return user_data