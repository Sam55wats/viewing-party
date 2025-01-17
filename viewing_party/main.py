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

def get_watched_avg_rating(user_data):
    if len(user_data['watched']) == 0:
        return 0.0

    sum_ratings = 0
    for movie in user_data['watched']:
        sum_ratings += movie['rating'] # sum_ratings = sum_ratings + movie['rating']

    return sum_ratings / len(user_data['watched'])
