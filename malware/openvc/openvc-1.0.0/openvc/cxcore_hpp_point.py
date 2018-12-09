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
import cxcore_hpp_point_ext as _ext
from cxcore_hpp_point_ext import *
        
#=============================================================================
# cxcore.hpp -- Point classes
#=============================================================================


vector_Point2i.__old_init__ = vector_Point2i.__init__
vector_Point2i.__init__ = _c.__vector__init__
vector_Point2i.create = _c.__vector_create
vector_Point2i.__repr__ = _c.__vector__repr__
vector_Point2i.tolist = _c.__vector_tolist
vector_Point2i.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Point2i()
_z.resize(1)
vector_Point2i.elem_type = _z[0].__class__
del(_z)
        
vector_vector_Point2i.__old_init__ = vector_vector_Point2i.__init__
vector_vector_Point2i.__init__ = _c.__vector__init__
vector_vector_Point2i.create = _c.__vector_create
vector_vector_Point2i.__repr__ = _c.__vector__repr__
vector_vector_Point2i.tolist = _c.__vector_tolist
vector_vector_Point2i.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_vector_Point2i()
_z.resize(1)
vector_vector_Point2i.elem_type = _z[0].__class__
del(_z)
        
def _Point2i__repr__(self):
    return "Point2i(x=" + repr(self.x) + ", y=" + repr(self.y) + ")"
Point2i.__repr__ = _Point2i__repr__
        
    
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Point2i that shares the same data with an ndarray instance, use: 'asPoint2i(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Point2i.__doc__ is None:
    Point2i.__doc__ = _str
else:
    Point2i.__doc__ += _str
    
def _Point2i__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Point2i.__getitem__ = _Point2i__getitem__
            
def _Point2i__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Point2i.__setitem__ = _Point2i__setitem__
            
def _Point2i__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Point2i.__getslice__ = _Point2i__getslice__
            
def _Point2i__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Point2i.__setslice__ = _Point2i__setslice__
            
def _Point2i__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Point2i.__iter__ = _Point2i__iter__
            
vector_Point2f.__old_init__ = vector_Point2f.__init__
vector_Point2f.__init__ = _c.__vector__init__
vector_Point2f.create = _c.__vector_create
vector_Point2f.__repr__ = _c.__vector__repr__
vector_Point2f.tolist = _c.__vector_tolist
vector_Point2f.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Point2f()
_z.resize(1)
vector_Point2f.elem_type = _z[0].__class__
del(_z)
        
vector_vector_Point2f.__old_init__ = vector_vector_Point2f.__init__
vector_vector_Point2f.__init__ = _c.__vector__init__
vector_vector_Point2f.create = _c.__vector_create
vector_vector_Point2f.__repr__ = _c.__vector__repr__
vector_vector_Point2f.tolist = _c.__vector_tolist
vector_vector_Point2f.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_vector_Point2f()
_z.resize(1)
vector_vector_Point2f.elem_type = _z[0].__class__
del(_z)
        
def _Point2f__repr__(self):
    return "Point2f(x=" + repr(self.x) + ", y=" + repr(self.y) + ")"
Point2f.__repr__ = _Point2f__repr__
        
    
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Point2f that shares the same data with an ndarray instance, use: 'asPoint2f(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Point2f.__doc__ is None:
    Point2f.__doc__ = _str
else:
    Point2f.__doc__ += _str
    
def _Point2f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Point2f.__getitem__ = _Point2f__getitem__
            
def _Point2f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Point2f.__setitem__ = _Point2f__setitem__
            
def _Point2f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Point2f.__getslice__ = _Point2f__getslice__
            
def _Point2f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Point2f.__setslice__ = _Point2f__setslice__
            
def _Point2f__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Point2f.__iter__ = _Point2f__iter__
            
vector_Point2d.__old_init__ = vector_Point2d.__init__
vector_Point2d.__init__ = _c.__vector__init__
vector_Point2d.create = _c.__vector_create
vector_Point2d.__repr__ = _c.__vector__repr__
vector_Point2d.tolist = _c.__vector_tolist
vector_Point2d.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Point2d()
_z.resize(1)
vector_Point2d.elem_type = _z[0].__class__
del(_z)
        
vector_vector_Point2d.__old_init__ = vector_vector_Point2d.__init__
vector_vector_Point2d.__init__ = _c.__vector__init__
vector_vector_Point2d.create = _c.__vector_create
vector_vector_Point2d.__repr__ = _c.__vector__repr__
vector_vector_Point2d.tolist = _c.__vector_tolist
vector_vector_Point2d.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_vector_Point2d()
_z.resize(1)
vector_vector_Point2d.elem_type = _z[0].__class__
del(_z)
        
