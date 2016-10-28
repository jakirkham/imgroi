__author__ = "John Kirkham <kirkhamj@janelia.hhmi.org>"
__date__ = "$Oct 28, 2016 15:26$"


import numpy


def label_mask_stack(new_masks, dtype=None):
    """
        Takes a mask stack and replaces them by the max of an enumerated stack.
        In other words, each mask is replaced by a consecutive integer (starts
        with 1 and proceeds to the length of the given axis (0 by default)).
        Afterwards, the max is taken along the given axis.

        Args:
            new_masks(numpy.ndarray):            masks to enumerate
            dtype(type):                         type to use for the label
                                                 matrix (default is int).

        Returns:
            (numpy.ndarray):                     an enumerated stack.

        Examples:

            >>> label_mask_stack(
            ...     numpy.array([[[1, 0, 0, 0],
            ...                   [0, 0, 0, 0],
            ...                   [0, 0, 0, 0],
            ...                   [0, 0, 0, 0]],
            ...
            ...                  [[0, 0, 0, 0],
            ...                   [0, 1, 0, 0],
            ...                   [0, 0, 0, 0],
            ...                   [0, 0, 0, 0]],
            ...
            ...                  [[0, 0, 0, 0],
            ...                   [0, 0, 0, 0],
            ...                   [0, 0, 1, 0],
            ...                   [0, 0, 0, 0]],
            ...
            ...                  [[0, 0, 0, 0],
            ...                   [0, 0, 0, 0],
            ...                   [0, 0, 0, 0],
            ...                   [0, 0, 0, 1]]], dtype=bool)
            ... )
            array([[1, 0, 0, 0],
                   [0, 2, 0, 0],
                   [0, 0, 3, 0],
                   [0, 0, 0, 4]])
    """

    try:
        xrange
    except NameError:
        xrange = range

    if dtype is None:
        dtype = int
    dtype = numpy.dtype(dtype).type


    new_lbl_img = numpy.zeros(
        new_masks.shape[1:],
        dtype=dtype
    )

    for i in xrange(len(new_masks)):
        lbl = new_lbl_img.dtype.type(i + 1)
        numpy.maximum(
            new_lbl_img,
            lbl * new_masks[i],
            out=new_lbl_img
        )

    return new_lbl_img
