from agent.voice.provider.piper_provider import PiperVoice


class ZetaSpeaker:

    def __init__(self):
        self.voice = PiperVoice()


    def speak(self, message):

        print("ZETA VOICE:", message)

        audio = self.voice.speak(message)

        return audio
