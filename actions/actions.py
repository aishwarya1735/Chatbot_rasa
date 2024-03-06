# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import webbrowser
import wikipedia
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionPlayMusic(Action):
    def name(self) -> Text:
        return "action_play_music"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to play music
        dispatcher.utter_message(text="Playing music...")
        return []

class ActionGetInfoWikipedia(Action):
    def name(self) -> Text:
        return "action_get_info_wikipedia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query = tracker.latest_message.get('text')
        try:
            summary = wikipedia.summary(query)
            dispatcher.utter_message(text=summary)
        except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) as e:
            dispatcher.utter_message(text="Please provide more specific query.")
        return []

class ActionOpenGitHub(Action):
    def name(self) -> Text:
        return "action_open_github"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        webbrowser.open('https://github.com')
        dispatcher.utter_message(text="Opening GitHub...")
        return []
