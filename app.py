import pandas as pd
import requests
import os
import time
from itertools import islice
from dotenv import load_dotenv

load_dotenv()

def read_csv_to_dataframe(file_path):
    df = pd.read_csv(file_path)
    return df

def get_linkedin_profile_email(linkedin_profile_url):
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/email'
    params = {
        'linkedin_profile_url': linkedin_profile_url,
        'callback_url': 'https://smee.io/ZSqyrKVv9OND7kBp',
    }
    response = requests.get(api_endpoint, params=params, headers=headers)
    return response

def process_company_domain(company_domain):
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company/resolve'
    params = {
        'company_domain': company_domain,
    }
    response = requests.get(api_endpoint, params=params, headers=headers)
    return response

api_key = os.environ.get('API_KEY')
file_path = '../data/test.csv'
df = read_csv_to_dataframe(file_path)

# Limit the iteration to 100 URLs every 15 minutes
urls = islice(df['LinkedIn Profile'], 100)
for url in urls:
    response = get_linkedin_profile_email(url)
    # Process the response as needed
    print(response.json())
    time.sleep(900)  # Delay for 15 minutes (900 seconds)
