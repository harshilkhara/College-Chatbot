# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from scraper import *

class ActionHelloWorld(FormAction):

	def name(self) -> Text:
		return "info_form"
	@staticmethod
	def required_slots(tracker: "Tracker") -> List[Text]:
		print("required_slot(traker: Traker)")
		return ["name", "number", "branch"]
	def submit(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
		dispatcher.utter_message(template="utter_submit", name=tracker.get_slot('name'),
								 number=tracker.get_slot('number'),
							     city=tracker.get_slot('branch'))
		return[]
	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
		return {
			"name": self.from_entity(entity="name", intent='name_entry'),
			"number": self.from_entity(entity="number", intent='number_entry'),
			"branch": self.from_entity(entity="branch", intent='branch_entry'),
		}

class ActionIntake(Action):
	def name(self) -> Text:
		return "action_intake_api"
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		text=Intake()
		dispatcher.utter_message(template="utter_intake",temp=text)
		return []

class ActionItprof(Action):
	def name(self) -> Text:
		return "action_itprof_api"
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		text=Itprof()
		dispatcher.utter_message(template="utter_itprof",temp1=text)
		return []

class ActionFees1(Action):
	def name(self) -> Text:
		return "action_fees1_api"
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		text=Fees1()
		dispatcher.utter_message(template="utter_fees1",temp2=text)
		return []

class ActionFees2(Action):
	def name(self) -> Text:
		return "action_fees2_api"
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		text=Fees2()
		dispatcher.utter_message(template="utter_fees2",temp3=text)
		return []

class ActionFees3(Action):
	def name(self) -> Text:
		return "action_fees3_api"
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		text=Fees3()
		dispatcher.utter_message(template="utter_fees3",temp4=text)
		return []

class ActionFees4(Action):
	def name(self) -> Text:
		return "action_fees4_api"
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		text=Fees2()
		dispatcher.utter_message(template="utter_fees4",temp5=text)
		return []

class ActionRegister(Action):
	def name(self) -> Text:
		return "action_register_api"
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		text=Register()
		dispatcher.utter_message(template="utter_register",temp6=text)
		return []

class ActionContact(Action):
	def name(self) -> Text:
		return "action_contact_api"
	def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		
		text=Contact()
		dispatcher.utter_message(template="utter_contact",temp7=text)
		return []

