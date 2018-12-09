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

def __sd_iter__(self):
    for i in xrange(len(self)):
        yield self[i]


def __vector__repr__(self):
    n = len(self)
    s = "%s(len=%d, [" % (self.__class__.__name__, n)
    if n==1:
        s += repr(self[0])
    elif n==2:
        s += repr(self[0])+", "+repr(self[1])
    elif n==3:
        s += repr(self[0])+", "+repr(self[1])+", "+repr(self[2])
    elif n==4:
        s += repr(self[0])+", "+repr(self[1])+", "+repr(self[2])+", "+repr(self[3])
    elif n > 4:
        s += repr(self[0])+", "+repr(self[1])+", ..., "+repr(self[n-2])+", "+repr(self[n-1])
    s += "])"
    return s

def is_vector(cls):
    """Returns whether class 'cls' is a std::vector class."""
    return cls.__name__.startswith('vector_')
    
def __vector_create(self, obj):
    """Creates the vector from a Python sequence.
    
    Argument 'obj':
        a Python sequence
    """
    N = len(obj)
    self.resize(N)
    if is_vector(self.elem_type):
        for i in xrange(N):
            self[i] = self.elem_type.fromlist(obj[i])
    else:
        for i in xrange(N):
            self[i] = obj[i]

def __vector_tolist(self):
    if is_vector(self.elem_type):
        return [self[i].tolist() for i in xrange(len(self))]
    return [self[i] for i in xrange(len(self))]

def __vector_fromlist(cls, obj):
    """Creates a vector from a Python sequence.
    
    Argument 'obj':
        a Python sequence
    """
    z = cls()
    z.create(obj)
    return z
    
def __vector__init__(self, obj=None):
    """Initializes the vector.
    
    Argument 'obj':
        If 'obj' is an integer, the vector is initialized as a vector of 
        'obj' elements. If 'obj' is a Python sequence. The vector is
        initialized as an equivalence of 'obj' by invoking self.fromlist().
    """
    self.__old_init__()
    if isinstance(obj, int):
        self.resize(obj)
    elif not obj is None:
        self.create(obj)
    
