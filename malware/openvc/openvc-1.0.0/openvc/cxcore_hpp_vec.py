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
import cxcore_hpp_vec_ext as _ext
from cxcore_hpp_vec_ext import *
        
#=============================================================================
# cxcore.hpp -- Vec classes
#=============================================================================


vector_Vec6d.__old_init__ = vector_Vec6d.__init__
vector_Vec6d.__init__ = _c.__vector__init__
vector_Vec6d.create = _c.__vector_create
vector_Vec6d.__repr__ = _c.__vector__repr__
vector_Vec6d.tolist = _c.__vector_tolist
vector_Vec6d.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec6d()
_z.resize(1)
vector_Vec6d.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec6d that shares the same data with an ndarray instance, use: 'asVec6d(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec6d.__doc__ is None:
    Vec6d.__doc__ = _str
else:
    Vec6d.__doc__ += _str
    
def _Vec6d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec6d.__getitem__ = _Vec6d__getitem__
            
def _Vec6d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec6d.__setitem__ = _Vec6d__setitem__
            
def _Vec6d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec6d.__getslice__ = _Vec6d__getslice__
            
def _Vec6d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec6d.__setslice__ = _Vec6d__setslice__
            
def _Vec6d__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec6d.__iter__ = _Vec6d__iter__
            
def _Vec6d__repr__(self):
    return "Vec6d(" + self.ndarray.__str__() + ")"
Vec6d.__repr__ = _Vec6d__repr__
    
vector_Vec2w.__old_init__ = vector_Vec2w.__init__
vector_Vec2w.__init__ = _c.__vector__init__
vector_Vec2w.create = _c.__vector_create
vector_Vec2w.__repr__ = _c.__vector__repr__
vector_Vec2w.tolist = _c.__vector_tolist
vector_Vec2w.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec2w()
_z.resize(1)
vector_Vec2w.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec2w that shares the same data with an ndarray instance, use: 'asVec2w(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec2w.__doc__ is None:
    Vec2w.__doc__ = _str
else:
    Vec2w.__doc__ += _str
    
def _Vec2w__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec2w.__getitem__ = _Vec2w__getitem__
            
def _Vec2w__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec2w.__setitem__ = _Vec2w__setitem__
            
def _Vec2w__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec2w.__getslice__ = _Vec2w__getslice__
            
def _Vec2w__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec2w.__setslice__ = _Vec2w__setslice__
            
def _Vec2w__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec2w.__iter__ = _Vec2w__iter__
            
def _Vec2w__repr__(self):
    return "Vec2w(" + self.ndarray.__str__() + ")"
Vec2w.__repr__ = _Vec2w__repr__
    
vector_Vec3s.__old_init__ = vector_Vec3s.__init__
vector_Vec3s.__init__ = _c.__vector__init__
vector_Vec3s.create = _c.__vector_create
vector_Vec3s.__repr__ = _c.__vector__repr__
vector_Vec3s.tolist = _c.__vector_tolist
vector_Vec3s.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec3s()
_z.resize(1)
vector_Vec3s.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec3s that shares the same data with an ndarray instance, use: 'asVec3s(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec3s.__doc__ is None:
    Vec3s.__doc__ = _str
else:
    Vec3s.__doc__ += _str
    
def _Vec3s__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec3s.__getitem__ = _Vec3s__getitem__
            
def _Vec3s__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec3s.__setitem__ = _Vec3s__setitem__
            
def _Vec3s__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec3s.__getslice__ = _Vec3s__getslice__
            
def _Vec3s__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec3s.__setslice__ = _Vec3s__setslice__
            
def _Vec3s__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec3s.__iter__ = _Vec3s__iter__
            
def _Vec3s__repr__(self):
    return "Vec3s(" + self.ndarray.__str__() + ")"
Vec3s.__repr__ = _Vec3s__repr__
    
