# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from Object import Object


class SampleAssembly(Object):

    name = "sampleassemblies"
    
    import pyre.db
    
    from ReferenceSet import ReferenceSet
    class Scatterers( ReferenceSet ):
        name = 'scatterersinsampleassembly'
        pass

    pass # end of SampleAssembly


# version
__id__ = "$Id$"

# End of file 