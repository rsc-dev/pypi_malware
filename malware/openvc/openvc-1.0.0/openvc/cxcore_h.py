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
import cxcore_h_ext as _ext
from cxcore_h_ext import *
        
#=============================================================================
# cxcore.h
#=============================================================================


#-----------------------------------------------------------------------------
# Array allocation, deallocation, initialization and access to elements
#-----------------------------------------------------------------------------



CV_MAX_ARR = 10

CV_NO_DEPTH_CHECK     = 1
CV_NO_CN_CHECK        = 2
CV_NO_SIZE_CHECK      = 4


#-----------------------------------------------------------------------------
# Arithmetic, logic and comparison operations
#-----------------------------------------------------------------------------

    

#-----------------------------------------------------------------------------
# Math operations
#-----------------------------------------------------------------------------


CV_RAND_UNI = 0
CV_RAND_NORMAL = 1

    

#-----------------------------------------------------------------------------
# Matrix operations
#-----------------------------------------------------------------------------


CV_COVAR_SCRAMBLED = 0
CV_COVAR_NORMAL = 1
CV_COVAR_USE_AVG = 2
CV_COVAR_SCALE = 4
CV_COVAR_ROWS = 8
CV_COVAR_COLS = 16

CV_PCA_DATA_AS_ROW = 0
CV_PCA_DATA_AS_COL = 1
CV_PCA_USE_AVG = 2


#-----------------------------------------------------------------------------
# Array Statistics
#-----------------------------------------------------------------------------

    
CV_REDUCE_SUM = 0
CV_REDUCE_AVG = 1
CV_REDUCE_MAX = 2
CV_REDUCE_MIN = 3


#-----------------------------------------------------------------------------
# Discrete Linear Transforms and Related Functions
#-----------------------------------------------------------------------------

    

#-----------------------------------------------------------------------------
# Dynamic Data Structure
#-----------------------------------------------------------------------------

    
CV_FRONT = 1
CV_BACK = 0



CvGraphScanner._ownershiplevel = 0

def _CvGraphScanner__del__(self):
    if self._ownershiplevel==1:
        _PE._cvReleaseGraphScanner(self)
CvGraphScanner.__del__ = _CvGraphScanner__del__

#-----------------------------------------------------------------------------
# Drawing Functions
#-----------------------------------------------------------------------------

    
CV_FILLED = -1
CV_AA = 16
    

#-----------------------------------------------------------------------------
# System Functions
#-----------------------------------------------------------------------------

    
# Sets the error mode
CV_ErrModeLeaf = 0
CV_ErrModeParent = 1
CV_ErrModeSilent = 2



#-----------------------------------------------------------------------------
# Data Persistence
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# CPU capabilities
#-----------------------------------------------------------------------------

CV_CPU_NONE    = 0    
CV_CPU_MMX     = 1
CV_CPU_SSE     = 2
CV_CPU_SSE2    = 3
CV_CPU_SSE3    = 4
CV_CPU_SSSE3   = 5
CV_CPU_SSE4_1  = 6
CV_CPU_SSE4_2  = 7
CV_CPU_AVX    = 10
CV_HARDWARE_MAX_FEATURE = 255
    


#=============================================================================
# cxflann.h
#=============================================================================