vector_Vec2i.__old_init__ = vector_Vec2i.__init__
vector_Vec2i.__init__ = _c.__vector__init__
vector_Vec2i.create = _c.__vector_create
vector_Vec2i.__repr__ = _c.__vector__repr__
vector_Vec2i.tolist = _c.__vector_tolist
vector_Vec2i.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec2i()
_z.resize(1)
vector_Vec2i.elem_type = _z[0].__class__
del(_z)
        
vector_vector_Vec2i.__old_init__ = vector_vector_Vec2i.__init__
vector_vector_Vec2i.__init__ = _c.__vector__init__
vector_vector_Vec2i.create = _c.__vector_create
vector_vector_Vec2i.__repr__ = _c.__vector__repr__
vector_vector_Vec2i.tolist = _c.__vector_tolist
vector_vector_Vec2i.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_vector_Vec2i()
_z.resize(1)
vector_vector_Vec2i.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec2i that shares the same data with an ndarray instance, use: 'asVec2i(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec2i.__doc__ is None:
    Vec2i.__doc__ = _str
else:
    Vec2i.__doc__ += _str
    
def _Vec2i__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec2i.__getitem__ = _Vec2i__getitem__
            
def _Vec2i__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec2i.__setitem__ = _Vec2i__setitem__
            
def _Vec2i__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec2i.__getslice__ = _Vec2i__getslice__
            
def _Vec2i__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec2i.__setslice__ = _Vec2i__setslice__
            
def _Vec2i__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec2i.__iter__ = _Vec2i__iter__
            
def _Vec2i__repr__(self):
    return "Vec2i(" + self.ndarray.__str__() + ")"
Vec2i.__repr__ = _Vec2i__repr__
    
vector_Vec4w.__old_init__ = vector_Vec4w.__init__
vector_Vec4w.__init__ = _c.__vector__init__
vector_Vec4w.create = _c.__vector_create
vector_Vec4w.__repr__ = _c.__vector__repr__
vector_Vec4w.tolist = _c.__vector_tolist
vector_Vec4w.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec4w()
_z.resize(1)
vector_Vec4w.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec4w that shares the same data with an ndarray instance, use: 'asVec4w(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec4w.__doc__ is None:
    Vec4w.__doc__ = _str
else:
    Vec4w.__doc__ += _str
    
def _Vec4w__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec4w.__getitem__ = _Vec4w__getitem__
            
def _Vec4w__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec4w.__setitem__ = _Vec4w__setitem__
            
def _Vec4w__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec4w.__getslice__ = _Vec4w__getslice__
            
def _Vec4w__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec4w.__setslice__ = _Vec4w__setslice__
            
def _Vec4w__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec4w.__iter__ = _Vec4w__iter__
            
def _Vec4w__repr__(self):
    return "Vec4w(" + self.ndarray.__str__() + ")"
Vec4w.__repr__ = _Vec4w__repr__
    
vector_Vec3w.__old_init__ = vector_Vec3w.__init__
vector_Vec3w.__init__ = _c.__vector__init__
vector_Vec3w.create = _c.__vector_create
vector_Vec3w.__repr__ = _c.__vector__repr__
vector_Vec3w.tolist = _c.__vector_tolist
vector_Vec3w.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec3w()
_z.resize(1)
vector_Vec3w.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec3w that shares the same data with an ndarray instance, use: 'asVec3w(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec3w.__doc__ is None:
    Vec3w.__doc__ = _str
else:
    Vec3w.__doc__ += _str
    
def _Vec3w__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec3w.__getitem__ = _Vec3w__getitem__
            
def _Vec3w__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec3w.__setitem__ = _Vec3w__setitem__
            
def _Vec3w__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec3w.__getslice__ = _Vec3w__getslice__
            
def _Vec3w__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec3w.__setslice__ = _Vec3w__setslice__
            
def _Vec3w__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec3w.__iter__ = _Vec3w__iter__
            
def _Vec3w__repr__(self):
    return "Vec3w(" + self.ndarray.__str__() + ")"
Vec3w.__repr__ = _Vec3w__repr__
    
