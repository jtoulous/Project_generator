from transformers import GPTJForCausalLM, GPTNeoXForCausalLM, GPT2LMHeadModel, AutoTokenizer
from .tools import getPrompt, printLog, printError

class Models():
    def __init__(self):
#        supervisor_model = "EleutherAI/gpt-j-6B" 
#        project_lead_model = "EleutherAI/gpt-j-6B"
#        worker_model = "EleutherAI/gpt-neox-20b"

        supervisor_model = "gpt2" 
        project_lead_model = "gpt2"
        worker_model = "gpt2"

        self.supervisor = {
            'model_name': supervisor_model,
            'model': GPT2LMHeadModel.from_pretrained(supervisor_model),
            'tokenizer': AutoTokenizer.from_pretrained(supervisor_model),
            'behavior': getPrompt('utils/prompts/supervisor_behavior.txt'),
            'project': "",
            'history': [],
        }

        self.project_lead = {
            'model_name': project_lead_model,
            'model': GPT2LMHeadModel.from_pretrained(project_lead_model),
            'tokenizer': AutoTokenizer.from_pretrained(project_lead_model),
            'behavior': getPrompt('utils/prompts/projectLead_behavior.txt'),
            'task': ""
        }

        self.worker = {
            'model_name': worker_model,
            'model': GPT2LMHeadModel.from_pretrained(worker_model),
            'tokenizer': AutoTokenizer.from_pretrained(worker_model),
            'behavior': getPrompt('utils/prompts/worker_behavior.txt'),
            'task': ""
        }


    def supervisor_query(self, query):
        breakpoint()
        remastered_query = ""
        behavior_reminder = "Rappel: " + self.supervisor['behavior']
        for msg in self.supervisor['history']:
            remastered_query = remastered_query + msg
        remastered_query = remastered_query + '\n' + behavior_reminder + '\n' + query
        self.supervisor['history'].append(query)

        printLog(f'\nTo superviser ===> {query}\n')
        inputs = self.supervisor['tokenizer'](remastered_query, return_tensors="pt")
        outputs = self.supervisor['model'].generate(inputs['input_ids'], max_length=1024, num_return_sequences=1)
        response = self.supervisor['tokenizer'].decode(outputs[0], skip_special_tokens=True)
        return response

#    def project_lead(self, msg):

#    def worker(self, msg):    

    def init_project(self):
        msg = self.supervisor_query(self.supervisor['project'] + '\n Commence maintenant.')
        return msg