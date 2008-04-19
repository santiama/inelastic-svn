#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                     California Institute of Technology
#                       (C) 2007  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from Actor import actionRequireAuthentication, action_link, AuthenticationError
from FormActor import FormActor as base


class NeutronExperiment(base):


    class Inventory(base.Inventory):

        import pyre.inventory

        id = pyre.inventory.str("id", default=None)
        id.meta['tip'] = "the unique identifier of the experiment"

        ncount = pyre.inventory.float( 'ncount', default = 1e6 )
        ncount.meta['tip'] = 'number of neutrons'

        pass # end of Inventory


    def default(self, director):
        return self.listall( director )


    def listall(self, director):
        try:
            page = director.retrieveSecurePage( 'neutronexperiment' )
        except AuthenticationError, err:
            return err.page
        
        main = page._body._content._main

        # populate the main column
        document = main.document(title='List of experiments')
        document.description = ''
        document.byline = 'byline?'

        # retrieve id:record dictionary from db
        clerk = director.clerk
        experiments = clerk.indexNeutronExperiments()
        
        listexperiments( experiments.values(), document, director )
        
        return page


    def edit(self, director):
        try:
            page, document = self._head( director )
        except AuthenticationError, error:
            return error.page

        formcomponent = self.retrieveFormToShow( 'run_neutron_experiment' )
        formcomponent.inventory.id = self.inventory.id
        formcomponent.director = director
        
        # create form
        form = document.form(
            name='neutronexperiment',
            legend= formcomponent.legend(),
            action=director.cgihome)

        # specify action
        action = actionRequireAuthentication(
            actor = 'job', sentry = director.sentry,
            label = '', routine = 'edit',
            arguments = {'form-received': formcomponent.name } )
        from vnf.weaver import action_formfields
        action_formfields( action, form )

        # expand the form with fields of the data object that is being edited
        formcomponent.expand( form )

        # run button
        submit = form.control(name="submit", type="submit", value="Run")
            
        return page    


    def __init__(self, name=None):
        if name is None:
            name = "neutronexperiment"
        super(NeutronExperiment, self).__init__(name)
        return


    def _head(self, director):
        page = director.retrieveSecurePage( 'neutronexperiment' )
        
        main = page._body._content._main

        # the record we are working on
        id = self.inventory.id
        self.experiment_record = experiment = \
                                 director.clerk.getNeutronExperiment( id )

        # populate the main column
        document = main.document(title='Neutron Experiment: %s' % experiment.short_description )
        document.description = ( '')
        document.byline = '<a href="http://danse.us">DANSE</a>'

        return page, document


    def _configure(self):
        base._configure(self)
        self.id = self.inventory.id
        return


    pass # end of NeutronExperiment



from wording import plural, present_be

def listexperiments( experiments, document, director ):
    p = document.paragraph()

    n = len(experiments)

    p.text = [ 'There %s %s experiment%s: ' %
               (present_be(n), n, plural(n))
                ]

    from inventorylist import list
    list( experiments, document, 'neutronexperiment', director )
    return


def instrument_selector( document, instruments ):
    label = "Instrument selector: "
    entries = [ (instrument.id, instrument.short_description)
                for instrument in instruments]
    name = 'instrument'
    from opal.content import selector
    widget = selector( name=name, entries=entries, label=label )
    document.contents.append( widget )
    return



# version
__id__ = "$Id$"

# End of file 