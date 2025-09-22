#!/usr/bin/python3
import numpy as np
"""Summery
"""


def lazy_matrix_mul(m_a, m_b):
    """_summary_

    Args:
        m_a (_type_): _description_
        m_b (_type_): _description_

    Raises:
        TypeError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    if type(np.array(m_a)) is not np.ndarray:
        raise TypeError("m_a must be a numpy array")
    if type(np.array(m_b)) is not np.ndarray:
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
    """
    
    
    
    try:
        result = np.array(m_a) @ np.array(m_b)
    except Exception as err:
        print(err)
        print(type(err))
    else:
        return result
        
