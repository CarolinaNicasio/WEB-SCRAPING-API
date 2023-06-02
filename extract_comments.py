import pandas as pd
from googleapiclient.discovery import build

#API youtube
DEVELOPER_KEY= "AIzaSyA1r-5rZZ6ycGMGjHOENc9TEbjPz7g0cBc"
VIDEO_ID = 'Uoox9fpmDP0'

def get_comments():
    api_version = 'v3'
    youtube = build('youtube', api_version, developerKey=  
                    DEVELOPER_KEY)
    response = youtube.commentThreads().list(
        part='snippet, replies',
        videoId=VIDEO_ID,
        maxResults = 100).execute()
    return response

response = get_comments()

comments = []
for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    comments.append(comment)
df = pd.DataFrame(comments, columns=['Comment'])


#CSV
df.to_csv('comments.csv', index=False)