vector_Vec4b.__old_init__ = vector_Vec4b.__init__
vector_Vec4b.__init__ = _c.__vector__init__
vector_Vec4b.create = _c.__vector_create
vector_Vec4b.__repr__ = _c.__vector__repr__
vector_Vec4b.tolist = _c.__vector_tolist
vector_Vec4b.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec4b()
_z.resize(1)
vector_Vec4b.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec4b that shares the same data with an ndarray instance, use: 'asVec4b(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec4b.__doc__ is None:
    Vec4b.__doc__ = _str
else:
    Vec4b.__doc__ += _str
    
def _Vec4b__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec4b.__getitem__ = _Vec4b__getitem__
            
def _Vec4b__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec4b.__setitem__ = _Vec4b__setitem__
            
def _Vec4b__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec4b.__getslice__ = _Vec4b__getslice__
            
def _Vec4b__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec4b.__setslice__ = _Vec4b__setslice__
            
def _Vec4b__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec4b.__iter__ = _Vec4b__iter__
            
def _Vec4b__repr__(self):
    return "Vec4b(" + self.ndarray.__str__() + ")"
Vec4b.__repr__ = _Vec4b__repr__
    
vector_Vec3b.__old_init__ = vector_Vec3b.__init__
vector_Vec3b.__init__ = _c.__vector__init__
vector_Vec3b.create = _c.__vector_create
vector_Vec3b.__repr__ = _c.__vector__repr__
vector_Vec3b.tolist = _c.__vector_tolist
vector_Vec3b.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec3b()
_z.resize(1)
vector_Vec3b.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec3b that shares the same data with an ndarray instance, use: 'asVec3b(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec3b.__doc__ is None:
    Vec3b.__doc__ = _str
else:
    Vec3b.__doc__ += _str
    
def _Vec3b__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec3b.__getitem__ = _Vec3b__getitem__
            
def _Vec3b__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec3b.__setitem__ = _Vec3b__setitem__
            
def _Vec3b__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec3b.__getslice__ = _Vec3b__getslice__
            
def _Vec3b__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec3b.__setslice__ = _Vec3b__setslice__
            
def _Vec3b__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec3b.__iter__ = _Vec3b__iter__
            
def _Vec3b__repr__(self):
    return "Vec3b(" + self.ndarray.__str__() + ")"
Vec3b.__repr__ = _Vec3b__repr__
    
vector_Vec2b.__old_init__ = vector_Vec2b.__init__
vector_Vec2b.__init__ = _c.__vector__init__
vector_Vec2b.create = _c.__vector_create
vector_Vec2b.__repr__ = _c.__vector__repr__
vector_Vec2b.tolist = _c.__vector_tolist
vector_Vec2b.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec2b()
_z.resize(1)
vector_Vec2b.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec2b that shares the same data with an ndarray instance, use: 'asVec2b(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec2b.__doc__ is None:
    Vec2b.__doc__ = _str
else:
    Vec2b.__doc__ += _str
    
def _Vec2b__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec2b.__getitem__ = _Vec2b__getitem__
            
def _Vec2b__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec2b.__setitem__ = _Vec2b__setitem__
            
def _Vec2b__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec2b.__getslice__ = _Vec2b__getslice__
            
def _Vec2b__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec2b.__setslice__ = _Vec2b__setslice__
            
def _Vec2b__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec2b.__iter__ = _Vec2b__iter__
            
def _Vec2b__repr__(self):
    return "Vec2b(" + self.ndarray.__str__() + ")"
Vec2b.__repr__ = _Vec2b__repr__
    
vector_Vec4s.__old_init__ = vector_Vec4s.__init__
vector_Vec4s.__init__ = _c.__vector__init__
vector_Vec4s.create = _c.__vector_create
vector_Vec4s.__repr__ = _c.__vector__repr__
vector_Vec4s.tolist = _c.__vector_tolist
vector_Vec4s.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec4s()
_z.resize(1)
vector_Vec4s.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec4s that shares the same data with an ndarray instance, use: 'asVec4s(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec4s.__doc__ is None:
    Vec4s.__doc__ = _str
