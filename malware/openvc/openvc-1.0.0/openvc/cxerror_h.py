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

CV_StsOk                   =  0  # everithing is ok                
CV_StsBackTrace            = -1  # pseudo error for back trace     
CV_StsError                = -2  # unknown /unspecified error      
CV_StsInternal             = -3  # internal error (bad state)      
CV_StsNoMem                = -4  # insufficient memory             
CV_StsBadArg               = -5  # function arg/param is bad       
CV_StsBadFunc              = -6  # unsupported function            
CV_StsNoConv               = -7  # iter. didn't converge           
CV_StsAutoTrace            = -8  # tracing                         

CV_HeaderIsNull            = -9  # image header is NULL            
CV_BadImageSize            = -10 # image size is invalid           
CV_BadOffset               = -11 # offset is invalid               
CV_BadDataPtr              = -12 #
CV_BadStep                 = -13 #
CV_BadModelOrChSeq         = -14 #
CV_BadNumChannels          = -15 #
CV_BadNumChannel1U         = -16 #
CV_BadDepth                = -17 #
CV_BadAlphaChannel         = -18 #
CV_BadOrder                = -19 #
CV_BadOrigin               = -20 #
CV_BadAlign                = -21 #
CV_BadCallBack             = -22 #
CV_BadTileSize             = -23 #
CV_BadCOI                  = -24 #
CV_BadROISize              = -25 #

CV_MaskIsTiled             = -26 #

CV_StsNullPtr                = -27 # null pointer 
CV_StsVecLengthErr           = -28 # incorrect vector length 
CV_StsFilterStructContentErr = -29 # incorr. filter structure content 
CV_StsKernelStructContentErr = -30 # incorr. transform kernel content 
CV_StsFilterOffsetErr        = -31 # incorrect filter ofset value 

#extra for CV 
CV_StsBadSize                = -201 # the input/output structure size is incorrect  
CV_StsDivByZero              = -202 # division by zero 
CV_StsInplaceNotSupported    = -203 # in-place operation is not supported 
CV_StsObjectNotFound         = -204 # request can't be completed 
CV_StsUnmatchedFormats       = -205 # formats of input/output arrays differ 
CV_StsBadFlag                = -206 # flag is wrong or not supported   
CV_StsBadPoint               = -207 # bad CvPoint  
CV_StsBadMask                = -208 # bad format of mask (neither 8uC1 nor 8sC1)
CV_StsUnmatchedSizes         = -209 # sizes of input/output structures do not match 
CV_StsUnsupportedFormat      = -210 # the data format/type is not supported by the function
CV_StsOutOfRange             = -211 # some of parameters are out of range 
CV_StsParseError             = -212 # invalid syntax/structure of the parsed file 
CV_StsNotImplemented         = -213 # the requested function/feature is not implemented 
CV_StsBadMemBlock            = -214 # an allocated block has been corrupted 
CV_StsAssert                 = -215 # assertion failed 

