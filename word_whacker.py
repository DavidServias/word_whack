import re
import json
from gtts import gTTS
from playsound import playsound
from Story import Story


def main():
    stories = []

    def import_stories():
        f = open("Stories.json")
        data = json.load(f)
        for story in data["stories"]:
            stories.append(story)
        if len(stories) < 0:
            print("No stories found.")

    def get_story():
        if len(stories) <= 0:
            import_stories()

        return Story(stories[0])

    my_story = get_story()
    my_story.get_user_input()
    my_story.speak_story()


main()
