# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 20:06:15 2024

@author: Chang Chiong Ann
"""

import asyncio
import aiohttp
import time
import nest_asyncio
nest_asyncio.apply()

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

async def send_request(session, url):
    try:
        async with session.get(url) as response: 
            print(f"URL: {url}, Status Code: {response.status}")
            return response.status
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def main():
    start_time = time.time()
    print("Asynchronous run started.")
    
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, url) for url in urls]
        await asyncio.gather(*tasks)
        
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Asynchronous runtime: {total_time} seconds")

if __name__=="__main__":
    asyncio.run(main())