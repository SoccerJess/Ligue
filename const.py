# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 13:31:52 2017

@author: 3415756
"""

# Helps define a constant in Python
# From Section 6.3: Defining Constants
# Python Cookbook (2 Ed) by Alex Martelli et al.
#
# Usage:
# import const
# const.magic = 23 # First binding is fine
# const.magic = 88 # Second binding raises const.ConstError

class _const:

    class ConstError(TypeError):
        pass

    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't rebind const(%s)" % name
        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()