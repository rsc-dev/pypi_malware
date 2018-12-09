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
"""PyOpenCV - A Python wrapper for OpenCV 2.x using Boost.Python and NumPy

Copyright (c) 2009, Minh-Tri Pham
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

   * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
   * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
   * Neither the name of pyopencv's copyright holders nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

For further inquiries, please contact Minh-Tri Pham at pmtri80@gmail.com.
"""

# Try to import numpy
try:
    import numpy as _NP
except ImportError:
    raise ImportError("NumPy is not found in your system. Please install NumPy of version at least 1.2.0.")

if _NP.version.version < '1.2.0':
    raise ImportError("NumPy is installed but its version is too old (%s detected). Please install NumPy of version at least 1.2.0." % _NP.version.version)

import config as _cfg
import functools as _fc

def _smart_import(global_dict):
    cvt_dict = {}
    for item in _cfg.__dict__:
        val = _cfg.__dict__[item]
        if item.startswith('convert_') and '_to_' in item:
            klass1, klass2 = item[8:].split('_to_')
            if not klass2 in cvt_dict:
                cvt_dict[klass2] = {}
            cvt_dict[klass2][klass1] = val
        else:
            global_dict[item] = val
            
    def convert(the_dict, x):
        try:
            f = the_dict[x.__class__.__name__]
        except KeyError:
            raise TypeError("Unable to convert from an object of type '%s'" % x.__class__.__name__)
        return f(x)
                
    for item in cvt_dict:
        func = _fc.partial(convert, cvt_dict[item])
        func.__doc__ = """Converts an object into an object of type %s

    The type of the input object must be one of the followings:
        %s
    Whenever possible, the output object shares the same data with the 
    input object.""" % (item, cvt_dict[item].keys())
        global_dict['as%s' % item] = func

_smart_import(globals())

if 'asMat' in globals():
    # rewrite the asMat function
    def reshapeSingleChannel(mat):
        """Reshapes a Mat object into one that has a single channel.

    The function returns mat itself if it is single-channel.

    If it is multi-channel, the function invokes mat.reshape() to reshape
    the object. If the object has a single row, the returning object has
    rows=mat.cols and cols=mat.channels(). Otherwise, the returning object
    has rows=mat.rows and cols=mat.cols*mat.channels().    
        """
        if mat.channels() != 1:
            new_mat = mat.reshape(1, mat.cols if mat.rows==1 else mat.rows)
            if '_depends' in mat.__dict__:
                new_mat._depends = mat._depends
            return new_mat
        return mat

    _asMat = asMat    
    def asMat(obj, force_single_channel=False):
        """Converts a Python object into a Mat object.

    This general-purpose meta-function uses a simple heuristic method to
    identify the type of the given Python object in order to convert it into
    a Mat object. First, it invokes the internal asMat() function of the
    Python extension to try to convert. If not successful, it assumes the 
    object is a Python sequence, and converts the object into a std::vector 
    object whose element type is the type of the first element of the Python 
    sequence. After that, it converts the std::vector object into a Mat 
    object by invoking the internal asMat() function again.
    
    In the case that the above heuristic method does not convert into a Mat
    object with your intended type and depth, use one of the asvector_...()
    functions to convert your object into a vector before invoking asMat().
    
    If 'force_single_channel' is True, the returning Mat is single-channel (by
    invoking reshapeSingleChannel()). Otherwise, PyOpenCV tries to return a 
    multi-channel Mat whenever possible.
        """
        
        if obj is None:
            return Mat()
            
        try:
            out_mat = _asMat(obj)
        except KeyError:
            z = obj[0]
            if isinstance(z, int):
                t = vector_int.fromlist(obj)
            elif isinstance(z, float):
                t = vector_float64.fromlist(obj)
            else:
                t = eval("vector_%s.fromlist(obj)" % z.__class__.__name__)
            out_mat = _asMat(t)
        
        if force_single_channel:
            return reshapeSingleChannel(out_mat)
        return out_mat
    asMat.__doc__ = asMat.__doc__ + """
Docstring of the internal asMat function:

    """ + _asMat.__doc__

if 'asPoint2i' in globals():
    asPoint = asPoint2i
