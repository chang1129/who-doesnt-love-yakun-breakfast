# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:53:16 2024

@author: Chang Chiong Ann
"""

import requests
import time


urls = [
    "https://www.google.com",
    "https://www.bing.com",
    "https://www.duckduckgo.com",
    "https://www.yahoo.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.linkedin.com",
    "https://www.tiktok.com",
    "https://www.wikipedia.org",
    # "https://www.wikiwiki.org"
]

def send_request(url):
    try:
        response = requests.get(url)
        print(f"URL: {url}, Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

def main():
    start_time = time.time()
    print("Synchronous run started.")
    
    for url in urls:
        send_request(url)
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Synchronous runtime: {total_time} seconds")

if __name__=="__main__":
    main()