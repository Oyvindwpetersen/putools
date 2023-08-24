
# -*- coding: utf-8 -*-
"""
Created on 

@author: OWP
"""

#%%

import numpy as np
from . import num
#%%

def starprint(A_list,n=0):

    # Print message 

    # Inputs: 
    # A_list: list or string with message
    # n: number of 25-star lines

    star_25='*************************'
    star_5='***** '
    
    if isinstance(A_list,str):
        A_list=[A_list]
    
    for k in np.arange(n):
        print(star_25)
        
    for A_list_sub in A_list:
        print(star_5 + A_list_sub)
        
    for k in np.arange(n):
        print(star_25)
        
        


def readfile(InputFileName):

    # Read file to list
    
    # Inputs:
    # InputFileName: filename
    
    # Outputs:
    # inputfilelines: list with each line as string

    fid=open(InputFileName,'r')
    inputfilelines=fid.read().splitlines()
    fid.close()
    
    return inputfilelines
    
#https://stackoverflow.com/questions/60618271/python-find-index-of-unique-substring-contained-in-list-of-strings-without-go


def writematrix(fid,matrix,digits=3,delimeter=', ',list_format='e'):
    
    # Write matrix to file  

    # Inputs:
    # fid: file identifier
    # matrix: vector or matrix with numbers 
    # digits: number of digits
    # delimeter: delimeter between numbers
    # list_format: e,f, or int (for all numbers same format) or [int,e,e] for different for each column
    
    matrix=np.atleast_2d(matrix)
    (n_row,n_col)=np.shape(matrix)

    if isinstance(list_format,str):
        list_format=[list_format]
        
    if len(list_format)==1:
        list_format=n_col*list_format;
    
    for k in np.arange(n_row):
        
        str_row=''
        a_el_str='None '
        for j in np.arange(n_col):
            if list_format[j]=='int':
                a_el_str=str(int(matrix[k,j]))
            elif list_format[j]=='e':
                a_el_str=num.num2stre(matrix[k,j],digits)
            elif list_format[j]=='f':
                a_el_str=num.num2strf(matrix[k,j],digits)
            else:
                raise Exception('Invalid format: ' + list_format[j])
                
            str_row=str_row + a_el_str + delimeter
            
        str_row=str_row[:(-len(delimeter))] + '\n'    

        fid.write(str_row)

#%%