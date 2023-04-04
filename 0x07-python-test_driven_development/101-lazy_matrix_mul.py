import numpy as np
""" method hat multiplies 2 matrices 
by using the module NumPy
"""


def lazy_matrix_mul(m_a, m_b):
        """ Function that takes in 2 matrices and multiplies them
        Args:
            m_a: first matrix
            m_b: second matrix
        """
        return np.matmul(m_a, m_b)
