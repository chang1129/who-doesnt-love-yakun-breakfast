# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:07:31 2024

@author: Chang Chiong Ann
"""

import time
import asyncio
import nest_asyncio
nest_asyncio.apply()

def print_meals(function_name):
    print(f"{function_name.replace('_',' ').capitalize()} is ready.")

async def kaya_butter_toast():
    await asyncio.sleep(5)
    print_meals(kaya_butter_toast.__name__)
    
async def kopi_o():
    await asyncio.sleep(3)
    print_meals(kopi_o.__name__)
    
async def two_soft_boiled_eggs():
    await asyncio.sleep(8)
    print_meals(two_soft_boiled_eggs.__name__)   
    
async def set_a_kaya_toast_with_butter_set():
    
    start_time = time.time()
    print("Asynchronous meals preparation started.")
    
    await asyncio.gather(kaya_butter_toast(), kopi_o(), two_soft_boiled_eggs())
    print_meals(set_a_kaya_toast_with_butter_set.__name__)
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Asynchronous runtime: {total_time} seconds")

if __name__=="__main__":
    asyncio.run(set_a_kaya_toast_with_butter_set())