from colorama import Fore, Style

from utils.models import Models
from utils.queries import System_query, Supervisor_query, ProjectLead_query, CodeGen_query
from utils.tools import printLog, printError, printModel, Get_Project


def generate_project(models):
    project_status = "start"
    msg = models.init_project()
    breakpoint()
#
#    while project_status != "DONE":    
#        if msg['target'] == 'SUPERVISER':
#            msg, project_status = Supervisor_query(msg)
#        elif msg['target'] == 'project_lead':
#            msg = ProjectLead_query(msg)
#        elif msg['target'] == 'code_gen':
#            msg = CodeGenerator_query(msg)
#        elif msg['target'] == 'system':
#            msg, project_status = system(msg, project_status)


if __name__ == "__main__":
    try:    
        models = Models()
        models.supervisor['project'] = Get_Project()
        generate_project(models)

    except Exception as error:
        printError(error)