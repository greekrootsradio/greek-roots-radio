import subprocess
import os


class PiperVoice:

    def __init__(self):

        self.model = os.path.expanduser(
            "~/cyprus/models/piper/en_GB-alba-medium.onnx"
        )

        self.output = os.path.expanduser(
            "~/cyprus/audio/zeta.wav"
        )

        self.piper = os.path.expanduser(
            "~/Library/Python/3.9/bin/piper"
        )


    def speak(self, text):

        command = [
            self.piper,
            "--model",
            self.model,
            "--output_file",
            self.output
        ]

        subprocess.run(
            command,
            input=text.encode("utf-8")
        )

        return self.output
