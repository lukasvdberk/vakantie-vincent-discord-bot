from json.decoder import JSONDecodeError

import discord
import requests
from keys import get_youtube_api_key
from pyyoutube import Api
import random
import json


channel_id = "UC6Qia_DIjUWJHIrk5zI9pmA"

video_links = []
last_know_amount_of_videos = 0
video_data_file_location = "src/data/video_data.json"

with open(video_data_file_location, "r") as video_data_file:
    video_data = json.load(video_data_file)

    video_links = video_data["videos"]
    last_know_amount_of_videos = ["last_know_amount_of_videos"]


def get_all_channel_videos():
    global channel_id, video_links
    api_key = get_youtube_api_key()

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    url = first_url
    while True:
        resp = requests.get(url=url).json()

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links


def get_amount_of_videos_uploaded():
    """
    :return: Returns the amount of videos vakantie vincent has uploaded.
    """
    api = Api(api_key=get_youtube_api_key())
    channel_by_id = api.get_channel_info(channel_id=channel_id)
    return channel_by_id.items[0].to_dict()["statistics"]["videoCount"]


def get_random_video_url():
    global video_links

    return random.choice(video_links)


def fetch_new_videos():
    """
    Gets new videos and saves it to video_data.json.
    Only call this method once a day since it makes a lot of request with the api key.
    :return:
    """
    global channel_id, last_know_amount_of_videos, video_links

    # initialize
    if (last_know_amount_of_videos == 0 and video_links is []) or \
            get_amount_of_videos_uploaded() != last_know_amount_of_videos:

        # Write to a file so the next startup will be quicker
        with open(video_data_file_location, "w+") as video_data_file:
            data_to_write = dict()

            last_know_amount_of_videos = get_amount_of_videos_uploaded()
            video_links = get_all_channel_videos()

            data_to_write["videos"] = video_links
            data_to_write["last_know_amount_of_videos"] = last_know_amount_of_videos
            json.dump(data_to_write, video_data_file)


def get_random_video():
    """
    :return: Searches for a random vakantie vincent video and returns the url.
    """

    return get_random_video_url()


async def send_random_video(client: discord.Client):
    for guild in client.guilds:
        channel_name = "vakantie-vincent-videos"
        # TODO refactor to a specific channel (maybe create a channel beforehand)
        for channel in guild.text_channels:
            # make sure your server has a channel with this name
            if channel.name == channel_name:
                await channel.send(get_random_video())


if __name__ == "__main__":
    # fetches the new video and sets it in data/video_data.json
    fetch_new_videos()