else:
    Vec4s.__doc__ += _str
    
def _Vec4s__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec4s.__getitem__ = _Vec4s__getitem__
            
def _Vec4s__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec4s.__setitem__ = _Vec4s__setitem__
            
def _Vec4s__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec4s.__getslice__ = _Vec4s__getslice__
            
def _Vec4s__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec4s.__setslice__ = _Vec4s__setslice__
            
def _Vec4s__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec4s.__iter__ = _Vec4s__iter__
            
def _Vec4s__repr__(self):
    return "Vec4s(" + self.ndarray.__str__() + ")"
Vec4s.__repr__ = _Vec4s__repr__
    
vector_Vec2s.__old_init__ = vector_Vec2s.__init__
vector_Vec2s.__init__ = _c.__vector__init__
vector_Vec2s.create = _c.__vector_create
vector_Vec2s.__repr__ = _c.__vector__repr__
vector_Vec2s.tolist = _c.__vector_tolist
vector_Vec2s.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec2s()
_z.resize(1)
vector_Vec2s.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec2s that shares the same data with an ndarray instance, use: 'asVec2s(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec2s.__doc__ is None:
    Vec2s.__doc__ = _str
else:
    Vec2s.__doc__ += _str
    
def _Vec2s__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec2s.__getitem__ = _Vec2s__getitem__
            
def _Vec2s__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec2s.__setitem__ = _Vec2s__setitem__
            
def _Vec2s__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec2s.__getslice__ = _Vec2s__getslice__
            
def _Vec2s__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec2s.__setslice__ = _Vec2s__setslice__
            
def _Vec2s__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec2s.__iter__ = _Vec2s__iter__
            
def _Vec2s__repr__(self):
    return "Vec2s(" + self.ndarray.__str__() + ")"
Vec2s.__repr__ = _Vec2s__repr__
    
vector_Vec4i.__old_init__ = vector_Vec4i.__init__
vector_Vec4i.__init__ = _c.__vector__init__
vector_Vec4i.create = _c.__vector_create
vector_Vec4i.__repr__ = _c.__vector__repr__
vector_Vec4i.tolist = _c.__vector_tolist
vector_Vec4i.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec4i()
_z.resize(1)
vector_Vec4i.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec4i that shares the same data with an ndarray instance, use: 'asVec4i(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec4i.__doc__ is None:
    Vec4i.__doc__ = _str
else:
    Vec4i.__doc__ += _str
    
def _Vec4i__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec4i.__getitem__ = _Vec4i__getitem__
            
def _Vec4i__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec4i.__setitem__ = _Vec4i__setitem__
            
def _Vec4i__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec4i.__getslice__ = _Vec4i__getslice__
            
def _Vec4i__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec4i.__setslice__ = _Vec4i__setslice__
            
def _Vec4i__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec4i.__iter__ = _Vec4i__iter__
            
def _Vec4i__repr__(self):
    return "Vec4i(" + self.ndarray.__str__() + ")"
Vec4i.__repr__ = _Vec4i__repr__
    
vector_Vec3i.__old_init__ = vector_Vec3i.__init__
vector_Vec3i.__init__ = _c.__vector__init__
vector_Vec3i.create = _c.__vector_create
vector_Vec3i.__repr__ = _c.__vector__repr__
vector_Vec3i.tolist = _c.__vector_tolist
vector_Vec3i.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec3i()
_z.resize(1)
vector_Vec3i.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec3i that shares the same data with an ndarray instance, use: 'asVec3i(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec3i.__doc__ is None:
    Vec3i.__doc__ = _str
else:
    Vec3i.__doc__ += _str
    
def _Vec3i__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec3i.__getitem__ = _Vec3i__getitem__
            
def _Vec3i__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec3i.__setitem__ = _Vec3i__setitem__
            
