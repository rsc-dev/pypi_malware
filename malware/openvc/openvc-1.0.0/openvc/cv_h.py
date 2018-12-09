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
import cv_h_ext as _ext
from cv_h_ext import *
        
#=============================================================================
# cvtypes.h
#=============================================================================


# Defines for Distance Transform
CV_DIST_USER    = -1
CV_DIST_L1      = 1
CV_DIST_L2      = 2
CV_DIST_C       = 3
CV_DIST_L12     = 4
CV_DIST_FAIR    = 5
CV_DIST_WELSCH  = 6
CV_DIST_HUBER   = 7

# Haar-like Object Detection structures

CV_HAAR_MAGIC_VAL    = 0x42500000
CV_TYPE_NAME_HAAR    = "opencv-haar-classifier"
CV_HAAR_FEATURE_MAX  = 3

def CV_IS_HAAR_CLASSIFIER(haar_cascade):
    return isinstance(haar_cascade, CvHaarClassifierCascade) and         haar_cascade.flags&CV_MAGIC_MASK==CV_HAAR_MAGIC_VAL


vector_CvConnectedComp.__old_init__ = vector_CvConnectedComp.__init__
vector_CvConnectedComp.__init__ = _c.__vector__init__
vector_CvConnectedComp.create = _c.__vector_create
vector_CvConnectedComp.__repr__ = _c.__vector__repr__
vector_CvConnectedComp.tolist = _c.__vector_tolist
vector_CvConnectedComp.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_CvConnectedComp()
_z.resize(1)
vector_CvConnectedComp.elem_type = _z[0].__class__
del(_z)
        
Seq_CvConnectedComp.__old_init__ = Seq_CvConnectedComp.__init__
def _Seq_CvConnectedComp__init__(self, *args, **kwds):
    Seq_CvConnectedComp.__old_init__(self, *args, **kwds)
    if args:
        self.depends = [args[0]]
    elif kwds:
        self.depends = [kwds.values()[0]]
    else:
        self.depends = []
_Seq_CvConnectedComp__init__.__doc__ = Seq_CvConnectedComp.__old_init__.__doc__    
Seq_CvConnectedComp.__init__ = _Seq_CvConnectedComp__init__
        
Seq_CvConnectedComp.__iter__ = _c.__sd_iter__;
        
def endFindContours(scanner):
    z = _ext._cvEndFindContours(scanner)
    scanner._ownershiplevel = 0 # not owning the structure anymore
    return z
endFindContours.__doc__ = _ext._cvEndFindContours.__doc__

CvContourScanner._ownershiplevel = 0

def _CvContourScanner__del__(self):
    if self._ownershiplevel==1:
        _ext._cvEndFindContours(self)
CvContourScanner.__del__ = _CvContourScanner__del__

#=============================================================================
# cv.h
#=============================================================================



#-----------------------------------------------------------------------------
# Image Processing
#-----------------------------------------------------------------------------

    
CV_BLUR_NO_SCALE = 0
CV_BLUR = 1
CV_GAUSSIAN = 2
CV_MEDIAN = 3
CV_BILATERAL = 4

CV_SCHARR = -1
CV_MAX_SOBEL_KSIZE = 7

CV_BGR2BGRA =   0
CV_RGB2RGBA =   CV_BGR2BGRA

CV_BGRA2BGR =   1
CV_RGBA2RGB =   CV_BGRA2BGR

CV_BGR2RGBA =   2
CV_RGB2BGRA =   CV_BGR2RGBA

CV_RGBA2BGR =   3
CV_BGRA2RGB =   CV_RGBA2BGR

CV_BGR2RGB  =   4
CV_RGB2BGR  =   CV_BGR2RGB

CV_BGRA2RGBA =  5
CV_RGBA2BGRA =  CV_BGRA2RGBA

CV_BGR2GRAY =   6
CV_RGB2GRAY =   7
CV_GRAY2BGR =   8
CV_GRAY2RGB =   CV_GRAY2BGR
CV_GRAY2BGRA =  9
CV_GRAY2RGBA =  CV_GRAY2BGRA
CV_BGRA2GRAY =  10
CV_RGBA2GRAY =  11

CV_BGR2BGR565 = 12
CV_RGB2BGR565 = 13
CV_BGR5652BGR = 14
CV_BGR5652RGB = 15
CV_BGRA2BGR565 = 16
CV_RGBA2BGR565 = 17
CV_BGR5652BGRA = 18
CV_BGR5652RGBA = 19

CV_GRAY2BGR565 = 20
CV_BGR5652GRAY = 21

CV_BGR2BGR555  = 22
CV_RGB2BGR555  = 23
CV_BGR5552BGR  = 24
CV_BGR5552RGB  = 25
CV_BGRA2BGR555 = 26
CV_RGBA2BGR555 = 27
CV_BGR5552BGRA = 28
CV_BGR5552RGBA = 29

CV_GRAY2BGR555 = 30
CV_BGR5552GRAY = 31

CV_BGR2XYZ =    32
CV_RGB2XYZ =    33
CV_XYZ2BGR =    34
CV_XYZ2RGB =    35

CV_BGR2YCrCb =  36
CV_RGB2YCrCb =  37
CV_YCrCb2BGR =  38
CV_YCrCb2RGB =  39

CV_BGR2HSV =    40
CV_RGB2HSV =    41

CV_BGR2Lab =    44
CV_RGB2Lab =    45

CV_BayerBG2BGR = 46
CV_BayerGB2BGR = 47
CV_BayerRG2BGR = 48
CV_BayerGR2BGR = 49

CV_BayerBG2RGB = CV_BayerRG2BGR
CV_BayerGB2RGB = CV_BayerGR2BGR
CV_BayerRG2RGB = CV_BayerBG2BGR
CV_BayerGR2RGB = CV_BayerGB2BGR

