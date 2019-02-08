.. applicake documentation master file, created by
   sphinx-quickstart on Fri Feb  8 07:32:32 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to applicake's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Description
===========

Applicake is a framework that simplifies the wrapping of external tools by standardizing input parameters, logging messages and output streams. Each wrapper is a class that extends one of the two supported "App" types, BasicApp and WrappedApp:

- BasicApp is mostly used for python-based apps, where the python can be implemented directly in the run method.

- WrappedApp is mostly used to wrap shell commands, where the shell command is prepare in prepare_run.


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
