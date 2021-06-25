.. ODE_Solver_AdSS documentation master file, created by
   sphinx-quickstart on Sat Jun 26 00:07:06 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ODE_Solver_AdSS's documentation!
===========================================

This package lets to solve complex second order differntial equation numerically using Runge Kutta fourth order
method. This package is primarily built to help solving the Klein - Gordon equation (in inflationary theory) and 
analyse its results with various tests and visualisation. This package employs adaptive step sizing to improve the
capturing of necessary datapoints and reduce the runtime. This also has a possibility of increasing the runtime for
simpler ODEs but nevertheless numerical methods are only used for complex ODEs and simple ODEs already must have
analytical solution on its side.

**NOTE** : This package and the documetion is under construction

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Installation_Guide
   User_Guide

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
