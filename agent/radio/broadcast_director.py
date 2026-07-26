from datetime import datetime

from agent.radio.show_generator import ShowGenerator
from agent.radio.presenter import RadioPresenter
from agent.radio.music_scheduler import MusicScheduler
from agent.radio.radio_memory import RadioMemory


class BroadcastDirector:


    def __init__(self):

        self.show_generator = ShowGenerator()

        self.presenter = RadioPresenter()

        self.music = MusicScheduler()

        self.memory = RadioMemory()



    def create_broadcast(self):


        show = self.show_generator.create_show()

        presenter_intro = self.presenter.create_intro()

        playlist = self.music.create_playlist()


        broadcast = {


            "station": "Greek Roots Radio",


            "show": show,


            "presenter_intro": presenter_intro,


            "music_playlist": playlist,


            "broadcast_time": str(datetime.now()),


            "status": "broadcast created"


        }


        memory_result = self.memory.remember_broadcast(
            broadcast
        )


        broadcast["memory"] = memory_result


        return broadcast
