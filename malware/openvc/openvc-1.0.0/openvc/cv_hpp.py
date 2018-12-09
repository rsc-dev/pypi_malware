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
import cv_hpp_ext as _ext
from cv_hpp_ext import *
        
#=============================================================================
# cv.hpp
#=============================================================================



vector_DTreeNode.__old_init__ = vector_DTreeNode.__init__
vector_DTreeNode.__init__ = _c.__vector__init__
vector_DTreeNode.create = _c.__vector_create
vector_DTreeNode.__repr__ = _c.__vector__repr__
vector_DTreeNode.tolist = _c.__vector_tolist
vector_DTreeNode.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_DTreeNode()
_z.resize(1)
vector_DTreeNode.elem_type = _z[0].__class__
del(_z)
        
vector_DTree.__old_init__ = vector_DTree.__init__
vector_DTree.__init__ = _c.__vector__init__
vector_DTree.create = _c.__vector_create
vector_DTree.__repr__ = _c.__vector__repr__
vector_DTree.tolist = _c.__vector_tolist
vector_DTree.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_DTree()
_z.resize(1)
vector_DTree.elem_type = _z[0].__class__
del(_z)
        
vector_Stage.__old_init__ = vector_Stage.__init__
vector_Stage.__init__ = _c.__vector__init__
vector_Stage.create = _c.__vector_create
vector_Stage.__repr__ = _c.__vector__repr__
vector_Stage.tolist = _c.__vector_tolist
vector_Stage.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Stage()
_z.resize(1)
vector_Stage.elem_type = _z[0].__class__
del(_z)
        
vector_KeyPoint.__old_init__ = vector_KeyPoint.__init__
vector_KeyPoint.__init__ = _c.__vector__init__
vector_KeyPoint.create = _c.__vector_create
vector_KeyPoint.__repr__ = _c.__vector__repr__
vector_KeyPoint.tolist = _c.__vector_tolist
vector_KeyPoint.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_KeyPoint()
_z.resize(1)
vector_KeyPoint.elem_type = _z[0].__class__
del(_z)
        