# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:27:41 2024

@author: Chang Chiong Ann
"""

import time

def print_meals(function_name):
    print(f"{function_name.replace('_',' ').capitalize()} is ready.")

def kaya_butter_toast():
    time.sleep(5)
    print_meals(kaya_butter_toast.__name__)
    
def kopi_o():
    time.sleep(3)
    print_meals(kopi_o.__name__)
    
def two_soft_boiled_eggs():
    time.sleep(8)
    print_meals(two_soft_boiled_eggs.__name__) 
    
def set_a_kaya_toast_with_butter_set():
    start_time = time.time()
    print("Synchronous meals preparation started.")
    kopi_o()
    kaya_butter_toast()
    two_soft_boiled_eggs()
    print_meals(set_a_kaya_toast_with_butter_set.__name__)
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Synchronous runtime: {total_time} seconds")
    
if __name__=="__main__":
    set_a_kaya_toast_with_butter_set()