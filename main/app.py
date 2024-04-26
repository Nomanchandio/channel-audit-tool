import json
import os
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs

API_KEY = os.getenv('API_KEY', 'AIzaSyAVZhXNtFnRkq0Dzx8WZLTd4hxRo-w98q4')

def get_channel_id(api_key, channel_input):
    youtube = build("youtube", "v3", developerKey=api_key)

    parsed_url = urlparse(channel_input)
    if parsed_url.netloc == "www.youtube.com" and parsed_url.path == "/channel":
        query_params = parse_qs(parsed_url.query)
        return query_params.get("channel_id", [None])[0]

    search_response = youtube.search().list(
        q=channel_input,
        type="channel",
        part="id"
    ).execute()

    channel_id = search_response.get("items", [None])[0]["id"]["channelId"] if search_response.get("items") else None

    return channel_id

def get_channel_info(api_key, channel_id):
    youtube = build("youtube", "v3", developerKey=api_key)

    channel_response = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    ).execute()

    channel_data = channel_response.get("items", [None])[0]
    if not channel_data:
        return None

    snippet = channel_data.get("snippet", {})
    statistics = channel_data.get("statistics", {})

    return {
        "channel_title": snippet.get("title"),
        "channel_description": snippet.get("description"),
        "published_at": snippet.get("publishedAt"),
        "subscriber_count": statistics.get("subscriberCount"),
        "view_count": statistics.get("viewCount"),
        "video_count": statistics.get("videoCount"),
    }

def lambda_handler(event, context):
    try:
        channel_id = event.get("channel_id")
        if not channel_id:
            return {
                "statusCode": 401,
                "body": json.dumps({
                    "message": "Channel ID is missing in the event",
                    "data": None
                })
            }

        channel_info = get_channel_info(API_KEY, channel_id)
        if not channel_info:
            return {
                "statusCode": 401,
                "body": json.dumps({
                    "message": "Channel info not found",
                    "data": None
                })
            }

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Your channel audit info",
                "data": channel_info
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": f"Something went wrong! Details: {str(e)}",
                "data": None
            })
        }

# For testing
event = {
    "channel_id": "your_channel_id_here"
}

print(lambda_handler(event, None))