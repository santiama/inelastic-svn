About
-----

Flot is a Javascript plotting library for jQuery. Read more at the
website:

  http://code.google.com/p/flot/

Take a look at the examples linked from above, they should give a good
impression of what Flot can do and the source code of the examples is
probably the fastest way to learn how to use Flot.
  

Installation
------------

Just include the Javascript file after you've included jQuery.

Note that you need to get a version of Excanvas (I currently suggest
you take the one bundled with Flot as it contains a bugfix for drawing
filled shapes) which is canvas emulation on Internet Explorer. You can
include the excanvas script like this:

  <!--[if IE]><script language="javascript" type="text/javascript" src="excanvas.js"></script><![endif]-->

If it's not working on your development IE 6.0, check that it has
support for VML which excanvas is relying on. It appears that some
stripped down versions used for test environments on virtual machines
lack the VML support.
  
Also note that you need at least jQuery 1.2.1.


Basic usage
-----------

Create a placeholder div to put the graph in:

   <div id="placeholder"></div>

You need to set the width and height of this div, otherwise the plot
library doesn't know how to scale the graph. You can do it inline like
this:

   <div id="placeholder" style="width:600px;height:300px"></div>

You can also do it with an external stylesheet.

Then on document ready, run the plot function:

  $.plot($("#placeholder"), data, options);

Here, data is an array of data series and options is an object with
settings if you want to customize the plot. Take a look at the
examples for some ideas of what to put in or look at the reference
in the file "API.txt".

The plot function immediately draws the chart and then returns a Plot
object with a couple of methods.


What's with the name?
---------------------

First: it's pronounced with a short o, like "plot". Not like "flawed".

So "Flot" is like "Plot".

And if you look up "flot" in a Danish-to-English dictionary, some up
the words that come up are "good-looking", "attractive", "stylish",
"smart", "impressive", "extravagant". One of the main goals with Flot
is pretty looks. Flot is supposed to be "flot".
