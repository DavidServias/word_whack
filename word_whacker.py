import re
import json
import os
import random
import subprocess


# story class
class Story:
    def __init__(self, story_data):
        self.title = story_data["title"]
        self.text = story_data["text"]
        # to insert a prompt in a story, enclose it with <prompt>
        # the following command will extract all of the prompts into a list
        self.prompts = re.findall("<[\w\s]+>", self.text)
        self.user_input = []

    # gets a response from the user for each prompt, and saves it in user_input list.
    def get_user_input(self):
        print(messages["user_input_prompt"])
        for prompt in self.prompts:
            prompt += ": "
            response = input(prompt)
            self.user_input.append(response)

    def insert_user_input(self):
        if len(self.user_input) > 0:
            new_text = self.text
            temp_input = self.user_input
            for prompt in self.prompts:
                # replace one ocadsf
                # currence of prompt with first item on temp_input list
                new_text = re.sub(prompt, temp_input[0], new_text, 1)
                # remove first item of temp_input list
                del temp_input[0]
            self.text = new_text

    def print_story(self):
        print(self.title,)
        print(self.text)

    def speak_story(self):
        subprocess.call(["python", "Speech.py", self.text])

        #  os.system("python Speech.py")
        #  To do: use "subprocess" instead.


def get_story():
    f = open("Stories.json")
    data = json.load(f)
    new_story = data["stories"][0]
    return Story(new_story)


messages = {
    "welcome": "Welcome to Wacky Story Maker",
    "user_input_prompt": "Please give your response:"
}


my_story = get_story()
my_story.get_user_input()
my_story.insert_user_input()
my_story.print_story()
my_story.speak_story()
