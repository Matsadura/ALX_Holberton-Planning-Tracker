# ALX / Holberton Planning Tracker
# Author: Zidane ZAOUI
# Nickname: Matsadura

import json, re
from discord_webhook import DiscordWebhook
from datetime import datetime
from info import *
from misc import *


# Keeps the login active
session = login(email, password)

# The planning data
PLAN = json.loads(fetch_planning(session))

# Sets the current date to compare with project deadline
current_date = datetime.now()



# Parse the projects for (My cohort "18") and appends them in MY_LIST
MY_LIST = []
HEADER = "> Cohort 18:"
MY_LIST.append(HEADER)
COUNT = 1
res = []
for project in PLAN['data']:
    start_date = datetime.strptime(project['start_date'], "%d-%m-%Y %H:%M")
    end_date = datetime.strptime(project['end_date'], "%d-%m-%Y %H:%M")

    if start_date <= current_date <= end_date:
        if project['type'] == 'project':
            PROJECT_INFO = f"```Project : {project['text']}\nDeadline : From {start_date.strftime('%d-%m-%Y')} to {end_date.strftime('%d-%m-%Y')} [First Deadline]```"
            if '_id' in project:
                res = extract_resources(session ,project['_id'])
            COUNT = 0
        elif project['type'] == 'project-second-deadline':
            PROJECT_INFO = f"```Project : {project['text']}\nDeadline : From {start_date.strftime('%d-%m-%Y')} to {end_date.strftime('%d-%m-%Y')} [Second Deadline]```"
            if 'id' in project:
                P_ID = re.findall(r"project-(.*?)-", project['id'])
                res = extract_resources(session , P_ID[0])

            COUNT = 0
        if COUNT == 1:
            MY_LIST.append("```None, enjoy the silence.```")
        else:
            if PROJECT_INFO not in MY_LIST:
                MY_LIST.append(PROJECT_INFO)
            MY_LIST.append(f"Ressources for this project :")
            for r in res:
                MY_LIST.append(r)


content= "\n".join(MY_LIST)

# Send the result to the Discord Channel
webhook = DiscordWebhook(url=hook, content=f"{content}\n\n#DoHardThings\n")
response = webhook.execute()