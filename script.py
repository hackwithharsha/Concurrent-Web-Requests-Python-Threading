import requests
import threading
from loguru import logger

def get_status(task_id):
    logger.info(f'Fetch status for task_id: {task_id}')
    res = requests.get(f'http://localhost:8000/status?task_id={task_id}')
    logger.info(f'{res.status_code} {res.text}')


threads = []

for i in range(12, 20):
    thread = threading.Thread(target=get_status, args=(i, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
