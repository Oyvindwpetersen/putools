
# -*- coding: utf-8 -*-
"""
Created on 

@author: OWP
"""

#%%

import numpy as np

#%%

def argmin(A,a_search):
    
    '''
    Find closest match of a in A
    
    Arguments
    ------------
    inputname (string): name of input file
    A (array): parent vector
    a_search (array): elements to find

    Returns
    ------------
    idx_min (array): indices of closest match
    
    '''

    if np.shape(a_search)==():
        ind_min=np.amin(np.abs(A-a_search))
        idx_min=ind_min
        
    if isinstance(a_search,list) or isinstance(a_search,np.ndarray):
    
        idx_min=np.zeros(np.shape(a_search),dtype=int) #*np.nan
        for k in np.arange(len(a_search)):
            ind_min=np.argmin(np.abs(A-a_search[k]))
            idx_min[k]=ind_min.astype('int')
        
    return idx_min

#%%

#%%

def listindexsub(L_all,target,casesens=False):
    
    '''
    Gives index of string among list of strings (partial match allowed)
    
    Arguments
    ------------
    L_all (list): parent
    target (string): search target
    casesens (bool): case sensitivity
    
    Returns
    ------------
    idx (list): indices of match
    
    '''

    if casesens==False:
        idx = [i for i, s in enumerate(L_all) if target.casefold() in s.casefold()]
    elif casesens==True:
        idx = [i for i, s in enumerate(L_all) if target in s]

    return idx


#%%

def listindexsingle(L_all,target):
    
    '''
    Find index of string within list of strings
    
    Arguments
    ------------
    L_all (list): parent
    target (string): search target
    
    Returns
    ------------
    idx_sub (number): indices of match
    
    '''
    
    try:
        idx_sub=L_all.index(target)        
    except:        
        idx_sub=None
        
    return idx_sub


def listindex(L_all,target):

    '''
    Find index of string(s) within list of strings (exact match, no partial)
    Error if no match or more than one match
    Case sensitive
    
    Arguments
    ------------
    L_all (list): parent
    target (list): search target
    
    Returns
    ------------
    idx (list): indices of match
    
    '''
    
    if isinstance(target,str):
        target=[target]
        
    idx=[None]*len(target)
    for k,target_sub in enumerate(target):
        
        idx_sub=listindexsingle(L_all,target_sub)
        
        if idx_sub==None:
            raise Exception('No match for ' + target_sub)
        else:
            
            # Check if any match in remainder of list
            idx_sub_check=listindexsingle(L_all[(idx_sub+1):],target_sub)
            
            if idx_sub_check is None: # Ok, no more matches for this word
                idx[k]=idx_sub
            else:
                print(idx_sub)
                print(idx_sub_check)
                raise Exception('Two or more matches for ' + target_sub)
                
        
    return idx

#%%

def num2stre(a,digits=6,delimeter=', '):
    
    '''
    Number(s) to string in scientific format
    
    Arguments
    ------------
    a (array): numbers to convert
    digits (int): digits behind comma
    delimeter (string): digits behind comma
    
    Returns
    ------------
    s (string): numbers separated with delimeter
    
    '''
    
    #format_exp='{:.6e}'
    format_exp='{:.' + str(digits) + 'e}'
    
    s='Empty_string'
    
    if isinstance(a,int):
        s=format_exp.format(a)
        
    elif isinstance(a,float):
        s=format_exp.format(a)
      
    elif isinstance(a,np.int32):
        s=format_exp.format(a)
          
    elif isinstance(a,list):
        
        s=''
        for a_element in a:
            s=s+format_exp.format(a_element) + delimeter
            
        s=s[0:(-1-len(delimeter))]
        
    elif isinstance(a,np.ndarray):
    
        s=''
        for a_element in np.nditer(a):
            s=s+np.format_float_scientific(a_element, unique=False, precision=digits) + delimeter
        
        s=s[0:(-len(delimeter))]
        
    return s

#%%

