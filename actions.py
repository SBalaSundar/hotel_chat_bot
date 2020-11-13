# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from datetime import datetime, timedelta
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import logging

logger = logging.getLogger(__name__)


class ActionScheduleCleaning(Action):

    def name(self) -> Text:
        return "action_schedule_cleaning"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number_of_hours = tracker.get_slot("number_of_hours")
        offset=int(number_of_hours) if number_of_hours else 0 
        logging.error(offset)
        scheduled_time= datetime.now() + timedelta(hours=offset)
        time=scheduled_time.strftime('%H:%M')
        logging.error(time)
        dispatcher.utter_message(text="Sure, I have scheduled a cleaning at "+time)

        return []
