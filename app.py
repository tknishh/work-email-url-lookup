import pandas as pd
import requests
import os
import time
from dotenv import load_dotenv
from itertools import islice

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

def process_urls(urls):
    for url in urls:
        response = get_linkedin_profile_email(url)
        # Process the response as needed
        print(response.json())

api_key = os.environ.get('API_KEY')
file_path = './data/pending_work_email.csv'
df = read_csv_to_dataframe(file_path)

urls = df['LinkedIn Profile']
batch_size = 10
total_rows = len(urls)
start_index = 0

while start_index < total_rows:
    batch_urls = islice(urls, start_index, start_index + batch_size)
    process_urls(batch_urls)
    time.sleep(120)  # Delay for 2 minutes (120 seconds)
    start_index += batch_size
