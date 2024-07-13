from colorama import Fore, Style

from utils.models import Models
from utils.tools import printLog, printError, printModel, Get_Project
from utils.ai_toolkit import Execute_Cmds

def generate_project(models):
    #project_status = 0
    cmds_generated = models.init_project()
    cmds = []
    printLog('\n==> generated: ', bright=True)
    for cmd in cmds_generated.split('~'):
        printLog('- ' + cmd)
        cmds.append(cmd)

    breakpoint()
    Execute_Cmds(cmds)


if __name__ == "__main__":
    try:    
        models = Models()
        models.projectLead['project'] = Get_Project()
        generate_project(models)

    except Exception as error:
        print(error)