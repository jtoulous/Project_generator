import os
import subprocess
from openai import OpenAI
from .tools import getPrompt, printLog, printError, printInfo
from .ai_toolkit import Process_Query, getHisto

class Models():
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPEN_AI_API'))

        self.projectLead = {
            'project': "",
            'behavior': getPrompt('utils/prompts/ProjectLead_behavior2.txt'),
            'history': []
        }


    def init_project(self):
        next_query = self.GPT_query(self.projectLead['behavior'])
        return next_query

    def GPT_query(self, behavior):
        full_query = 'Comportement:\n' + behavior + '\n\nProject:\n' + self.projectLead['project'] + '\nCommence maintenant.'
        printLog(f'\n==> To project_lead:', bright=True)
        printLog(full_query)

        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.projectLead['behavior']},
                {"role": "user", "content": full_query}
            ]
        )

        cmd_list = completion.choices[0].message.content
        return cmd_list
