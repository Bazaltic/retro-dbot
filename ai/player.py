import threading
import traceback
import time
from input.window import Window
from input.keyboard import Keyboard
from utils.helpers.collection import Collection
from utils.patterns.observable import Observable
from utils.patterns.observer import Observer

from input.login import Login
import config
import logging

TICK = 0.5


class Player(threading.Thread, Observable, Observer):
    def __init__(self, player_info, game_state) -> None:
        super().__init__(daemon=True)
        self.player_info = player_info
        self.player_name = player_info['name']
        self.player_type = player_info['type']
        self.game_state = game_state
        self.window = None
        self.keyboard = None
        self.login = None

        self.flag_search_mob = False

    # Listen to GUI events
    def update(self, event, event_type):
        if event_type == "flag_search_mob":
            self.flag_search_mob = not self.flag_search_mob

    def find_window(self):
        windows = Window.list_windows()
        w = Collection(windows).find_one(callback=lambda x: self.player_name in x.name)
        if not w:
            self.login = Login(self.player_info)
            self.login.login()
            self.window = self.login.window
            self.keyboard = self.login.kb
        else:
            self.window = w
            self.keyboard = Keyboard(w)
        logging.info(f'Found window for {self.player_name} !')

    def wait_until(self, callback, timeout=60):
        while timeout > 0:
            if callback(self.game_state):
                break
            time.sleep(TICK)
            timeout -= TICK
        return timeout > 0

    def run(self):
        self.find_window()
        self.wait_until(lambda x: x.player_entity_id != 0 and x.map)
        logging.info('Player found !')
        # ai = DummyFighter(self)
        while True:
            try:
                # ai.loop()
                time.sleep(TICK)
            except Exception as e:
                logging.exception(e)

    def __repr__(self):
        return self.player_name


if __name__ == '__main__':
    p = Player(config.PLAYERS[0], None)
    p.find_window()