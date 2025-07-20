"""
This module initializes the denoising package for CT image enhancement.

Functions:
    enhance_image(input_path, output_path): Enhances a DICOM image by applying
                                            wavelet transform and median filtering.
"""

from .enhancer import enhance_image

__all__ = ['enhance_image']
