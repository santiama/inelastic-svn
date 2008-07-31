########################################################################
#
# File Name:            HTMLParamElement
#
# Documentation:        http://docs.4suite.com/4DOM/HTMLParamElement.html
#

### This file is automatically generated by GenerateHtml.py.
### DO NOT EDIT!

"""
WWW: http://4suite.com/4DOM         e-mail: support@4suite.com

Copyright (c) 2000 Fourthought Inc, USA.   All Rights Reserved.
See  http://4suite.com/COPYRIGHT  for license and copyright information
"""

import string
from xml.dom import Node
from xml.dom.html.HTMLElement import HTMLElement

class HTMLParamElement(HTMLElement):

    def __init__(self, ownerDocument, nodeName="PARAM"):
        HTMLElement.__init__(self, ownerDocument, nodeName)

    ### Attribute Methods ###

    def _get_name(self):
        return self.getAttribute("NAME")

    def _set_name(self, value):
        self.setAttribute("NAME", value)

    def _get_type(self):
        return self.getAttribute("TYPE")

    def _set_type(self, value):
        self.setAttribute("TYPE", value)

    def _get_value(self):
        return self.getAttribute("VALUE")

    def _set_value(self, value):
        self.setAttribute("VALUE", value)

    def _get_valueType(self):
        return string.capitalize(self.getAttribute("VALUETYPE"))

    def _set_valueType(self, value):
        self.setAttribute("VALUETYPE", value)

    ### Attribute Access Mappings ###

    _readComputedAttrs = HTMLElement._readComputedAttrs.copy()
    _readComputedAttrs.update({
        "name" : _get_name,
        "type" : _get_type,
        "value" : _get_value,
        "valueType" : _get_valueType
        })

    _writeComputedAttrs = HTMLElement._writeComputedAttrs.copy()
    _writeComputedAttrs.update({
        "name" : _set_name,
        "type" : _set_type,
        "value" : _set_value,
        "valueType" : _set_valueType
        })

    _readOnlyAttrs = filter(lambda k,m=_writeComputedAttrs: not m.has_key(k),
                     HTMLElement._readOnlyAttrs + _readComputedAttrs.keys())
