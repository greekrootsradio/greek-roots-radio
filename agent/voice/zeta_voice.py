from agent.skills.chat import run
from agent.voice.speaker import ZetaSpeaker


class ZetaVoice:

    def __init__(self):
        self.speaker = ZetaSpeaker()


    def talk(self, message):

        print("\nANDREAS:")
        print(message)

        response = run(message)

        print("\nZETA:")
        print(response)

        audio = self.speaker.speak(response)

        print("\nZETA VOICE:")
        print(response)

        print("\nAudio created:")
        print(audio)

        return audio



if __name__ == "__main__":

    zeta = ZetaVoice()

    while True:

        try:
            message = input("\nYou: ")

        except KeyboardInterrupt:
            print("\nZETA shutting down.")
            break


        if message.lower() in ["exit", "quit", "stop"]:
            print("ZETA shutting down.")
            break


        if message.strip() == "":
            continue


        zeta.talk(message)
