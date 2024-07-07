from utils.models import Models
from utils.tools import printLog, printError

def generate_project(models):
    project_status = "start"
    msg = models.init_project()
    breakpoint()
#
#    while project_status != "finished":    
#        if msg['target'] == 'supervisor':
#            msg, project_status = supervisor(msg)
#        elif msg['target'] == 'project_lead':
#            msg = project_lead(msg)
#        elif msg['target'] == 'worker':
#            msg = worker(msg)
#        elif msg['target'] == 'system':
#            msg = system(msg)


if __name__ == "__main__":
    models = Models()
    models.supervisor['project'] = input('Describe your project very clearly in details: \n')

    generate_project(models)