
# -*- coding: utf-8 -*-
"""
Created on 

@author: OWP
"""

#%%

import numpy as np
from timeit import default_timer as timer

#%%

def tic():

    # Timing function
    
    # Outputs:
    # t0: initial time
    
    t0=timer()
    return t0

def toc(t0,digits=5):

    # Timing function
    
    # Inputs:
    # t0: initial time

    t1=timer()
    dt=t1-t0   
    
    if dt>1:
        digits=2
    elif dt>0.1:
        digits=3
    elif dt>0.01:
        digits=4

    format_f='{:.' + str(digits) + 'f}'
    print('Elapsed time: ' + format_f.format(dt) + ' seconds.')

    

def tocs(t0):

    # Timing function
    
    # Inputs:
    # t0: initial time
    
    # Outputs:
    # dt: elapsed time

    t1=timer()
    dt=t1-t0   

    return dt
    
#%%