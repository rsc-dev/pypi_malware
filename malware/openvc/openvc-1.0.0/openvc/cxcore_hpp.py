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
import cxcore_hpp_ext as _ext
from cxcore_hpp_ext import *
        
#=============================================================================
# cxcore.hpp
#=============================================================================


vector_Size2i.__old_init__ = vector_Size2i.__init__
vector_Size2i.__init__ = _c.__vector__init__
vector_Size2i.create = _c.__vector_create
vector_Size2i.__repr__ = _c.__vector__repr__
vector_Size2i.tolist = _c.__vector_tolist
vector_Size2i.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Size2i()
_z.resize(1)
vector_Size2i.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Size2i that shares the same data with an ndarray instance, use: 'asSize2i(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Size2i.__doc__ is None:
    Size2i.__doc__ = _str
else:
    Size2i.__doc__ += _str
    
def _Size2i__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Size2i.__getitem__ = _Size2i__getitem__
            
def _Size2i__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Size2i.__setitem__ = _Size2i__setitem__
            
def _Size2i__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Size2i.__getslice__ = _Size2i__getslice__
            
def _Size2i__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Size2i.__setslice__ = _Size2i__setslice__
            
def _Size2i__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Size2i.__iter__ = _Size2i__iter__
            
def _Size2i__repr__(self):
    return "Size2i(width=" + repr(self.width) + ", height=" + repr(self.height) + ")"
Size2i.__repr__ = _Size2i__repr__
        
    
vector_Size2f.__old_init__ = vector_Size2f.__init__
vector_Size2f.__init__ = _c.__vector__init__
vector_Size2f.create = _c.__vector_create
vector_Size2f.__repr__ = _c.__vector__repr__
vector_Size2f.tolist = _c.__vector_tolist
vector_Size2f.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Size2f()
_z.resize(1)
vector_Size2f.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Size2f that shares the same data with an ndarray instance, use: 'asSize2f(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Size2f.__doc__ is None:
    Size2f.__doc__ = _str
else:
    Size2f.__doc__ += _str
    
def _Size2f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Size2f.__getitem__ = _Size2f__getitem__
            
def _Size2f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Size2f.__setitem__ = _Size2f__setitem__
            
def _Size2f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Size2f.__getslice__ = _Size2f__getslice__
            
def _Size2f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Size2f.__setslice__ = _Size2f__setslice__
            
def _Size2f__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Size2f.__iter__ = _Size2f__iter__
            
def _Size2f__repr__(self):
    return "Size2f(width=" + repr(self.width) + ", height=" + repr(self.height) + ")"
Size2f.__repr__ = _Size2f__repr__
        
    
Size = Size2i

vector_Rect.__old_init__ = vector_Rect.__init__
vector_Rect.__init__ = _c.__vector__init__
vector_Rect.create = _c.__vector_create
vector_Rect.__repr__ = _c.__vector__repr__
vector_Rect.tolist = _c.__vector_tolist
vector_Rect.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Rect()
_z.resize(1)
vector_Rect.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Rect that shares the same data with an ndarray instance, use: 'asRect(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Rect.__doc__ is None:
    Rect.__doc__ = _str
else:
    Rect.__doc__ += _str
    
def _Rect__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Rect.__getitem__ = _Rect__getitem__
            
def _Rect__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Rect.__setitem__ = _Rect__setitem__
            
def _Rect__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Rect.__getslice__ = _Rect__getslice__
            
def _Rect__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Rect.__setslice__ = _Rect__setslice__
            
def _Rect__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Rect.__iter__ = _Rect__iter__
            
def _Rect__repr__(self):
    return "Rect(x=" + repr(self.x) + ", y=" + repr(self.y) + \
        ", width=" + repr(self.width) + ", height=" + repr(self.height) + ")"
Rect.__repr__ = _Rect__repr__
        
    
vector_RotatedRect.__old_init__ = vector_RotatedRect.__init__
vector_RotatedRect.__init__ = _c.__vector__init__
vector_RotatedRect.create = _c.__vector_create
vector_RotatedRect.__repr__ = _c.__vector__repr__
vector_RotatedRect.tolist = _c.__vector_tolist
vector_RotatedRect.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_RotatedRect()
_z.resize(1)
vector_RotatedRect.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of RotatedRect that shares the same data with an ndarray instance, use: 'asRotatedRect(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if RotatedRect.__doc__ is None:
    RotatedRect.__doc__ = _str
else:
    RotatedRect.__doc__ += _str
    
def _RotatedRect__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
RotatedRect.__getitem__ = _RotatedRect__getitem__
            
def _RotatedRect__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
RotatedRect.__setitem__ = _RotatedRect__setitem__
            
def _RotatedRect__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
RotatedRect.__getslice__ = _RotatedRect__getslice__
            
def _RotatedRect__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
RotatedRect.__setslice__ = _RotatedRect__setslice__
            
def _RotatedRect__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
RotatedRect.__iter__ = _RotatedRect__iter__
            
def _RotatedRect__repr__(self):
    return "RotatedRect(center=" + repr(self.center) + ", size=" + repr(self.size) + \
        ", angle=" + repr(self.angle) + ")"
RotatedRect.__repr__ = _RotatedRect__repr__
        

def _RNG__repr__(self):
    return "RNG(state=" + repr(self.state) + ")"
RNG.__repr__ = _RNG__repr__
    

def _TermCriteria__repr__(self):
    return "TermCriteria(type=" + repr(self.type) + ", maxCount=" + repr(self.maxCount) + \
        ", epsilon=" + repr(self.epsilon) + ")"
TermCriteria.__repr__ = _TermCriteria__repr__
    

vector_KDTree_Node.__old_init__ = vector_KDTree_Node.__init__
vector_KDTree_Node.__init__ = _c.__vector__init__
vector_KDTree_Node.create = _c.__vector_create
vector_KDTree_Node.__repr__ = _c.__vector__repr__
vector_KDTree_Node.tolist = _c.__vector_tolist
vector_KDTree_Node.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_KDTree_Node()
_z.resize(1)
vector_KDTree_Node.elem_type = _z[0].__class__
del(_z)
        
Seq_int.__old_init__ = Seq_int.__init__
def _Seq_int__init__(self, *args, **kwds):
    Seq_int.__old_init__(self, *args, **kwds)
    if args:
        self.depends = [args[0]]
    elif kwds:
        self.depends = [kwds.values()[0]]
    else:
        self.depends = []
_Seq_int__init__.__doc__ = Seq_int.__old_init__.__doc__    
Seq_int.__init__ = _Seq_int__init__
        
Seq_int.__iter__ = _c.__sd_iter__;
        