#!/usr/bin/python3
import numpy as np

def matrix_mul(m_a, m_b):
    """
    """
    if type(m_a) is not np.ndarray:
        raise TypeError("m_a must be a numpy array")
    if type(m_b) is not np.ndarray:
        raise TypeError("m_b must be a numpy array")
    
    if False in [type(m_a[i]) == np.ndarray for i in range(len(m_a))]:
        raise TypeError("m_a must be a numpy array of numpy arrays")
    
    if False in [type(m_b[i]) == np.ndarray for i in range(len(m_b))]:
        raise TypeError("m_b must be a numpy array of numpy arrays")
    
    if m_a.size == 0:
        raise ValueError("m_a can't be empty")
    if m_b.size == 0:
        raise ValueError("m_b can't be empty")
    
    if not np.issubdtype(m_a.dtype, np.number):
        raise TypeError("m_a should contain only integers or floats")
    if not np.issubdtype(m_b.dtype, np.number):
        raise TypeError("m_b should contain only integers or floats")
    
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("m_a must be the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("m_b must be the same size")
    
    try:
        result = m_a * m_b
    except Exception:
        raise TypeError("m_a and m_b can't be multiplied")
    else:
        return result
        
