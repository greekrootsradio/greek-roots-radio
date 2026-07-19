from datetime import datetime

from agent.projects.radio.live.runtime.engine import start_runtime
from agent.projects.radio.audio.assembler import assemble_segment


def run_broadcast_cycle():

    runtime = start_runtime()

    audio = assemble_segment()

    cycle = {

        "engine": "ZETA Continuous Broadcast Loop",

        "station": "Greek Roots Radio",

        "time": datetime.now().isoformat(),

        "runtime": runtime,

        "segment": audio,

        "actions": [

            "generate_presenter",

            "prepare_audio",

            "play_music",

            "monitor_listener_state",

            "select_next_segment"

        ],

        "status": "BROADCAST_CYCLE_READY"

    }

    return cycle


if __name__ == "__main__":

    print(run_broadcast_cycle())
