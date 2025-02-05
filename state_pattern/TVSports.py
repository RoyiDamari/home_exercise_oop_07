from typing import override
from TVInterface import TVInterface


class TVSports(TVInterface):
    @override
    def turn_on(self):
        print("TV turning ON (Sports Channel).")
        return self

    @override
    def turn_off(self):
        print("Turning OFF TV. Remembering last channel as Sports.")
        from TVOff import TVOff
        return TVOff(self)

    @override
    def news_channel(self):
        print("Switching to News Channel.")
        from TVNews import TVNews
        return TVNews()

    @override
    def sports_channel(self):
        print("Resuming Sports Channel.")
        return self

    @override
    def movies_channel(self):
        print("Switching to Movies Channel.")
        from TVMovies import TVMovies
        return TVMovies()

