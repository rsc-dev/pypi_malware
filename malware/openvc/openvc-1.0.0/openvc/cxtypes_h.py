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
import cxtypes_h_ext as _ext
from cxtypes_h_ext import *
        
vector_int8.__old_init__ = vector_int8.__init__
vector_int8.__init__ = _c.__vector__init__
vector_int8.create = _c.__vector_create
vector_int8.__repr__ = _c.__vector__repr__
vector_int8.tolist = _c.__vector_tolist
vector_int8.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_int8()
_z.resize(1)
vector_int8.elem_type = _z[0].__class__
del(_z)
        
vector_uint8.__old_init__ = vector_uint8.__init__
vector_uint8.__init__ = _c.__vector__init__
vector_uint8.create = _c.__vector_create
vector_uint8.__repr__ = _c.__vector__repr__
vector_uint8.tolist = _c.__vector_tolist
vector_uint8.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_uint8()
_z.resize(1)
vector_uint8.elem_type = _z[0].__class__
del(_z)
        
vector_int16.__old_init__ = vector_int16.__init__
vector_int16.__init__ = _c.__vector__init__
vector_int16.create = _c.__vector_create
vector_int16.__repr__ = _c.__vector__repr__
vector_int16.tolist = _c.__vector_tolist
vector_int16.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_int16()
_z.resize(1)
vector_int16.elem_type = _z[0].__class__
del(_z)
        
vector_uint16.__old_init__ = vector_uint16.__init__
vector_uint16.__init__ = _c.__vector__init__
vector_uint16.create = _c.__vector_create
vector_uint16.__repr__ = _c.__vector__repr__
vector_uint16.tolist = _c.__vector_tolist
vector_uint16.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_uint16()
_z.resize(1)
vector_uint16.elem_type = _z[0].__class__
del(_z)
        
vector_int.__old_init__ = vector_int.__init__
vector_int.__init__ = _c.__vector__init__
vector_int.create = _c.__vector_create
vector_int.__repr__ = _c.__vector__repr__
vector_int.tolist = _c.__vector_tolist
vector_int.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_int()
_z.resize(1)
vector_int.elem_type = _z[0].__class__
del(_z)
        
vector_uint.__old_init__ = vector_uint.__init__
vector_uint.__init__ = _c.__vector__init__
vector_uint.create = _c.__vector_create
vector_uint.__repr__ = _c.__vector__repr__
vector_uint.tolist = _c.__vector_tolist
vector_uint.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_uint()
_z.resize(1)
vector_uint.elem_type = _z[0].__class__
del(_z)
        
vector_long.__old_init__ = vector_long.__init__
vector_long.__init__ = _c.__vector__init__
vector_long.create = _c.__vector_create
vector_long.__repr__ = _c.__vector__repr__
vector_long.tolist = _c.__vector_tolist
vector_long.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_long()
_z.resize(1)
vector_long.elem_type = _z[0].__class__
del(_z)
        
vector_ulong.__old_init__ = vector_ulong.__init__
vector_ulong.__init__ = _c.__vector__init__
vector_ulong.create = _c.__vector_create
vector_ulong.__repr__ = _c.__vector__repr__
vector_ulong.tolist = _c.__vector_tolist
vector_ulong.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_ulong()
_z.resize(1)
vector_ulong.elem_type = _z[0].__class__
del(_z)
        
vector_int64.__old_init__ = vector_int64.__init__
vector_int64.__init__ = _c.__vector__init__
vector_int64.create = _c.__vector_create
vector_int64.__repr__ = _c.__vector__repr__
vector_int64.tolist = _c.__vector_tolist
vector_int64.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_int64()
_z.resize(1)
vector_int64.elem_type = _z[0].__class__
del(_z)
        
vector_uint64.__old_init__ = vector_uint64.__init__
vector_uint64.__init__ = _c.__vector__init__
vector_uint64.create = _c.__vector_create
vector_uint64.__repr__ = _c.__vector__repr__
vector_uint64.tolist = _c.__vector_tolist
vector_uint64.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_uint64()
_z.resize(1)
vector_uint64.elem_type = _z[0].__class__
del(_z)
        
vector_float32.__old_init__ = vector_float32.__init__
vector_float32.__init__ = _c.__vector__init__
vector_float32.create = _c.__vector_create
vector_float32.__repr__ = _c.__vector__repr__
vector_float32.tolist = _c.__vector_tolist
vector_float32.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_float32()
_z.resize(1)
vector_float32.elem_type = _z[0].__class__
del(_z)
        
