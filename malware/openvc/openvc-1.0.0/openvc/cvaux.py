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
import cvaux_ext as _ext
from cvaux_ext import *
        
#=============================================================================
# cvaux.h
#=============================================================================



#-----------------------------------------------------------------------------
# Eigen Objects
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# 1D/2D HMM
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# A few functions from old stereo gesture recognition demosions
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# Additional operations on Subdivisions
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# More operations on sequences
#-----------------------------------------------------------------------------


CV_DOMINANT_IPAN = 1


CV_UNDEF_SC_PARAM = 12345

CV_IDP_BIRCHFIELD_PARAM1  = 25    
CV_IDP_BIRCHFIELD_PARAM2  = 5
CV_IDP_BIRCHFIELD_PARAM3  = 12
CV_IDP_BIRCHFIELD_PARAM4  = 15
CV_IDP_BIRCHFIELD_PARAM5  = 25

CV_DISPARITY_BIRCHFIELD  = 0    



#-----------------------------------------------------------------------------
# Contour Morphing
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# Texture Descriptors
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# Face eyes&mouth tracking
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# 3D Tracker
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# Skeletons and Linear-Contour Models
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# Background/foreground segmentation
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# Calibration engine
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# Object Tracking
#-----------------------------------------------------------------------------



CvConDensation._ownershiplevel = 0

def _CvConDensation__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleaseConDensation(self)
CvConDensation.__del__ = _CvConDensation__del__

#=============================================================================
# cvaux.hpp
#=============================================================================



vector_CvFuzzyCurve.__old_init__ = vector_CvFuzzyCurve.__init__
vector_CvFuzzyCurve.__init__ = _c.__vector__init__
vector_CvFuzzyCurve.create = _c.__vector_create
vector_CvFuzzyCurve.__repr__ = _c.__vector__repr__
vector_CvFuzzyCurve.tolist = _c.__vector_tolist
vector_CvFuzzyCurve.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_CvFuzzyCurve()
_z.resize(1)
vector_CvFuzzyCurve.elem_type = _z[0].__class__
del(_z)
        
vector_CvFuzzyRule_Ptr.__old_init__ = vector_CvFuzzyRule_Ptr.__init__
vector_CvFuzzyRule_Ptr.__init__ = _c.__vector__init__
vector_CvFuzzyRule_Ptr.create = _c.__vector_create
vector_CvFuzzyRule_Ptr.__repr__ = _c.__vector__repr__
vector_CvFuzzyRule_Ptr.tolist = _c.__vector_tolist
vector_CvFuzzyRule_Ptr.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_CvFuzzyRule_Ptr()
_z.resize(1)
vector_CvFuzzyRule_Ptr.elem_type = _z[0].__class__
del(_z)
        
vector_Octree_Node.__old_init__ = vector_Octree_Node.__init__
vector_Octree_Node.__init__ = _c.__vector__init__
vector_Octree_Node.create = _c.__vector_create
vector_Octree_Node.__repr__ = _c.__vector__repr__
vector_Octree_Node.tolist = _c.__vector_tolist
vector_Octree_Node.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_Octree_Node()
_z.resize(1)
vector_Octree_Node.elem_type = _z[0].__class__
del(_z)
        
YAPE = LDetector

vector_FernClassifier_Feature.__old_init__ = vector_FernClassifier_Feature.__init__
vector_FernClassifier_Feature.__init__ = _c.__vector__init__
vector_FernClassifier_Feature.create = _c.__vector_create
vector_FernClassifier_Feature.__repr__ = _c.__vector__repr__
vector_FernClassifier_Feature.tolist = _c.__vector_tolist
vector_FernClassifier_Feature.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_FernClassifier_Feature()
_z.resize(1)
vector_FernClassifier_Feature.elem_type = _z[0].__class__
del(_z)
        
#=============================================================================
# cvvidsurf.hpp
#=============================================================================

CV_BLOB_MINW = 5
CV_BLOB_MINH = 5



CvFGDetector._ownershiplevel = 0

def _CvFGDetector__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleaseFGDetector(self)
CvFGDetector.__del__ = _CvFGDetector__del__

CvBlobDetector._ownershiplevel = 0

def _CvBlobDetector__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleaseBlobDetector(self)
CvBlobDetector.__del__ = _CvBlobDetector__del__

CvBlobTrackGen._ownershiplevel = 0

def _CvBlobTrackGen__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleaseBlobTrackGen(self)
CvBlobTrackGen.__del__ = _CvBlobTrackGen__del__

CvBlobTracker._ownershiplevel = 0

def _CvBlobTracker__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleaseBlobTracker(self)
CvBlobTracker.__del__ = _CvBlobTracker__del__

CvBlobTrackerOne._ownershiplevel = 0

def _CvBlobTrackerOne__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleaseBlobTrackerOne(self)
CvBlobTrackerOne.__del__ = _CvBlobTrackerOne__del__

PROFILE_EPANECHNIKOV = 0
PROFILE_DOG = 1


CvBlobTrackPostProc._ownershiplevel = 0

def _CvBlobTrackPostProc__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleaseBlobTrackPostProc(self)
CvBlobTrackPostProc.__del__ = _CvBlobTrackPostProc__del__

CvBlobTrackAnalysis._ownershiplevel = 0

def _CvBlobTrackAnalysis__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleaseBlobTrackAnalysis(self)
CvBlobTrackAnalysis.__del__ = _CvBlobTrackAnalysis__del__

CvBlobTrackerAuto._ownershiplevel = 0

def _CvBlobTrackerAuto__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleaseBlobTrackerAuto(self)
CvBlobTrackerAuto.__del__ = _CvBlobTrackerAuto__del__
