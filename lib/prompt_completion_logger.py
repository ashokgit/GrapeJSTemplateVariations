import os
import json
from datetime import datetime

class PromptCompletionLogger:
    def __init__(self):
        self.log_dir = './log'
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def log(self, prompt, completion):
        data = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'prompt': prompt,
            'completion': completion
        }
        log_file_path = os.path.join(self.log_dir, 'log.jsonl')
        with open(log_file_path, 'a') as f:
            f.write(json.dumps(data) + '\n')