def num2strf(a,digits=6,delimeter=', '):
    
    '''
    Number(s) to string in float format
    
    Arguments
    ------------
    a (array): numbers to convert
    digits (int): digits behind comma
    delimeter (string): digits behind comma
    
    Returns
    ------------
    s (string): numbers separated with delimeter
    
    '''
    
    format_f='{:.6f}'
    format_f='{:.' + str(digits) + 'f}'

    s='Empty_string'

    if isinstance(a,int):
        s=format_f.format(a)
        
    elif isinstance(a,float):
        s=format_f.format(a)
        
    elif isinstance(a,np.int32):
        s=format_f.format(a)
         
    elif isinstance(a,list):
        
        s=''
        for a_element in a:
            s=s+format_f.format(a_element) + delimeter
            
        s=s[:(-1-len(delimeter))]
    elif isinstance(a,np.ndarray):
    
        s=''
        for a_element in np.nditer(a):
            s=s + format_f.format(a_element) + delimeter
        
        s=s[:(-len(delimeter))]
        
    return s

#%%

def rangebin(n,d):
    
    # Divide range into bins of given size
    # n=12,d=5 gives bin1=[1,2,3,4,5] bin2=[6,7,8,9,10] bin3=[11,12]

    # Inputs:
    # n: number
    # d: bin size
    
    # Outputs:
    # bins: list with bins indicies

    if n<=d:
        bins=[np.arange(n)]
    else:
        nbins=int(np.ceil(n/d))
        
        bins=[None]*nbins
        for k in range(nbins):
            bins[k]=k*d+np.arange(d)
            
        if bins[-1][-1]>n:
            bins[-1]=np.arange(bins[-2][-1]+1,n)
            
    return bins

#%%

def isnumeric(a):
    
    # Check if a is numeric, i.e. numpy or numbers in list

    # Inputs:
    # a: number

    # Outputs:
    # isnum: logical
    
    isnum=False    
    if isinstance(a,int):
        isnum=True
    elif isinstance(a,float):
        isnum=True
    elif isinstance(a,list):
        
        if len(a)>0:
            if isinstance(a[0],int):
                isnum=True
            elif isinstance(a[0],float):
                isnum=True
            elif isinstance(a[0],np.int32):
                isnum=True

                
    elif isinstance(a,np.ndarray):
        isnum=True

    if isinstance(a,bool):
        isnum=False   
        
    return isnum
            
#%%


def ensure_1d_list(N):
    # Check if N is a single number (int or float)
    if isinstance(N, (int, float)):
        return [N]
    
    # Check if N is a numpy array
    elif isinstance(N, np.ndarray):
        return N.flatten().tolist()
    
    # Check if N is a list
    elif isinstance(N, list):
        # Check if the list is already 1-dimensional
        if all(not isinstance(i, (list, np.ndarray)) for i in N):
            return N
        else:
            # Flatten the list if it contains nested lists or arrays
            return np.array(N).flatten().tolist()
    
    # Raise an error if N is of an unsupported type
    else:
        raise TypeError("Input must be an int, float, list, or numpy array.")
        
        


def ensurenp(a,Force1d=False):
    
    # Convert a number to numpy array

    # Inputs:
    # a: number
    # Force1d: keep vector format (not 2d)

    # Outputs:
    # b: numpy array

    if isinstance(a,np.ndarray):
        if np.shape(a)==():
            if Force1d==True:
                b=np.array([a])
            else:
                b=np.copy(a)
            
        else:
            b=np.copy(a)
        
    elif isinstance(a,int) or isinstance(a,float):
        if Force1d==True:
            b=np.array([a])
        else:
            b=np.array(a)
    
    elif isinstance(a,list):
        b=np.array(a)

    else:
        raise Exception('Not supported type of a')
    
    return b

#%%

def str2num(a_list,numformat='float',n_col=None):
    
    '''
    Convert list of strings to matrix
    
    Arguments
    ------------
    a_list (list): numbers to convert
    numformat (string): 'float' or 'int'
    n_col (int): number of columns to read
    
    Returns
    ------------
    M (array): numbers separated with delimeter
    
    '''

    if isinstance(a_list,str):
        a_list=[a_list]   
        
    # Testdata
    #a_list=[None]*2
    #a_list[0]='12.44, 212, 0.0001, 1e-3, -2, -2.21'
    #a_list[1]='-3.11e-3, 6e6, -212, , -2.0 , 55.99'

    # Find right size if none specified
    if n_col is None:
        n_col=len(a_list[0].split(','))
    
    n_row=len(a_list)
    
    M=np.zeros((n_row,n_col))*np.nan
    
    for k in np.arange(n_row):
        
        a_row=a_list[k].split(',')
        
        for j in np.arange(n_col):
        
            if a_row[j]=='' or a_row[j]==' ' or a_row[j]=='  ':
                #M[k,j]=0.0
                #continue
                a_row[j]='0.0'
            
            if numformat=='float':
                M[k,j]=float(a_row[j])
            elif numformat=='int':
                M[k,j]=int(a_row[j])
        
    
    return M

