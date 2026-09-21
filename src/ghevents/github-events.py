import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
    json_text = requests.get(url).text
    events = json.loads(json_text)
    return events

def print_events(events, n=5):
    for x in events:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)

def main():
    """
    Main function for the GitHub events script.
    Prints GHUSER and url, retrieves events, and prints the first few.
    """
    print("GHUSER:", GHUSER)
    print("URL:", url)

    events = retrieve_events(url)
    print_events(events)   # uses default n=5

if __name__ == "__main__":
    main()