def _Vec3i__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec3i.__getslice__ = _Vec3i__getslice__
            
def _Vec3i__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec3i.__setslice__ = _Vec3i__setslice__
            
def _Vec3i__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec3i.__iter__ = _Vec3i__iter__
            
def _Vec3i__repr__(self):
    return "Vec3i(" + self.ndarray.__str__() + ")"
Vec3i.__repr__ = _Vec3i__repr__
    
vector_Vec6f.__old_init__ = vector_Vec6f.__init__
vector_Vec6f.__init__ = _c.__vector__init__
vector_Vec6f.create = _c.__vector_create
vector_Vec6f.__repr__ = _c.__vector__repr__
vector_Vec6f.tolist = _c.__vector_tolist
vector_Vec6f.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec6f()
_z.resize(1)
vector_Vec6f.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec6f that shares the same data with an ndarray instance, use: 'asVec6f(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec6f.__doc__ is None:
    Vec6f.__doc__ = _str
else:
    Vec6f.__doc__ += _str
    
def _Vec6f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec6f.__getitem__ = _Vec6f__getitem__
            
def _Vec6f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec6f.__setitem__ = _Vec6f__setitem__
            
def _Vec6f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec6f.__getslice__ = _Vec6f__getslice__
            
def _Vec6f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec6f.__setslice__ = _Vec6f__setslice__
            
def _Vec6f__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec6f.__iter__ = _Vec6f__iter__
            
def _Vec6f__repr__(self):
    return "Vec6f(" + self.ndarray.__str__() + ")"
Vec6f.__repr__ = _Vec6f__repr__
    
vector_Vec4f.__old_init__ = vector_Vec4f.__init__
vector_Vec4f.__init__ = _c.__vector__init__
vector_Vec4f.create = _c.__vector_create
vector_Vec4f.__repr__ = _c.__vector__repr__
vector_Vec4f.tolist = _c.__vector_tolist
vector_Vec4f.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec4f()
_z.resize(1)
vector_Vec4f.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec4f that shares the same data with an ndarray instance, use: 'asVec4f(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec4f.__doc__ is None:
    Vec4f.__doc__ = _str
else:
    Vec4f.__doc__ += _str
    
def _Vec4f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec4f.__getitem__ = _Vec4f__getitem__
            
def _Vec4f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec4f.__setitem__ = _Vec4f__setitem__
            
def _Vec4f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec4f.__getslice__ = _Vec4f__getslice__
            
def _Vec4f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec4f.__setslice__ = _Vec4f__setslice__
            
def _Vec4f__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec4f.__iter__ = _Vec4f__iter__
            
def _Vec4f__repr__(self):
    return "Vec4f(" + self.ndarray.__str__() + ")"
Vec4f.__repr__ = _Vec4f__repr__
    
vector_Vec3f.__old_init__ = vector_Vec3f.__init__
vector_Vec3f.__init__ = _c.__vector__init__
vector_Vec3f.create = _c.__vector_create
vector_Vec3f.__repr__ = _c.__vector__repr__
vector_Vec3f.tolist = _c.__vector_tolist
vector_Vec3f.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec3f()
_z.resize(1)
vector_Vec3f.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec3f that shares the same data with an ndarray instance, use: 'asVec3f(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec3f.__doc__ is None:
    Vec3f.__doc__ = _str
else:
    Vec3f.__doc__ += _str
    
def _Vec3f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec3f.__getitem__ = _Vec3f__getitem__
            
def _Vec3f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec3f.__setitem__ = _Vec3f__setitem__
            
def _Vec3f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec3f.__getslice__ = _Vec3f__getslice__
            
def _Vec3f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec3f.__setslice__ = _Vec3f__setslice__
            
def _Vec3f__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec3f.__iter__ = _Vec3f__iter__
            
def _Vec3f__repr__(self):
    return "Vec3f(" + self.ndarray.__str__() + ")"
