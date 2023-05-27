import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes'
response = requests.get(url).json()

def extract_episodes(data):
    episodes = data['_embedded']['episodes']
    extracted_data = []
    
    for episode in episodes:
        episode_data = {}
        episode_data['id'] = episode['id']
        episode_data['url'] = episode['url']
        episode_data['name'] = episode['name']
        episode_data['season'] = episode['season']
        episode_data['number'] = episode['number']
        episode_data['type'] = episode['type']
        episode_data['airdate'] = episode['airdate']
        episode_data['airtime'] = episode['airtime']
        episode_data['runtime'] = episode['runtime']
        episode_data['average_rating'] = episode['rating']['average']
        
        # Remove HTML tags from summary
        summary_html = episode['summary']
        summary_text = BeautifulSoup(summary_html, 'html.parser').get_text()
        episode_data['summary'] = summary_text
        
        # Extract image links
        episode_data['medium_image_link'] = episode['image']['medium']
        episode_data['original_image_link'] = episode['image']['original']
        
        extracted_data.append(episode_data)
    
    return extracted_data

episodes = extract_episodes(response)

df = pd.DataFrame(episodes)

df.to_csv("episodes.csv", index=False)