def _Point2d__repr__(self):
    return "Point2d(x=" + repr(self.x) + ", y=" + repr(self.y) + ")"
Point2d.__repr__ = _Point2d__repr__
        
    
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Point2d that shares the same data with an ndarray instance, use: 'asPoint2d(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Point2d.__doc__ is None:
    Point2d.__doc__ = _str
else:
    Point2d.__doc__ += _str
    
def _Point2d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Point2d.__getitem__ = _Point2d__getitem__
            
def _Point2d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Point2d.__setitem__ = _Point2d__setitem__
            
def _Point2d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Point2d.__getslice__ = _Point2d__getslice__
            
def _Point2d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Point2d.__setslice__ = _Point2d__setslice__
            
def _Point2d__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Point2d.__iter__ = _Point2d__iter__
            
Seq_Point2i.__old_init__ = Seq_Point2i.__init__
def _Seq_Point2i__init__(self, *args, **kwds):
    Seq_Point2i.__old_init__(self, *args, **kwds)
    if args:
        self.depends = [args[0]]
    elif kwds:
        self.depends = [kwds.values()[0]]
    else:
        self.depends = []
_Seq_Point2i__init__.__doc__ = Seq_Point2i.__old_init__.__doc__    
Seq_Point2i.__init__ = _Seq_Point2i__init__
        
Seq_Point2i.__iter__ = _c.__sd_iter__;
        
Point = Point2i
Seq_Point = Seq_Point2i

vector_Point3i.__old_init__ = vector_Point3i.__init__
vector_Point3i.__init__ = _c.__vector__init__
vector_Point3i.create = _c.__vector_create
vector_Point3i.__repr__ = _c.__vector__repr__
vector_Point3i.tolist = _c.__vector_tolist
vector_Point3i.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Point3i()
_z.resize(1)
vector_Point3i.elem_type = _z[0].__class__
del(_z)
        
vector_vector_Point3i.__old_init__ = vector_vector_Point3i.__init__
vector_vector_Point3i.__init__ = _c.__vector__init__
vector_vector_Point3i.create = _c.__vector_create
vector_vector_Point3i.__repr__ = _c.__vector__repr__
vector_vector_Point3i.tolist = _c.__vector_tolist
vector_vector_Point3i.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_vector_Point3i()
_z.resize(1)
vector_vector_Point3i.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Point3i that shares the same data with an ndarray instance, use: 'asPoint3i(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Point3i.__doc__ is None:
    Point3i.__doc__ = _str
else:
    Point3i.__doc__ += _str
    
def _Point3i__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Point3i.__getitem__ = _Point3i__getitem__
            
def _Point3i__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Point3i.__setitem__ = _Point3i__setitem__
            
def _Point3i__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Point3i.__getslice__ = _Point3i__getslice__
            
def _Point3i__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Point3i.__setslice__ = _Point3i__setslice__
            
def _Point3i__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Point3i.__iter__ = _Point3i__iter__
            
def _Point3i__repr__(self):
    return "Point3i(x=" + repr(self.x) + ", y=" + repr(self.y) + ", z=" + repr(self.z) + ")"
Point3i.__repr__ = _Point3i__repr__
        
    
vector_Point3f.__old_init__ = vector_Point3f.__init__
vector_Point3f.__init__ = _c.__vector__init__
vector_Point3f.create = _c.__vector_create
vector_Point3f.__repr__ = _c.__vector__repr__
vector_Point3f.tolist = _c.__vector_tolist
vector_Point3f.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Point3f()
_z.resize(1)
vector_Point3f.elem_type = _z[0].__class__
del(_z)
        
vector_vector_Point3f.__old_init__ = vector_vector_Point3f.__init__
vector_vector_Point3f.__init__ = _c.__vector__init__
vector_vector_Point3f.create = _c.__vector_create
vector_vector_Point3f.__repr__ = _c.__vector__repr__
vector_vector_Point3f.tolist = _c.__vector_tolist
vector_vector_Point3f.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_vector_Point3f()
_z.resize(1)
vector_vector_Point3f.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Point3f that shares the same data with an ndarray instance, use: 'asPoint3f(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Point3f.__doc__ is None:
    Point3f.__doc__ = _str
else:
    Point3f.__doc__ += _str
    
def _Point3f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Point3f.__getitem__ = _Point3f__getitem__
            
def _Point3f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Point3f.__setitem__ = _Point3f__setitem__
            
def _Point3f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Point3f.__getslice__ = _Point3f__getslice__
            
def _Point3f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Point3f.__setslice__ = _Point3f__setslice__
            
def _Point3f__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Point3f.__iter__ = _Point3f__iter__
            
def _Point3f__repr__(self):
    return "Point3f(x=" + repr(self.x) + ", y=" + repr(self.y) + ", z=" + repr(self.z) + ")"
