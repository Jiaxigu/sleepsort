# -*- coding: utf-8 -*-

from multiprocessing.dummy import Pool as ThreadPool
from time import sleep

def sleepsort(array, interval = 0.01):
    """
    sort an array of non-negative numeric values with sleepsort.
    :rtype: List
    """
    sorted_list = []
    
    # raise Error when negative value was found
    if min(array) < 0:
        raise ValueError('Array values must be non-negative.')
    
    def task(n):
        sleep(n * interval)
        sorted_list.append(n)
        
    pool = ThreadPool(len(array))
    pool.map(task, array)
    pool.close()
    pool.join()
    return sorted_list