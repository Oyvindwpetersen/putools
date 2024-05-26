
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
        
        
def findsubstr(full_str,sub_str):
    
    '''
    Find all indices at which substring occurs in longer string
    
    Arguments
    ------------
    full_str (str): full string
    sub_str (str): substring
    
    Returns
    ------------
    index: list with indices
    
    '''
    
        
    return [
        index
        for index in range(len(full_str) - len(sub_str) + 1)
        if full_str[index:].startswith(sub_str)
    ]
    
    # https://stackoverflow.com/questions/60618271/python-find-index-of-unique-substring-contained-in-list-of-strings-without-go

def readfile(file_name,encode='utf-8'):

    '''
    Read text file
    
    Arguments
    ------------
    fid: file identifier
    file_name (str): filename including folder
    encode (str): encoding
    
    Returns
    ------------
    inputfilelines: list with each line as string
    
    '''
    
    fid=open(file_name,'r',encoding=encode)
    inputfilelines=fid.read().splitlines()
    fid.close()
    
    return inputfilelines
    

def writematrix(fid,matrix,digits=3,delimeter=', ',format='e'):
    
    '''
    Write matrix to text file
    
    Arguments
    ------------
    fid: file identifier
    matrix (np array): vector or matrix with numbers 
    digits (int): number of digits
    delimeter (str): between numbers
    format (str): 'e','f', or 'int' or ['int','e','e'] for different for each column
    
    Returns
    ------------
    None
    
    '''
    
    matrix=np.atleast_2d(matrix)
    (n_row,n_col)=np.shape(matrix)

    # Ensure list
    if isinstance(format,str):
        format=[format]

    # If uniform format, copy for all columns
    if len(format)==1:
        format=n_col*format;
    
    for k in np.arange(n_row):
        
        str_row=''
        tmp_str='None '
        for j in np.arange(n_col):
            if format[j]=='int':
                tmp_str=str(int(matrix[k,j]))
            elif format[j]=='e':
                tmp_str=num.num2stre(matrix[k,j],digits)
            elif format[j]=='f':
                tmp_str=num.num2strf(matrix[k,j],digits)
            else:
                raise Exception('Invalid format: ' + format[j])
                
            str_row=str_row + tmp_str + delimeter
            
         
        str_row=str_row[:(-len(delimeter))] + '\n'    

        fid.write(str_row)