Point3f.__repr__ = _Point3f__repr__
        
    
vector_Point3d.__old_init__ = vector_Point3d.__init__
vector_Point3d.__init__ = _c.__vector__init__
vector_Point3d.create = _c.__vector_create
vector_Point3d.__repr__ = _c.__vector__repr__
vector_Point3d.tolist = _c.__vector_tolist
vector_Point3d.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Point3d()
_z.resize(1)
vector_Point3d.elem_type = _z[0].__class__
del(_z)
        
vector_vector_Point3d.__old_init__ = vector_vector_Point3d.__init__
vector_vector_Point3d.__init__ = _c.__vector__init__
vector_vector_Point3d.create = _c.__vector_create
vector_vector_Point3d.__repr__ = _c.__vector__repr__
vector_vector_Point3d.tolist = _c.__vector_tolist
vector_vector_Point3d.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_vector_Point3d()
_z.resize(1)
vector_vector_Point3d.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Point3d that shares the same data with an ndarray instance, use: 'asPoint3d(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Point3d.__doc__ is None:
    Point3d.__doc__ = _str
else:
    Point3d.__doc__ += _str
    
def _Point3d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Point3d.__getitem__ = _Point3d__getitem__
            
def _Point3d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Point3d.__setitem__ = _Point3d__setitem__
            
def _Point3d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Point3d.__getslice__ = _Point3d__getslice__
            
def _Point3d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Point3d.__setslice__ = _Point3d__setslice__
            
def _Point3d__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Point3d.__iter__ = _Point3d__iter__
            
def _Point3d__repr__(self):
    return "Point3d(x=" + repr(self.x) + ", y=" + repr(self.y) + ", z=" + repr(self.z) + ")"
Point3d.__repr__ = _Point3d__repr__
        
    
vector_Mat.__old_init__ = vector_Mat.__init__
vector_Mat.__init__ = _c.__vector__init__
vector_Mat.create = _c.__vector_create
vector_Mat.__repr__ = _c.__vector__repr__
vector_Mat.tolist = _c.__vector_tolist
vector_Mat.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Mat()
_z.resize(1)
vector_Mat.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Mat that shares the same data with an ndarray instance, use: 'asMat(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Mat.__doc__ is None:
    Mat.__doc__ = _str
else:
    Mat.__doc__ += _str
    
def _Mat__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Mat.__getitem__ = _Mat__getitem__
            
def _Mat__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Mat.__setitem__ = _Mat__setitem__
            
def _Mat__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Mat.__getslice__ = _Mat__getslice__
            
def _Mat__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Mat.__setslice__ = _Mat__setslice__
            
def _Mat__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Mat.__iter__ = _Mat__iter__
            
def _Mat__repr__(self):
    return "Mat()" if self.empty() else "Mat(rows=" + repr(self.rows)         + ", cols=" + repr(self.cols) + ", nchannels=" + repr(self.channels())         + ", depth=" + repr(self.depth()) + "):\n" + repr(self.ndarray)
Mat.__repr__ = _Mat__repr__

vector_Ptr_Mat.__old_init__ = vector_Ptr_Mat.__init__
vector_Ptr_Mat.__init__ = _c.__vector__init__
vector_Ptr_Mat.create = _c.__vector_create
vector_Ptr_Mat.__repr__ = _c.__vector__repr__
vector_Ptr_Mat.tolist = _c.__vector_tolist
vector_Ptr_Mat.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Ptr_Mat()
_z.resize(1)
vector_Ptr_Mat.elem_type = _z[0].__class__
del(_z)
        
vector_MatND.__old_init__ = vector_MatND.__init__
vector_MatND.__init__ = _c.__vector__init__
vector_MatND.create = _c.__vector_create
vector_MatND.__repr__ = _c.__vector__repr__
vector_MatND.tolist = _c.__vector_tolist
vector_MatND.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_MatND()
_z.resize(1)
vector_MatND.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of MatND that shares the same data with an ndarray instance, use: 'asMatND(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if MatND.__doc__ is None:
    MatND.__doc__ = _str
else:
    MatND.__doc__ += _str
    
def _MatND__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
MatND.__getitem__ = _MatND__getitem__
            
def _MatND__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
MatND.__setitem__ = _MatND__setitem__
            
def _MatND__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
MatND.__getslice__ = _MatND__getslice__
            
def _MatND__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
MatND.__setslice__ = _MatND__setslice__
            
def _MatND__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
MatND.__iter__ = _MatND__iter__
            
def _MatND__repr__(self):
    return "MatND(shape=" + repr(self.ndarray.shape) + ", nchannels=" + repr(self.channels())         + ", depth=" + repr(self.depth()) + "):\n" + repr(self.ndarray)
MatND.__repr__ = _MatND__repr__
