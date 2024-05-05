import json
import os
import glob
from actions import action_manager


input_file_path = './data/json'


for root, dirs, files in os.walk(input_file_path):
    for file in glob.glob(os.path.join(root, '*.json')):
        with open(file, 'r') as f:
            data = json.load(f)
            action_manager.process(data)


print("CSV файлы успешно созданны!")