CV_BGR2Luv =    50
CV_RGB2Luv =    51
CV_BGR2HLS =    52
CV_RGB2HLS =    53

CV_HSV2BGR =    54
CV_HSV2RGB =    55

CV_Lab2BGR =    56
CV_Lab2RGB =    57
CV_Luv2BGR =    58
CV_Luv2RGB =    59
CV_HLS2BGR =    60
CV_HLS2RGB =    61

CV_COLORCVT_MAX = 100

CV_WARP_FILL_OUTLIERS = 8
CV_WARP_INVERSE_MAP = 16

CV_SHAPE_RECT = 0
CV_SHAPE_CROSS = 1
CV_SHAPE_ELLIPSE = 2
CV_SHAPE_CUSTOM = 100

CV_MOP_ERODE = 0
CV_MOP_DILATE = 1
CV_MOP_OPEN = 2
CV_MOP_CLOSE = 3
CV_MOP_GRADIENT = 4
CV_MOP_TOPHAT = 5
CV_MOP_BLACKHAT = 6

CV_TM_SQDIFF        = 0
CV_TM_SQDIFF_NORMED = 1
CV_TM_CCORR         = 2
CV_TM_CCORR_NORMED  = 3
CV_TM_CCOEFF        = 4
CV_TM_CCOEFF_NORMED = 5




_str = "\n    'distance_func' is a Python function declared as follows:\n        def distance_func((int)a, (int)b, (object)userdata) -> (float)x\n    where\n        'a' : the address of a C array of C floats representing the first vector\n        'b' : the address of a C array of C floats representing the second vector\n        'userdata' : the 'userdata' parameter of cvCalcEMD2()\n        'x' : the resultant distance"
if calcEMD2.__doc__ is None:
    calcEMD2.__doc__ = _str
else:
    calcEMD2.__doc__ += _str
    
#-----------------------------------------------------------------------------
# Contours Retrieving
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# Motion Analysis
#-----------------------------------------------------------------------------


CV_LKFLOW_PYR_A_READY = 1
CV_LKFLOW_PYR_B_READY = 2
CV_LKFLOW_INITIAL_GUESSES = 4
CV_LKFLOW_GET_MIN_EIGENVALS = 8



#-----------------------------------------------------------------------------
# Planar Subdivisions
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# Contour Processing and Shape Analysis
#-----------------------------------------------------------------------------


CV_POLY_APPROX_DP = 0

CV_CONTOURS_MATCH_I1 = 1
CV_CONTOURS_MATCH_I2 = 2
CV_CONTOURS_MATCH_I3 = 3

CV_CONTOUR_TREES_MATCH_I1 = 1

CV_CLOCKWISE = 1
CV_COUNTER_CLOCKWISE = 2

CV_COMP_CORREL       = 0
CV_COMP_CHISQR       = 1
CV_COMP_INTERSECT    = 2
CV_COMP_BHATTACHARYYA= 3

CV_VALUE = 1
CV_ARRAY = 2

CV_DIST_MASK_3 = 3
CV_DIST_MASK_5 = 5
CV_DIST_MASK_PRECISE = 0

CV_CALIB_CB_FAST_CHECK = 8 # OpenCV 2.1: Equivalent C++ constant not yet available


#-----------------------------------------------------------------------------
# Feature detection
#-----------------------------------------------------------------------------



CvFeatureTree._ownershiplevel = 0

def _CvFeatureTree__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleaseFeatureTree(self)
CvFeatureTree.__del__ = _CvFeatureTree__del__

CvLSH._ownershiplevel = 0

def _CvLSH__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleaseLSH(self)
CvLSH.__del__ = _CvLSH__del__

vector_CvSURFPoint.__old_init__ = vector_CvSURFPoint.__init__
vector_CvSURFPoint.__init__ = _c.__vector__init__
vector_CvSURFPoint.create = _c.__vector_create
vector_CvSURFPoint.__repr__ = _c.__vector__repr__
vector_CvSURFPoint.tolist = _c.__vector_tolist
vector_CvSURFPoint.fromlist = classmethod(_c.__vector_fromlist)
_z = vector_CvSURFPoint()
_z.resize(1)
vector_CvSURFPoint.elem_type = _z[0].__class__
del(_z)
        
Seq_CvSURFPoint.__old_init__ = Seq_CvSURFPoint.__init__
def _Seq_CvSURFPoint__init__(self, *args, **kwds):
    Seq_CvSURFPoint.__old_init__(self, *args, **kwds)
    if args:
        self.depends = [args[0]]
    elif kwds:
        self.depends = [kwds.values()[0]]
    else:
        self.depends = []
_Seq_CvSURFPoint__init__.__doc__ = Seq_CvSURFPoint.__old_init__.__doc__    
Seq_CvSURFPoint.__init__ = _Seq_CvSURFPoint__init__
        
Seq_CvSURFPoint.__iter__ = _c.__sd_iter__;
        
#-----------------------------------------------------------------------------
# POSIT (POSe from ITeration)
#-----------------------------------------------------------------------------



CvPOSITObject._ownershiplevel = 0

def _CvPOSITObject__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleasePOSITObject(self)
CvPOSITObject.__del__ = _CvPOSITObject__del__

#-----------------------------------------------------------------------------
# Camera Calibration, Pose Estimation and Stereo
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# Kolmogorov-Zabin stereo-correspondence algorithm (a.k.a. KZ1)
#-----------------------------------------------------------------------------



CvStereoGCState._ownershiplevel = 0

def _CvStereoGCState__del__(self):
    if self._ownershiplevel==1:
        _ext._cvReleaseStereoGCState(self)
CvStereoGCState.__del__ = _CvStereoGCState__del__
