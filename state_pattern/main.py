from state_pattern import TVContext
from TVMovies import TVMovies

def main():
    tv = TVContext(TVMovies())  # TV starts OFF
    tv.turn_on()  # Turns ON, defaulting to News Channel
    tv.sports_channel()  # Switch to Sports
    tv.movies_channel()  # Switch to Movies
    tv.turn_off()  # Turns OFF, remembering Movies Channel
    tv.turn_off()  # Already OFF
    tv.turn_on()  # Turns ON, restoring Movies Channel
    tv.news_channel()  # Switches to News
    tv.news_channel()  # SResuming News Channel
    tv.turn_off()  # Turns OFF, remembering News Channel
    tv.movies_channel()


if __name__ == "__main__":
     main()