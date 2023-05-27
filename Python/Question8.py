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

#Q1. Get all the overall ratings for each season and using plots compare the ratings for all the seasons, like season 1 ratings, season 2, and so on.
df['average_rating'] = df['average_rating'].astype(float)

season_ratings = df.groupby('season')['average_rating'].mean()

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
season_ratings.plot(kind='bar', color='blue')
plt.title('Westworld: Season Ratings')
plt.xlabel('Season')
plt.ylabel('Average Rating')
plt.xticks(rotation=0)
plt.show()

#Q2. Get all the episode names, whose average rating is more than 8 for every season

df['average_rating'] = df['average_rating'].astype(float)
episodes = df[df['average_rating'] > 8]

#Q3. Get all the episode names that aired before May 2019

data = df[df['airdate'] < '2019-05' ]

#Q4. Get the episode name from each season with the highest and lowest rating

highest_rated_episodes = df.groupby('season').apply(lambda x: x.loc[x['average_rating'].idxmax()])
lowest_rated_episodes = df.groupby('season').apply(lambda x: x.loc[x['average_rating'].idxmin()])
highest_rated_names = highest_rated_episodes['name'].tolist()
lowest_rated_names = lowest_rated_episodes['name'].tolist()

#Q5. Get the summary for the most popular ( ratings ) episode in every season

episode_summaries = highest_rated_episodes['summary'].tolist()