vector_float64.__old_init__ = vector_float64.__init__
vector_float64.__init__ = _c.__vector__init__
vector_float64.create = _c.__vector_create
vector_float64.__repr__ = _c.__vector__repr__
vector_float64.tolist = _c.__vector_tolist
vector_float64.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_float64()
_z.resize(1)
vector_float64.elem_type = _z[0].__class__
del(_z)
        
vector_vector_int.__old_init__ = vector_vector_int.__init__
vector_vector_int.__init__ = _c.__vector__init__
vector_vector_int.create = _c.__vector_create
vector_vector_int.__repr__ = _c.__vector__repr__
vector_vector_int.tolist = _c.__vector_tolist
vector_vector_int.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_vector_int()
_z.resize(1)
vector_vector_int.elem_type = _z[0].__class__
del(_z)
        
vector_vector_float32.__old_init__ = vector_vector_float32.__init__
vector_vector_float32.__init__ = _c.__vector__init__
vector_vector_float32.create = _c.__vector_create
vector_vector_float32.__repr__ = _c.__vector__repr__
vector_vector_float32.tolist = _c.__vector_tolist
vector_vector_float32.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_vector_float32()
_z.resize(1)
vector_vector_float32.elem_type = _z[0].__class__
del(_z)
        
import math as _m
import ctypes as _CT

#=============================================================================
# cxtypes.h
#=============================================================================



#-----------------------------------------------------------------------------
# Common macros and inline functions
#-----------------------------------------------------------------------------

CV_PI = _m.pi
CV_LOG2 = 0.69314718055994530941723212145818


#-----------------------------------------------------------------------------
# Random number generation
#-----------------------------------------------------------------------------

    

#-----------------------------------------------------------------------------
# Matrix type (CvMat) 
#-----------------------------------------------------------------------------

# Matrix type (CvMat)
CV_CN_MAX = 64
CV_CN_SHIFT = 3
CV_DEPTH_MAX = (1 << CV_CN_SHIFT)

CV_8U = 0
CV_8S = 1
CV_16U = 2
CV_16S = 3
CV_32S = 4
CV_32F = 5
CV_64F = 6
CV_USRTYPE1 = 7

def CV_MAKETYPE(depth,cn):
    return ((depth) + (((cn)-1) << CV_CN_SHIFT))
CV_MAKE_TYPE = CV_MAKETYPE

CV_8UC1 = CV_MAKETYPE(CV_8U,1)
CV_8UC2 = CV_MAKETYPE(CV_8U,2)
CV_8UC3 = CV_MAKETYPE(CV_8U,3)
CV_8UC4 = CV_MAKETYPE(CV_8U,4)

CV_8SC1 = CV_MAKETYPE(CV_8S,1)
CV_8SC2 = CV_MAKETYPE(CV_8S,2)
CV_8SC3 = CV_MAKETYPE(CV_8S,3)
CV_8SC4 = CV_MAKETYPE(CV_8S,4)

CV_16UC1 = CV_MAKETYPE(CV_16U,1)
CV_16UC2 = CV_MAKETYPE(CV_16U,2)
CV_16UC3 = CV_MAKETYPE(CV_16U,3)
CV_16UC4 = CV_MAKETYPE(CV_16U,4)

CV_16SC1 = CV_MAKETYPE(CV_16S,1)
CV_16SC2 = CV_MAKETYPE(CV_16S,2)
CV_16SC3 = CV_MAKETYPE(CV_16S,3)
CV_16SC4 = CV_MAKETYPE(CV_16S,4)

CV_32SC1 = CV_MAKETYPE(CV_32S,1)
CV_32SC2 = CV_MAKETYPE(CV_32S,2)
CV_32SC3 = CV_MAKETYPE(CV_32S,3)
CV_32SC4 = CV_MAKETYPE(CV_32S,4)

CV_32FC1 = CV_MAKETYPE(CV_32F,1)
CV_32FC2 = CV_MAKETYPE(CV_32F,2)
CV_32FC3 = CV_MAKETYPE(CV_32F,3)
CV_32FC4 = CV_MAKETYPE(CV_32F,4)

CV_64FC1 = CV_MAKETYPE(CV_64F,1)
CV_64FC2 = CV_MAKETYPE(CV_64F,2)
CV_64FC3 = CV_MAKETYPE(CV_64F,3)
CV_64FC4 = CV_MAKETYPE(CV_64F,4)

