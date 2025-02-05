from typing import override
from TVInterface import TVInterface


class TVMovies(TVInterface):
    @override
    def turn_on(self):
        print("TV turning ON (Movies Channel).")
        return self

    @override
    def turn_off(self):
        print("Turning OFF TV. Remembering last channel as Movies.")
        from TVOff import TVOff
        return TVOff(self)

    @override
    def news_channel(self):
        print("Switching to News Channel.")
        from TVNews import TVNews
        return TVNews()

    @override
    def sports_channel(self):
        print("Switching to Sports Channel.")
        from TVSports import TVSports
        return TVSports()

    @override
    def movies_channel(self):
        print("Resuming Movies Channel.")
        return self

