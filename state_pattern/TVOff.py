from typing import override
from TVInterface import TVInterface


class TVOff(TVInterface):
    def __init__(self, prev_state):
        self.prev_state = prev_state

    @override
    def turn_on(self):
        print(f"TV turning ON. Restoring {self.prev_state.__class__.__name__.replace('TV', '')} Channel...")
        return self.prev_state

    @override
    def turn_off(self):
        print("TV is already OFF.")
        return self

    @override
    def news_channel(self):
        print("TV is OFF. Turning ON to News Channel.")
        from TVNews import TVNews
        return TVNews()

    @override
    def sports_channel(self):
        print("TV is OFF. Turning ON to Sports Channel.")
        from TVSports import TVSports
        return TVSports()

    @override
    def movies_channel(self):
        print("TV is OFF. Turning ON to Movies Channel.")
        from TVMovies import TVMovies
        return TVMovies()

