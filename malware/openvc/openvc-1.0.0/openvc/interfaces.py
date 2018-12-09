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


#=============================================================================
# Helpers for access to images for other GUI packages
#=============================================================================

from info import *
from info import _NP

__all__ = []

#-----------------------------------------------------------------------------
# wx -- by Gary Bishop
#-----------------------------------------------------------------------------
# modified a bit by Minh-Tri Pham
try:
    import wx

    def cvIplImageAsBitmap(self):
        """Converts a CV_8UC3 Mat into a wx.Bitmap
        
        The Mat must be of type CV_8UC3, or else a TypeError is raised. 
        Since in gtk, a pixbuf's color space is RGB, it is assumed that the 
        Mat is also using this color space (i.e. you may want to call 
        cvCvtColor() to convert the color space *before* invoking this 
        function). Whether the image data is shared or copied to pixbuf 
        depends on how the function gtk.gdk.pixbuf_new_from_data()
        handles the image data passed to it, and not on PyOpenCV.
        """
        if self.type() != CV_8UC3:
            raise TypeError('The source image is not of type CV_8UC3.')
        return wx.BitmapFromBuffer(self.cols, self.rows, self.data)
        
    Mat.to_wx_bitmap = cvIplImageAsBitmap

except ImportError:
    pass

#-----------------------------------------------------------------------------
# PIL -- by Jeremy Bethmont
#-----------------------------------------------------------------------------
# modified by Minh-Tri Pham
try:
    from PIL import Image

    _cv_type_to_pil_mode_and_decoder = {
        CV_8UC1: ("L", "L"),
        CV_8UC3: ("RGB", "BGR"),
        CV_8UC4: ("RGBA", "BGRA"),
        CV_32SC1: ("I", "I"),
        CV_32FC1: ("F", "F"),
    }
    
    def _Mat_to_pil_image(self):
        """Converts a Mat into a PIL Image
        
        Right now, PyOpenCV can convert 1-channel (uint8|int32|float32) 
        Mats or uint8 (BGR|BGRA) Mats. Whether the image's data 
        array is shared or copied to PIL.Image depends on how PIL decodes
        the array (i.e. via function PIL.Image.fromstring()).
        """
        try:
            mode, decoder = _cv_type_to_pil_mode_and_decoder[self.type()]
        except KeyError:
            raise TypeError("Don't know how to convert the image. Check its depth and/or its number of channels.")
        return Image.fromstring(mode, (self.cols, self.rows), self.data, "raw", decoder, self.step, 1)
    Mat.to_pil_image = _Mat_to_pil_image
    
    _pil_image_bands_to_attrs = {
        ('L',): ("uint8", 1, 1, "raw", "L"),
        ('I',): ("int32", 4, 1, "raw", "I"),
        ('F',): ("float32", 4, 1, "raw", "F"),
        ('R', 'G', 'B'): ("uint8", 1, 3, "raw", "BGR"),
        ('R', 'G', 'B', 'A'): ("uint8", 1, 4, "raw", "BGRA"),
    }
    
    def cvCreateImageFromPilImage(pilimage):
        """Converts a PIL.Image into a Mat
        
        Right now, PyOpenCV can convert PIL.Images of band ('L'), ('I'), 
        ('F'), ('R', 'G', 'B'), or ('R', 'G', 'B', 'A'). Whether the 
        data array is copied from PIL.Image to IplImage or shared between
        the two images depends on how PIL converts the PIL.Image's data into
        a string (i.e. via function PIL.Image.tostring()).
        """
        try:
            dtype, elem_size, nchannels, decoder, mode = _pil_image_bands_to_attrs[pilimage.getbands()]
        except KeyError:
            raise TypeError("Don't know how to convert the image. Check its bands and/or its mode.")
        cols = pilimage.size[0]
        rows = pilimage.size[1]
        step = cols * nchannels * elem_size
        data = pilimage.tostring(decoder, mode, step)
        z = _NP.frombuffer(data, dtype=dtype, count=rows*cols*nchannels).reshape(rows, cols, nchannels)
        return asMat(z)
        
    Mat.from_pil_image = staticmethod(cvCreateImageFromPilImage)
        
except ImportError:
    pass

    
#-----------------------------------------------------------------------------
# GTK's pixbuf -- by Daniel Carvalho
#-----------------------------------------------------------------------------
# modified by Minh-Tri Pham
try:
    import pygtk
    pygtk.require20()
    import gtk
    
    def _mat_as_gtk_pixbuf(self):
        """Converts a CV_8UC3 Mat into a gtk.gdk.pixbuf
        
        The Mat must be of type CV_8UC3, or else a TypeError is raised. 
        Since in gtk, a pixbuf's color space is RGB, it is assumed that the 
        Mat is also using this color space (i.e. you may want to call 
        cvCvtColor() to convert the color space *before* invoking this 
        function). Whether the image data is shared or copied to pixbuf 
        depends on how the function gtk.gdk.pixbuf_new_from_data()
        handles the image data passed to it, and not on PyOpenCV.
        """
        if self.type() != CV_8UC3:
            raise TypeError('The source image is not of type CV_8UC3.')
            
        return gtk.gdk.pixbuf_new_from_data(self.data, gtk.gdk.COLORSPACE_RGB,
            False, 8, self.cols, self.rows, self.step)
            
    Mat.to_gtk_pixbuf = _mat_as_gtk_pixbuf
    
    def cvCreateMatFromGtkPixbuf(pixbuf):
        """Converts a gtk.gdk.pixbuf into a CV_8UC3 Mat
        
        The pixbuf must have 8 bits per sample and no alpha channel, or else
        a TypeError is raised. Since in gtk, a pixbuf's color space is RGB,
        the output Mat would therefore use the same color space (i.e. you
        may want to call cvCvtColor() to convert the color space *after*
        invoking this function). Whether the pixbuf's data is shared or 
        copied to the Mat depends on whether the function 
        gtk.gdk.get_pixels() returns its data array or a copy of the array, 
        and not on PyOpenCV.
        """
        if not isinstance(pixbuf, gtk.gdk.Pixbuf):
            raise TypeError("The first argument 'pixbuf' is not a gtk pixbuf.")
        if pixbuf.get_has_alpha():
            raise TypeError('Pixbuf source with an alpha channel is currently not supported.')
        if pixbuf.get_bits_per_sample() != 8:
            raise TypeError('The pixbuf source does not have exactly 8 bits per sample.')
            
        rows = pixbuf.get_height()
        cols = pixbuf.get_width()
        step = pixbuf.get_row_stride()
        z = _NP.frombuffer(pixbuf.get_pixels(), dtype='uint8', count=rows*step).reshape(rows, step, 1)
        z.shape = (rows, cols, 3)
        z.strides = (step, 3, 1)
        return asMat(z)

    Mat.from_gtk_pixbuf = staticmethod(cvCreateMatFromGtkPixbuf)
            
except ImportError:
    pass
except AssertionError:
    pass