CV_AUTOSTEP = 0x7fffffff

CV_MAT_CN_MASK = ((CV_CN_MAX - 1) << CV_CN_SHIFT)
def CV_MAT_CN(flags):
    return ((((flags) & CV_MAT_CN_MASK) >> CV_CN_SHIFT) + 1)
CV_MAT_DEPTH_MASK = (CV_DEPTH_MAX - 1)
def CV_MAT_DEPTH(flags):
    return ((flags) & CV_MAT_DEPTH_MASK)
CV_MAT_TYPE_MASK = (CV_DEPTH_MAX*CV_CN_MAX - 1)
def CV_MAT_TYPE(flags):
    ((flags) & CV_MAT_TYPE_MASK)
CV_MAT_CONT_FLAG_SHIFT = 9
CV_MAT_CONT_FLAG = (1 << CV_MAT_CONT_FLAG_SHIFT)
def CV_IS_MAT_CONT(flags):
    return ((flags) & CV_MAT_CONT_FLAG)
CV_IS_CONT_MAT = CV_IS_MAT_CONT
CV_MAT_TEMP_FLAG_SHIFT = 10
CV_MAT_TEMP_FLAG = (1 << CV_MAT_TEMP_FLAG_SHIFT)
def CV_IS_TEMP_MAT(flags):
    return ((flags) & CV_MAT_TEMP_FLAG)

CV_MAGIC_MASK = 0xFFFF0000
CV_MAT_MAGIC_VAL = 0x42420000
CV_TYPE_NAME_MAT = "opencv-matrix"



#-----------------------------------------------------------------------------
# Multi-dimensional dense array (CvMatND)
#-----------------------------------------------------------------------------

CV_MATND_MAGIC_VAL    = 0x42430000
CV_TYPE_NAME_MATND    = "opencv-nd-matrix"

CV_MAX_DIM = 32
CV_MAX_DIM_HEAP = (1 << 16)


#-----------------------------------------------------------------------------
# Multi-dimensional sparse array (CvSparseMat) 
#-----------------------------------------------------------------------------

CV_SPARSE_MAT_MAGIC_VAL    = 0x42440000
CV_TYPE_NAME_SPARSE_MAT    = "opencv-sparse-matrix"



#-----------------------------------------------------------------------------
# Other supplementary data type definitions
#-----------------------------------------------------------------------------

# CV_TERMCRIT_ITER    = 1
# CV_TERMCRIT_NUMBER  = CV_TERMCRIT_ITER
# CV_TERMCRIT_EPS     = 2


def _CvPoint__repr__(self):
    return "CvPoint(x=" + repr(self.x) + ", y=" + repr(self.y) + ")"
CvPoint.__repr__ = _CvPoint__repr__
        

def _CvPoint2D32f__repr__(self):
    return "CvPoint2D32f(x=" + repr(self.x) + ", y=" + repr(self.y) + ")"
CvPoint2D32f.__repr__ = _CvPoint2D32f__repr__
        

def _CvPoint2D64f__repr__(self):
    return "CvPoint2D64f(x=" + repr(self.x) + ", y=" + repr(self.y) + ")"
CvPoint2D64f.__repr__ = _CvPoint2D64f__repr__
        

def _CvPoint3D32f__repr__(self):
    return "CvPoint3D32f(x=" + repr(self.x) + ", y=" + repr(self.y) + ", z=" + repr(self.z) + ")"
CvPoint3D32f.__repr__ = _CvPoint3D32f__repr__
        

def _CvPoint3D64f__repr__(self):
    return "CvPoint3D64f(x=" + repr(self.x) + ", y=" + repr(self.y) + ", z=" + repr(self.z) + ")"
CvPoint3D64f.__repr__ = _CvPoint3D64f__repr__
        

#-----------------------------------------------------------------------------
# Dynamic Data structures
#-----------------------------------------------------------------------------

CV_STORAGE_MAGIC_VAL = 0x42890000

CV_TYPE_NAME_SEQ             = "opencv-sequence"
CV_TYPE_NAME_SEQ_TREE        = "opencv-sequence-tree"

CV_SET_ELEM_IDX_MASK   = ((1 << 26) - 1)
CV_SET_ELEM_FREE_FLAG  = (1 << (_CT.sizeof(_CT.c_int)*8-1))

