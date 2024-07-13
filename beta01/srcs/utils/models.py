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
            'behavior': getPrompt('utils/prompts/ProjectLead_behavior1.txt'),
            'history': []
        }


    def init_project(self):
        next_query = self.GPT_query(self.projectLead['project'] + '\n Commence maintenant.')
        return next_query

    def GPT_query(self, query):
        printLog(f'\n==> To project_lead:', bright=True)
        printLog(query)

        history = getHisto(self.projectLead)
        full_query = 'Project: ' + self.projectLead['project'] +  history + '\n query:' + query
        full_query = 'query:' + query
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.projectLead['behavior']},
                {"role": "user", "content": full_query}
            ]
        )

        next_query = completion.choices[0].message.content
        printLog('\n==> generated: ', bright=True)
        printLog(next_query)
        self.projectLead['history'].append(query)
        self.projectLead['history'].append(next_query)
        return next_query