Vec3f.__repr__ = _Vec3f__repr__
    
vector_Vec2f.__old_init__ = vector_Vec2f.__init__
vector_Vec2f.__init__ = _c.__vector__init__
vector_Vec2f.create = _c.__vector_create
vector_Vec2f.__repr__ = _c.__vector__repr__
vector_Vec2f.tolist = _c.__vector_tolist
vector_Vec2f.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec2f()
_z.resize(1)
vector_Vec2f.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec2f that shares the same data with an ndarray instance, use: 'asVec2f(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec2f.__doc__ is None:
    Vec2f.__doc__ = _str
else:
    Vec2f.__doc__ += _str
    
def _Vec2f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec2f.__getitem__ = _Vec2f__getitem__
            
def _Vec2f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec2f.__setitem__ = _Vec2f__setitem__
            
def _Vec2f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec2f.__getslice__ = _Vec2f__getslice__
            
def _Vec2f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec2f.__setslice__ = _Vec2f__setslice__
            
def _Vec2f__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec2f.__iter__ = _Vec2f__iter__
            
def _Vec2f__repr__(self):
    return "Vec2f(" + self.ndarray.__str__() + ")"
Vec2f.__repr__ = _Vec2f__repr__
    
vector_Vec4d.__old_init__ = vector_Vec4d.__init__
vector_Vec4d.__init__ = _c.__vector__init__
vector_Vec4d.create = _c.__vector_create
vector_Vec4d.__repr__ = _c.__vector__repr__
vector_Vec4d.tolist = _c.__vector_tolist
vector_Vec4d.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec4d()
_z.resize(1)
vector_Vec4d.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec4d that shares the same data with an ndarray instance, use: 'asVec4d(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec4d.__doc__ is None:
    Vec4d.__doc__ = _str
else:
    Vec4d.__doc__ += _str
    
def _Vec4d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec4d.__getitem__ = _Vec4d__getitem__
            
def _Vec4d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec4d.__setitem__ = _Vec4d__setitem__
            
def _Vec4d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec4d.__getslice__ = _Vec4d__getslice__
            
def _Vec4d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec4d.__setslice__ = _Vec4d__setslice__
            
def _Vec4d__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec4d.__iter__ = _Vec4d__iter__
            
def _Vec4d__repr__(self):
    return "Vec4d(" + self.ndarray.__str__() + ")"
Vec4d.__repr__ = _Vec4d__repr__
    
vector_Vec3d.__old_init__ = vector_Vec3d.__init__
vector_Vec3d.__init__ = _c.__vector__init__
vector_Vec3d.create = _c.__vector_create
vector_Vec3d.__repr__ = _c.__vector__repr__
vector_Vec3d.tolist = _c.__vector_tolist
vector_Vec3d.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec3d()
_z.resize(1)
vector_Vec3d.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec3d that shares the same data with an ndarray instance, use: 'asVec3d(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec3d.__doc__ is None:
    Vec3d.__doc__ = _str
else:
    Vec3d.__doc__ += _str
    
def _Vec3d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec3d.__getitem__ = _Vec3d__getitem__
            
def _Vec3d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec3d.__setitem__ = _Vec3d__setitem__
            
def _Vec3d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec3d.__getslice__ = _Vec3d__getslice__
            
def _Vec3d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec3d.__setslice__ = _Vec3d__setslice__
            
def _Vec3d__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec3d.__iter__ = _Vec3d__iter__
            
def _Vec3d__repr__(self):
    return "Vec3d(" + self.ndarray.__str__() + ")"
Vec3d.__repr__ = _Vec3d__repr__
    
vector_Vec2d.__old_init__ = vector_Vec2d.__init__
vector_Vec2d.__init__ = _c.__vector__init__
vector_Vec2d.create = _c.__vector_create
vector_Vec2d.__repr__ = _c.__vector__repr__
vector_Vec2d.tolist = _c.__vector_tolist
vector_Vec2d.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Vec2d()
_z.resize(1)
vector_Vec2d.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Vec2d that shares the same data with an ndarray instance, use: 'asVec2d(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec2d.__doc__ is None:
    Vec2d.__doc__ = _str
