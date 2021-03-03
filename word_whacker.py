import json
from Story import Story
import random


def main():
    start_game()


# def get_story(stories):
#    if len(stories) <= 0:
#        import_stories()
#    #  chooses story randomly
#    index = random.randrange(len(stories))
#    new_story = Story(stories[index])
#    #  removes this story from list so that it won't be repeated
#    del stories[index]
#
#    return new_story


def start_game():
    stories = []

    #  imports all the stories from "Story.py"

    def import_stories():
        f = open("Stories.json")
        data = json.load(f)
        print(data)
        if len(data['stories']) > 0:
            for story in data["stories"]:
                stories.append(story)
            else:
                print("No stories found.")

    def get_story():
        if len(stories) <= 0:
            import_stories()
        #  chooses story randomly
        index = random.randrange(len(stories))
        new_story = Story(stories[index])
        #  removes this story from list so that it won't be repeated
        del stories[index]

        return new_story

    game_in_progress = True
    while game_in_progress:
        my_story = get_story()
        my_story.get_user_input()
        my_story.speak_story()
        print(my_story.title)
        response = input("Do another Word Whack? y/n")
        if response == "n":
            print("Thanks for playing!")
            game_in_progress = False
        elif response != "y":
            print("I didn't really understand that, so I'll take that as a yes.")


main()
