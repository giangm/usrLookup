#!/usr/bin/python3

import requests
from requests import Timeout
import time
import colorama
from colorama import Fore, Style
from prettytable import PrettyTable

def main():

    # Print banner
    banner()

    # Colored text
    colorama.init(autoreset=True)

    # Username from user input
    username = input(Fore.YELLOW + '[+] Enter username: ')

    # Websites to search
    websites = {'facebook': f'https://www.facebook.com/{username}',
                'instagram': f'https://www.instagram.com/{username}',
                'google_plus': f'https://plus.google.com/s/{username}/top',
                'youtube': f'https://www.youtube.com/{username}',
                'twitter': f'https://www.twitter.com/{username}',
                'blogger': f'https://{username}.blogspot.com',
                'twitch': f'https://www.twitch.tv/{username}',
                'tiktok': f'https://www.tiktok.com/@{username}',
                'reddit': f'https://www.reddit.com/user/{username}',
                'ebay': f'https://www.ebay.com/usr/{username}',
                'wordpress': f'https://{username}.wordpress.com',
                'pinterest': f'https://www.pinterest.com/{username}',
                'slack': f'https://{username}.slack.com',
                'github': f'https://www.github.com/{username}',
                'basecamp': f'https://{username}.basecamphq.com/login',
                'tumblr': f'https://{username}.tumblr.com',
                'flickr': f'https://www.flickr.com/people/{username}',
                'producthunt': f'https://www.producthunt.com/@{username}',
                'steam': f'https://steamcommunity.com/id/{username}',
                'myspace': f'https://myspace.com/{username}',
                'foursquare': f'https://foursquare.com/{username}',
                'okcupid': f'https://www.okcupid.com/profile/{username}',
                'vimeo': f'https://vimeo.com/{username}',
                'etsy': f'https://www.etsy.com/shop/{username}',
                'soundcloud': f'https://soundcloud.com/{username}',
                'bitbucket': f'https://bitbucket.org/{username}',
                'cashme': f'https://cash.me/{username}',
                'dailymotion': f'https://www.dailymotion.com/{username}',
                'aboutme': f'https://about.me/{username}',
                'disqus': f'https://disqus.com/by/{username}',
                'medium': f'https://medium.com/@{username}',
                'behance': f'https://www.behance.net/{username}',
                'coderwall': f'https://coderwall.com/{username}',
                'deviantart': f'https://{username}.deviantart.com',
                'goodreads': f'https://www.goodreads.com/{username}',
                'instructables': f'https://www.instructables.com/member/{username}',
                'keybase': f'https://keybase.io/{username}',
                'kongregate': f'https://kongregate.com/accounts/{username}',
                'livejournal': f'https://{username}.livejournal.com',
                'mix': f'https://mix.com/{username}',
                'angellist': f'https://angel.co/{username}',
                'last_fm': f'https://last.fm/user/{username}',
                'slideshare': f'https://slideshare.net/{username}',
                'paypal': f'https://www.paypal.com/paypalme/{username}',
                'dribbble': f'https://dribbble.com/{username}',
                'imgur': f'https://imgur.com/user/{username}',
                'flipboard': f'https://flipboard.com/@{username}',
                'vk': f'https://vk.com/{username}',
                'codecademy': f'https://www.codecademy.com/{username}',
                'roblox': f'https://www.roblox.com/user.aspx?username:{username}',
                'gravatar': f'https://en.gravatar.com/{username}',
                'trip': f'https://www.trip.skyscanner.com/user/{username}',
                'pastebin': f'https://pastebin.com/u/{username}',
                'blipfm': f'https://blip.fm/{username}',
                'wikipedia': f'https://www.wikipedia.org/wiki/User:{username}',
                'ello': f'https://ello.co/{username}',
                'ifttt': f'https://www.ifttt.com/p/{username}',
                'codementor': f'https://www.codementor.io/{username}',
                'fiverr': f'https://www.fiverr.com/{username}',
                'trakt': f'https://www.trakt.tv/users/{username}',
                'hackernews': f'https://news.ycombinator.com/user?id:{username}',
                'five_hundred_px': f'https://500px.com/{username}',
                'spotify': f'https://open.spotify.com/user/{username}',
                'houzz': f'https://houzz.com/user/{username}',
                'contently': f'https://{username}.contently.com',
                'buzzfeed': f'https://buzzfeed.com/{username}',
                'tripadvisor': f'https://tripadvisor.com/members/{username}',
                'hubpages': f'https://{username}.hubpages.com',
                'scribd': f'https://www.scribd.com/{username}',
                'canva': f'https://www.canva.com/{username}',
                'creative_market': f'https://creativemarket.com/{username}',
                'bandcamp': f'https://www.bandcamp.com/{username}',
                'wikia': f'https://www.fandom.com/u/{username}',
                'reverb_nation': f'https://www.reverbnation.com/{username}',
                'wattpad': f'https://www.wattpad.com/user/{username}',
                'designspiration': f'https://www.designspiration.net/{username}',
                'eyeem': f'https://www.eyeem.com/u/{username}',
                'kanoworld': f'https://world.kano.me/explore/user/{username}',
                'askfm': f'https://ask.fm/{username}',
                'badoo': f'https://www.badoo.com/en/{username}',
                }

    # Perform username lookup
    lookup(websites, username)

def lookup(websites, username):

    # Counter of matches
    matched_counter = 0

    # Pretty Table
    table = PrettyTable()
    table.field_names = ['Website Name', 'URL']

    print(Fore.YELLOW + f'[+] Searching for username: {username}')

    # Searching username
    for name, URL in websites.items():
        try:
            request = requests.get(URL, timeout = 10)
            if request.status_code == 200:
                print(f'---> {name.title()} <---')

                # Check if the username appeared in the website
                if username in request.text:
                    print(Fore.GREEN + Style.DIM + f'[+] MATCH FOUND - {username} has been detected on the {name.title()} website.')
                    print(Fore.GREEN + Style.DIM + f'[+] URL - {URL}')
                    table.add_row([f'{name.title()}', URL])
                else:
                    # Username was not detected on the website, could be false positive
                    print(Fore.RED + f'[+] MATCH FOUND BUT FALSE POSITIVE - {username} has not been detected on the {name.title()} website.')

                matched_counter += 1
        except:
            continue

    print(Fore.YELLOW + f'\n[+] {matched_counter} matches found out of {len(websites)}.')
    print(table)

def banner():
    banner_ascii = '''
    +------------------------------------------------------------+
    |                    _____                __                 |
    | .--.--.-----.----.|     |_.-----.-----.|  |--.--.--.-----. |
    | |  |  |__ --|   _||       |  _  |  _  ||    <|  |  |  _  | |
    | |_____|_____|__|  |_______|_____|_____||__|__|_____|   __| |
    |                                                    |__|    |
    +------------------------------------------------------------+
    '''
    print(Fore.WHITE + banner_ascii)

if __name__ == "__main__":
    main()
