import re
from gtts import gTTS
from playsound import playsound


# story class
class Story:
    def __init__(self, story_data):
        self.title = story_data["title"]
        self.text = story_data["text"]
        # to insert a prompt in a story, enclose it with <prompt>
        # the following command will extract all of the prompts into a list
        self.prompts = re.findall("<[\w\s]+>", self.text)
        self.user_input = []

    def test(self):
        print(self.title)

    def insert_user_input(self):
        if len(self.user_input) > 0:
            new_text = self.text
            temp_input = self.user_input
            for prompt in self.prompts:
                # replace each occurrence of prompt with first item on temp_input list
                new_text = re.sub(prompt, temp_input[0], new_text, 1)
                # remove first item of temp_input list
                del temp_input[0]
            self.text = new_text

    # gets a response from the user for each prompt, and saves it in user_input list.
    def get_user_input(self):
        print("Fill in the blanks:",)
        for prompt in self.prompts:
            prompt += ": "
            response = input(prompt)
            self.user_input.append(response)
        self.insert_user_input()

    def speak_story(self):
        split_text = self.text.split(". ")
        # Language in which you want to convert
        language = 'en'
        # speak title
        print(self.title)
        speech_audio = gTTS(text=self.title, lang=language, slow=False)
        speech_audio.save("speech_audio.mp3")
        playsound('speech_audio.mp3')
        # speak text
        for line in split_text:
            print(line + ".")
            speech_audio = gTTS(text=line, lang=language, slow=False)
            speech_audio.save("speech_audio.mp3")
            playsound('speech_audio.mp3')
