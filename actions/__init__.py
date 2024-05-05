from typing import List
from .action import Action
from .action_mail import ActionMail
from .action_meeting import ActionMeeting

class ActionManager:
    actions :List[Action] = [
        ActionMail(output_file_path='./data/csv/action_email.csv'),
        ActionMeeting(output_file_path='./data/csv/action_meeting.csv')
        ]

    @classmethod
    def register_action(cls, action):
        cls.actions.append(action)

    def process(self, data):
        for action in self.actions:
            action.parse_action(data)


action_manager = ActionManager()