else:
    Vec2d.__doc__ += _str
    
def _Vec2d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec2d.__getitem__ = _Vec2d__getitem__
            
def _Vec2d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec2d.__setitem__ = _Vec2d__setitem__
            
def _Vec2d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec2d.__getslice__ = _Vec2d__getslice__
            
def _Vec2d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec2d.__setslice__ = _Vec2d__setslice__
            
def _Vec2d__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Vec2d.__iter__ = _Vec2d__iter__
            
def _Vec2d__repr__(self):
    return "Vec2d(" + self.ndarray.__str__() + ")"
Vec2d.__repr__ = _Vec2d__repr__
    
def _Complexd__repr__(self):
    return "Complexd(re=" + repr(self.re) + ", im=" + repr(self.im) + ")"
Complexd.__repr__ = _Complexd__repr__
    
def _Complexf__repr__(self):
    return "Complexf(re=" + repr(self.re) + ", im=" + repr(self.im) + ")"
Complexf.__repr__ = _Complexf__repr__
    
vector_Scalar.__old_init__ = vector_Scalar.__init__
vector_Scalar.__init__ = _c.__vector__init__
vector_Scalar.create = _c.__vector_create
vector_Scalar.__repr__ = _c.__vector__repr__
vector_Scalar.tolist = _c.__vector_tolist
vector_Scalar.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Scalar()
_z.resize(1)
vector_Scalar.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Scalar that shares the same data with an ndarray instance, use: 'asScalar(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Scalar.__doc__ is None:
    Scalar.__doc__ = _str
else:
    Scalar.__doc__ += _str
    
def _Scalar__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Scalar.__getitem__ = _Scalar__getitem__
            
def _Scalar__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Scalar.__setitem__ = _Scalar__setitem__
            
def _Scalar__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Scalar.__getslice__ = _Scalar__getslice__
            
def _Scalar__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Scalar.__setslice__ = _Scalar__setslice__
            
def _Scalar__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Scalar.__iter__ = _Scalar__iter__
            
def _Scalar__repr__(self):
    return "Scalar(" + self.ndarray.__str__() + ")"
Scalar.__repr__ = _Scalar__repr__

# Constructs a color value
def CV_RGB(r, g, b):
    return Scalar(b, g, r)


vector_Range.__old_init__ = vector_Range.__init__
vector_Range.__init__ = _c.__vector__init__
vector_Range.create = _c.__vector_create
vector_Range.__repr__ = _c.__vector__repr__
vector_Range.tolist = _c.__vector_tolist
vector_Range.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Range()
_z.resize(1)
vector_Range.elem_type = _z[0].__class__
del(_z)
        
_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    Alternatively, you could create a reference to 'ndarray' by using 'asndarray(obj)', where 'obj' is an instance of this class.\n    \n    To create an instance of Range that shares the same data with an ndarray instance, use: 'asRange(a),\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Range.__doc__ is None:
    Range.__doc__ = _str
else:
    Range.__doc__ += _str
    
def _Range__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Range.__getitem__ = _Range__getitem__
            
def _Range__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Range.__setitem__ = _Range__setitem__
            
def _Range__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Range.__getslice__ = _Range__getslice__
            
def _Range__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Range.__setslice__ = _Range__setslice__
            
def _Range__iter__(self, *args, **kwds):
    return self.ndarray.__iter__(*args, **kwds)
Range.__iter__ = _Range__iter__
            
def _Range__repr__(self):
    return "Range(start=" + repr(self.start) + ", end=" + repr(self.end) + ")"
Range.__repr__ = _Range__repr__
        
CV_WHOLE_SEQ_END_INDEX = 0x3fffffff
CV_WHOLE_SEQ = Range(0, CV_WHOLE_SEQ_END_INDEX)
CV_WHOLE_ARR  = Range( 0, 0x3fffffff )

