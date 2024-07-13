from colorama import Fore, Style

from utils.models import Models
from utils.tools import printLog, printError, printModel, Get_Project
from utils.ai_toolkit import Execute_Cmd

def generate_project(models):
    project_status = 0
    

    while True:    
        if project_status == 0:
            query = models.init_project()
            project_status = 1
        else:
            query = models.GPT_query(query)
        
        if query == 'DONE':
            return 
        query = Execute_Cmd(query)


if __name__ == "__main__":
    try:    
        models = Models()
        models.projectLead['project'] = Get_Project()
        generate_project(models)

    except Exception as error:
        print(error)