#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                     California Institute of Technology
#                       (C) 2007  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from Actor import Actor, action_link, action, actionRequireAuthentication


class ScatteringKernel(Actor):

    class Inventory(Actor.Inventory):

        import time
        import pyre.inventory

        id = pyre.inventory.str("id", default=None)
        id.meta['tip'] = "the unique identifier for a given search"
        
        page = pyre.inventory.str('page', default='empty')

    def default(self, director):
        return self.listall( director )

    def listall(self, director):
        page = director.retrievePage('scatteringKernel')
        
        main = page._body._content._main
        
        # populate the main column
        document = main.document(title='List of scattering kernels')
        document.description = ''
        document.byline = 'byline?'

        # retrieve id:record dictionary from db
        clerk = director.clerk
        scatteringKernels = clerk.getScatteringKernels()
            
        p = document.paragraph()
        numScatteringKernels = len(scatteringKernels)
        columns = ['description', 'texture','creator','date created','id']
        numColumns=len(columns)#scatteringKernels[0].getNumColumns()

        from PyHtmlTable import PyHtmlTable
        t=PyHtmlTable(numScatteringKernels,numColumns, {'width':'400','border':2,'bgcolor':'white'})
        for colNum, col in enumerate(columns):
            t.setc(0,colNum,col)
            
        for row, job in enumerate(scatteringKernels):
            for colNum, colName in enumerate( columns ):           
                value = job.getColumnValue(colName)
                if colName == 'description':
                    link = action_link(
                        actionRequireAuthentication(
                        'scatteringKernel',
                        director.sentry,
                        label = value,
                        routine = 'show',
                        id = job.id,
                        ),  director.cgihome
                        )
                    value = link
                t.setc(row+1,colNum,value)
        p.text = [t.return_html()]
        
        p = document.paragraph()
        p.text = [action_link(
        actionRequireAuthentication(
        'scatteringKernelInput', director.sentry,
        label = 'Add a new scattering kernel'),  director.cgihome
        ),
        '<br>']
        return page          

# this method should be altered so it loads all the values into the form fields
# and basically gives the user complete editing power
    def show(self, director):
        page = director.retrieveSecurePage( 'scatteringKernel' )
        
        id = self.inventory.id
        record = director.clerk.getJob( id )

        main = page._body._content._main
        document = main.document( title = '%s' % (record.description,) )

        props = record.getColumnNames()
        lines = ['%s=%s' % (prop, getattr(record, prop) ) for prop in props]
        for line in lines:
            p = document.paragraph()
            p.text = [line]
            continue
        return page


    def __init__(self, name=None):
        if name is None:
            name = "scatteringKernel"
        super(ScatteringKernel, self).__init__(name)
        return








# version
__id__ = "$Id$"

# End of file 
