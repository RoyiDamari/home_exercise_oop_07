from typing import override
from TVInterface import TVInterface


class TVNews(TVInterface):
    @override
    def turn_on(self):
        print("TV turning ON (News Channel).")
        return self

    @override
    def turn_off(self):
        print("Turning OFF TV. Remembering last channel as News.")
        from TVOff import TVOff
        return TVOff(self)

    @override
    def news_channel(self):
        print("Resuming News Channel.")
        return self

    @override
    def sports_channel(self):
        print("Switching to Sports Channel.")
        from TVSports import TVSports
        return TVSports()

    @override
    def movies_channel(self):
        print("Switching to Movies Channel.")
        from TVMovies import TVMovies
        return TVMovies()