# Checks whether the element pointed by ptr belongs to a set or not
def CV_IS_SET_ELEM(ptr):
    return cast(ptr, CvSetElem_p)[0].flags >= 0

CV_TYPE_NAME_GRAPH = "opencv-graph"



#-----------------------------------------------------------------------------
# Sequence types
#-----------------------------------------------------------------------------

#Viji Periapoilan 5/21/2007(start)

CV_SEQ_MAGIC_VAL            = 0x42990000

#define CV_IS_SEQ(seq) #    ((seq) != NULL && (((CvSeq*)(seq))->flags & CV_MAGIC_MASK) == CV_SEQ_MAGIC_VAL)

CV_SET_MAGIC_VAL           = 0x42980000
#define CV_IS_SET(set) #    ((set) != NULL && (((CvSeq*)(set))->flags & CV_MAGIC_MASK) == CV_SET_MAGIC_VAL)

CV_SEQ_ELTYPE_BITS         = 9
CV_SEQ_ELTYPE_MASK         =  ((1 << CV_SEQ_ELTYPE_BITS) - 1)
CV_SEQ_ELTYPE_POINT        =  CV_32SC2  #/* (x,y) */
CV_SEQ_ELTYPE_CODE         = CV_8UC1   #/* freeman code: 0..7 */
CV_SEQ_ELTYPE_GENERIC      =  0
CV_SEQ_ELTYPE_PTR          =  CV_USRTYPE1
CV_SEQ_ELTYPE_PPOINT       =  CV_SEQ_ELTYPE_PTR  #/* &(x,y) */
CV_SEQ_ELTYPE_INDEX        =  CV_32SC1  #/* #(x,y) */
CV_SEQ_ELTYPE_GRAPH_EDGE   =  0  #/* &next_o, &next_d, &vtx_o, &vtx_d */
CV_SEQ_ELTYPE_GRAPH_VERTEX =  0  #/* first_edge, &(x,y) */
CV_SEQ_ELTYPE_TRIAN_ATR    =  0  #/* vertex of the binary tree   */
CV_SEQ_ELTYPE_CONNECTED_COMP= 0  #/* connected component  */
CV_SEQ_ELTYPE_POINT3D      =  CV_32FC3  #/* (x,y,z)  */

CV_SEQ_KIND_BITS           = 3
CV_SEQ_KIND_MASK           = (((1 << CV_SEQ_KIND_BITS) - 1)<<CV_SEQ_ELTYPE_BITS)


# types of sequences
CV_SEQ_KIND_GENERIC        = (0 << CV_SEQ_ELTYPE_BITS)
CV_SEQ_KIND_CURVE          = (1 << CV_SEQ_ELTYPE_BITS)
CV_SEQ_KIND_BIN_TREE       = (2 << CV_SEQ_ELTYPE_BITS)

#Viji Periapoilan 5/21/2007(end)

# types of sparse sequences (sets)
CV_SEQ_KIND_GRAPH       = (3 << CV_SEQ_ELTYPE_BITS)
CV_SEQ_KIND_SUBDIV2D    = (4 << CV_SEQ_ELTYPE_BITS)

CV_SEQ_FLAG_SHIFT       = (CV_SEQ_KIND_BITS + CV_SEQ_ELTYPE_BITS)

# flags for curves
CV_SEQ_FLAG_CLOSED     = (1 << CV_SEQ_FLAG_SHIFT)
CV_SEQ_FLAG_SIMPLE     = (2 << CV_SEQ_FLAG_SHIFT)
CV_SEQ_FLAG_CONVEX     = (4 << CV_SEQ_FLAG_SHIFT)
CV_SEQ_FLAG_HOLE       = (8 << CV_SEQ_FLAG_SHIFT)

# flags for graphs
CV_GRAPH_FLAG_ORIENTED = (1 << CV_SEQ_FLAG_SHIFT)

CV_GRAPH               = CV_SEQ_KIND_GRAPH
CV_ORIENTED_GRAPH      = (CV_SEQ_KIND_GRAPH|CV_GRAPH_FLAG_ORIENTED)

