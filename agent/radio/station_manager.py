from datetime import datetime
import json
import os


class StationManager:

    def __init__(self):

        self.project_file = os.path.expanduser(
            "~/cyprus/workspace/projects/greek_roots_radio.json"
        )


    def load_project(self):

        if not os.path.exists(self.project_file):
            return {}

        with open(self.project_file, "r") as f:
            return json.load(f)


    def save_project(self, project):

        os.makedirs(os.path.dirname(self.project_file), exist_ok=True)

        with open(self.project_file, "w") as f:
            json.dump(project, f, indent=4)


    def build(self):

        project = self.load_project()

        project["branding"] = {
            "station_name": "Greek Roots Radio",
            "tagline": "Greek Cypriots Growing Up in the UK",
            "identity": "Greek • Reggae • Community • Culture"
        }

        project["music_categories"] = [
            "Classic Greek",
            "Cypriot",
            "Laiko",
            "Modern Greek",
            "Reggae",
            "Roots Reggae",
            "Dub",
            "Mediterranean Fusion"
        ]

        project["daily_schedule"] = {
            "06:00": "Morning Coffee",
            "09:00": "Community Mix",
            "12:00": "Greek Classics",
            "15:00": "Cyprus Hour",
            "18:00": "Drive Home",
            "20:00": "Reggae Roots",
            "22:00": "Late Night Chill"
        }

        project["ai_presenter"] = {
            "name": "ZETA",
            "role": "AI Radio Host",
            "voice_style": "Warm Greek Cypriot",
            "languages": [
                "English",
                "Greek",
                "Cypriot Greek"
            ]
        }

        project["status"] = "station build in progress"
        project["last_updated"] = str(datetime.now())

        self.save_project(project)

        return {
            "agent": "ZETA Station Manager",
            "status": "updated",
            "project": project
        }
