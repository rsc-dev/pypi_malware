#!/usr/bin/env python
# PyOpenCV - A Python wrapper for OpenCV 2.x using Boost.Python and NumPy

# Copyright (c) 2009, Minh-Tri Pham
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

#    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#    * Neither the name of pyopencv's copyright holders nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# For further inquiries, please contact Minh-Tri Pham at pmtri80@gmail.com.
# ----------------------------------------------------------------------------

import common as _c
import sdopencv_ext as _ext
from sdopencv_ext import *
        
import numpy as _np
    
#=============================================================================
# sdopencv
#=============================================================================

def cmpsum(arr, thresh=0, pos_val=1, neg_val=None):
    """Compares and sums up.
    
    Description:
        return numpy.sum(numpy.where(arr >= thresh, pos_val, neg_val), axis=-1)
        
    Input:
        arr : ndarray
            input array
        thresh : 1D ndarray or a number (default value: 0)
        pos_val : 1D ndarray or a number (default value: 1)
        neg_val : 1D ndarray or a number (default value: -pos_val)
    """
    if neg_val is None:
        neg_val = -pos_val
    return _np.sum(_np.where(arr >= thresh, pos_val, neg_val), axis=-1)

def vectorize_float64(pyfunc):
    """Performs 'numpy.vectorize(pyfunc)' assuming 'pyfunc' maps from float64 to float64"""
    try:
        f = _np.vectorize(pyfunc, otypes='d')
    except ValueError:
        from numpy.lib import function_base as fb
        old_func = fb._get_nargs
        fb._get_nargs = lambda obj: (1, 0)
        f = _np.vectorize(pyfunc, otypes='d')
        fb._get_nargs = old_func
        
    f2 = lambda x: f(_np.asarray(x, dtype=_np.float64))
    f2.__doc__ = f.__doc__
    
    return f2
