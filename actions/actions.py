# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction


class ActionWelcomeUser(Action):

    def name(self) -> Text:
        return "action_welcome_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name_ = ""
        name_ = tracker.get_slot("name_")
        nameset = tracker.get_slot("nameset")
        if name_ is None:
            dispatcher.utter_message(
                text="Hi welcome to weave! What is your name?")
        else:
            if nameset is True:
                dispatcher.utter_message(
                    text="Hi {}, welcome back! What is your goal on weave today?".format(name_))

            else:
                dispatcher.utter_message(
                    text="Hi {}, I'm here to guide you - what is your goal on weave today?".format(name_))
        return [SlotSet("nameset", True if name_ is not None else False)]
