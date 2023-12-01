import requests, re
from bs4 import BeautifulSoup


# Login to intranet
def login(email, password):
   """
        This functions logs in to the intranet

        Args:
            email: your intranet emails
            password: the password associated with your email
        
        Returns: The current active session to stay logged id
   """
   session = requests.Session()
   login_page_response = session.get('https://intranet.alxswe.com/auth/sign_in')
   soup = BeautifulSoup(login_page_response.text, 'html.parser')
   authenticity_token = soup.find('input', attrs={'name': 'authenticity_token'})['value']
   login_data = {
       'user[email]': email,
       'user[password]': password,
       'authenticity_token': authenticity_token
   }
   login_url = 'https://intranet.alxswe.com/auth/sign_in'
   response = session.post(login_url, data=login_data)
   return session


# Extract planning data
def fetch_planning(session):
    """
        This functions extracts the data from the planning

        Args:
            session: The current active sessions
        
        Returns:
            data: The planning data 
    """
    url = "https://intranet.alxswe.com/dashboards/batch_planning_data.json?calendar_view=1&timeshift=-60"
    response = session.get(url)
    data = response.text
    return data


# Extract the ressources
def extract_resources(session, project_id):
    """
        This functions extracts the ressources of
        the current project

        Args:
            session: The current active session
            project_id: The ID associated with the current
                project
        
        Returns:
            The ressources links for the current project
    """
    url = f'https://intranet.alxswe.com/projects/{project_id}'
    response = session.get(url)
    if "Tables" in response.text:
       html_content = response.text
    else:
       exit(1)
    ressources = re.findall(r'<li><a href="/rltoken/(.*?)" title="(.*?)"', html_content, re.DOTALL)
    list_of_ress = [f"[{i[1]}](https://intranet.alxswe.com/rltoken/{i[0]})" for i in ressources]
    return list_of_ress