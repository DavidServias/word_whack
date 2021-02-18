import re


# story class
class Story:
    def __init__(self, title, story_text):
        self.title = title
        self.story_text = story_text
        # to insert a prompt in a story, enclose it with <prompt>
        # the following command will extract all of the prompts into a list
        self.prompts = re.findall("<[\w\s]+>", self.story_text)
        self.user_input = []

    # gets a response from the user for each prompt, and saves it in user_input list.
    def get_user_input(self):
        print(messages["user_input_prompt"])
        for prompt in self.prompts:
            prompt += ": "
            response = input(prompt)
            self.user_input.append(response)

    def insert_user_input(self):
        new_text = self.story_text
        temp_input = self.user_input
        for prompt in self.prompts:
            # replace one occurrence of prompt with first item on temp_input list
            new_text = re.sub(prompt, temp_input[0], new_text, 1)
            # remove first item of temp_input list
            del temp_input[0]
        return new_text

    def print_story(self):
        print(self.title,)
        print(self.insert_user_input())


messages = {
    "welcome": "Welcome to Wacky Story Maker",
    "user_input_prompt": "Please give your response:"
}


my_story = Story(my_title, my_story_text)

my_story.get_user_input()
my_story.print_story()