# point sets
CV_SEQ_POINT_SET       = (CV_SEQ_KIND_GENERIC| CV_SEQ_ELTYPE_POINT)
CV_SEQ_POINT3D_SET     = (CV_SEQ_KIND_GENERIC| CV_SEQ_ELTYPE_POINT3D)
CV_SEQ_POLYLINE        = (CV_SEQ_KIND_CURVE  | CV_SEQ_ELTYPE_POINT)
CV_SEQ_POLYGON         = (CV_SEQ_FLAG_CLOSED | CV_SEQ_POLYLINE )
CV_SEQ_CONTOUR         = CV_SEQ_POLYGON
CV_SEQ_SIMPLE_POLYGON  = (CV_SEQ_FLAG_SIMPLE | CV_SEQ_POLYGON  )

# chain-coded curves
CV_SEQ_CHAIN           = (CV_SEQ_KIND_CURVE  | CV_SEQ_ELTYPE_CODE)
CV_SEQ_CHAIN_CONTOUR   = (CV_SEQ_FLAG_CLOSED | CV_SEQ_CHAIN)

# binary tree for the contour
CV_SEQ_POLYGON_TREE    = (CV_SEQ_KIND_BIN_TREE  | CV_SEQ_ELTYPE_TRIAN_ATR)

# sequence of the connected components
CV_SEQ_CONNECTED_COMP  = (CV_SEQ_KIND_GENERIC  | CV_SEQ_ELTYPE_CONNECTED_COMP)

# sequence of the integer numbers
CV_SEQ_INDEX           = (CV_SEQ_KIND_GENERIC  | CV_SEQ_ELTYPE_INDEX)

# CV_SEQ_ELTYPE( seq )   = ((seq)->flags & CV_SEQ_ELTYPE_MASK)
# CV_SEQ_KIND( seq )     = ((seq)->flags & CV_SEQ_KIND_MASK )

def CV_GET_SEQ_ELEM(TYPE, seq, index):
    result = cvGetSeqElem(seq, index)
    return cast(result, POINTER(TYPE))



#-----------------------------------------------------------------------------
# Data structures for persistence (a.k.a serialization) functionality
#-----------------------------------------------------------------------------

CV_STORAGE_READ = 0
CV_STORAGE_WRITE = 1
CV_STORAGE_WRITE_TEXT = CV_STORAGE_WRITE
CV_STORAGE_WRITE_BINARY = CV_STORAGE_WRITE
CV_STORAGE_APPEND = 2

CV_NODE_NONE        = 0
CV_NODE_INT         = 1
CV_NODE_INTEGER     = CV_NODE_INT
CV_NODE_REAL        = 2
CV_NODE_FLOAT       = CV_NODE_REAL
CV_NODE_STR         = 3
CV_NODE_STRING      = CV_NODE_STR
CV_NODE_REF         = 4 # not used
CV_NODE_SEQ         = 5
CV_NODE_MAP         = 6
CV_NODE_TYPE_MASK   = 7

def CV_NODE_TYPE(flags):
    return flags & CV_NODE_TYPE_MASK

# file node flags
CV_NODE_FLOW        = 8 # used only for writing structures to YAML format
CV_NODE_USER        = 16
CV_NODE_EMPTY       = 32
CV_NODE_NAMED       = 64

def CV_NODE_IS_INT(flags):
    return CV_NODE_TYPE(flags) == CV_NODE_INT
    
def CV_NODE_IS_REAL(flags):
    return CV_NODE_TYPE(flags) == CV_NODE_REAL
    
def CV_NODE_IS_STRING(flags):
    return CV_NODE_TYPE(flags) == CV_NODE_STRING
    
def CV_NODE_IS_SEQ(flags):
    return CV_NODE_TYPE(flags) == CV_NODE_SEQ
    
def CV_NODE_IS_MAP(flags):
    return CV_NODE_TYPE(flags) == CV_NODE_MAP
    
def CV_NODE_IS_COLLECTION(flags):
    return CV_NODE_TYPE(flags) >= CV_NODE_SEQ
    
def CV_NODE_IS_FLOW(flags):
    return bool(flags & CV_NODE_FLOW)
    
def CV_NODE_IS_EMPTY(flags):
    return bool(flags & CV_NODE_EMPTY)
    
def CV_NODE_IS_USER(flags):
    return bool(flags & CV_NODE_USER)
    
def CV_NODE_HAS_NAME(flags):
    return bool(flags & CV_NODE_NAMED)

CV_NODE_SEQ_SIMPLE = 256
def CV_NODE_SEQ_IS_SIMPLE(seq):
    return bool(seq[0].flags & CV_NODE_SEQ_SIMPLE)