#%%

def genlabel(number,dof,midfix='_'):
    
    if isinstance(dof,str):
        if dof=='all':
            dof=['U1','U2','U3','UR1','UR2','UR3']
        else:
            dof=[dof]
        
    if isinstance(number,int):
        number=[number]
        
    if isinstance(number,np.int32):
        number=[number]
        
    if isinstance(number,float):
        number=[number]    

    A_label=[ str(int(number_sub)) + midfix + dof_sub for number_sub in number for dof_sub in dof]
        
    return A_label

#%%

def norm_fast(a):
    return sum(a*a)**0.5
    
#%%

#@nb.njit(fastmath=True)
def norm_fast_old(a):
    s = 0.
    for i in range(a.shape[0]):
        s += a[i]**2
    return np.sqrt(s)
    
#%%

def cross_fast(a,b):
    c=np.array([
        a[1]*b[2] - a[2]*b[1] ,
        a[2]*b[0] - a[0]*b[2] ,
        a[0]*b[1] - a[1]*b[0] ,
        ])
    
    return c

#%%

def block_diag_rep(A,r):

    m,n = A.shape
    out = np.zeros((r,m,r,n), dtype=A.dtype)
    diag = np.einsum('ijik->ijk',out)
    diag[:] = A
    
    return out.reshape(-1,n*r)


def printprogress(headers,values,formats=None,dispheader=True,n_spaces=8,n_dist=None):
    
    N=len(headers)
    
    if formats is None:
        formats=['{:.2e}']*N
    
    if N != len(values):
        print('***** Wrong length headers/values')
    
    if N != len(formats):
        print('***** Wrong length headers/formats')
    
    # headers=['Iter','Conv_check','Max r','Min r','Max dr','Min dr']
    # values=[10,np.pi/100,1.22,-2.4,0.22,-0.00022]
    # formats=['int','2e','2e','2e','2e','3e'];
    # dispheader=True
    
    
    for k in np.arange(N):
        if formats[k].endswith('e'):
            formats[k]='{:.' + formats[k] +'}'
        elif formats[k].endswith('f'):
            formats[k]='{:.' + formats[k] +'}'
        elif formats[k].endswith('int'):
            formats[k]='{:.0f}'
    
    header_line=''
    single_space=' '
    
    if n_dist is None:
        spaces=[n_spaces]*N
    
        # Cut spaces if header length exceed max length
        header_max=15
        for k in np.arange(N):
            if len(headers[k])>header_max:
                spaces[k]=spaces[k]-(len(headers[k])-header_max)

        # Build header
        sep=[None]*N
        for k in np.arange(N):
            
            header_line=header_line + single_space*spaces[k] + headers[k]
            sep[k]=len(header_line)
    
    else:
        if len(n_dist)==1:
            sep=np.cumsum(np.ones(N)*n_dist)
        else:
            sep=np.cumsum(n_dist)
        
        for k in np.arange(N):
            header_line=header_line + single_space*int(sep[k]-len(headers[k])-len(header_line)) + headers[k]

    header_line=header_line + single_space*4
    double_line='|' + '='*(len(header_line)-2) + '|'
    
   # Build line
    value_line=''
    for k in np.arange(N):
        
        if formats[k]=='bool':
            value_str=str(bool(values[k]))
        else:
            value_str=formats[k].format(values[k])
        
        spaces_v=int(sep[k]-len(value_line)-len(value_str))
        
        value_line=value_line + single_space*spaces_v + value_str

    # Display
    if dispheader:
        print(double_line)
        print(header_line)
        print(double_line)
    
    print(value_line)
    
