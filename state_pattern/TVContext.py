from TVInterface import TVInterface


class TVContext:
    def __init__(self, tv_state: TVInterface):
        self.tv_state = tv_state
        self.first_time_on = True

    def turn_on(self):
        self.tv_state = self.tv_state.turn_on()

    def turn_off(self):
        self.tv_state = self.tv_state.turn_off()

    def news_channel(self):
        self.tv_state = self.tv_state.news_channel()

    def sports_channel(self):
        self.tv_state = self.tv_state.sports_channel()

    def movies_channel(self):
        self.tv_state = self.tv_state.movies_channel()

