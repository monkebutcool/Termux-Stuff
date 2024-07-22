import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from colorama import Fore, Style

API_KEY_FILE = "youtube.api.key"

# Function to get YouTube API key from user or file
def get_api_key():
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, "r") as file:
            api_key = file.readline().strip()
            if api_key:
                return api_key
    # If file doesn't exist or key is not valid, prompt user for new key
    api_key = input("Enter your YouTube API key: ")
    with open(API_KEY_FILE, "w") as file:
        file.write(api_key)
    return api_key

# Function to retrieve channel information using YouTube API
def get_channel_info(api_key):
    api_service_name = "youtube"
    api_version = "v3"

    youtube = build(api_service_name, api_version, developerKey=api_key)

    while True:
        mention = input("Enter the YouTube channel mention (e.g., \"@YouTube\"): ").strip()
        if mention.startswith("@"):
            username = mention[1:]  # Remove "@" prefix
        else:
            print("Please enter a mention starting with '@'.")
            continue

        try:
            request = youtube.channels().list(part="snippet,statistics", forUsername=username)
            response = request.execute()

            if 'items' in response and len(response['items']) > 0:
                channel_data = response["items"][0]

                nickname = channel_data["snippet"]["title"]
                
                # Handling subscriber count
                subs = int(channel_data["statistics"].get("subscriberCount", "Unknown"))
                
                # Handling view count
                views = int(channel_data["statistics"].get("viewCount", "Unknown"))
                
                creation_date = channel_data["snippet"]["publishedAt"]
                channel_bio = channel_data["snippet"].get("description", "No description available")

                print(f"{Fore.GREEN}Nickname: {nickname}")
                print(f"Mention: @{username}")
                print(f"All Time Subs: {subs}")
                print(f"All Time Views: {views}")
                print(f"Creation Date: {creation_date}")
                print(f"Channel Bio: {channel_bio}")
                print(Style.RESET_ALL)
                break
            else:
                print(f"Channel with mention '@{username}' not found.")
        except HttpError as e:
            print(f"HTTP Error: {e}")
        except KeyError as e:
            print(f"KeyError: {e}. Response: {response}")

# Main program
if __name__ == "__main__":
    api_key = get_api_key()
    get_channel_info(api_key)
