.. _readers:

Readers: getting data into ``ixdat``
====================================
Source: https://github.com/ixdat/ixdat/tree/user_ready/src/ixdat/readers

A full list of the readers thus accessible and their names can be viewed by typing:

>>> from ixdat.readers import READER_CLASSES
>>> READER_CLASSES

Reading .csv files exported by ixdat: The ``IxdatCSVReader``
------------------------------------------------------------

``ixdat`` can export measurement data in a .csv format with necessary information in the
header. See :ref:`exporters`. It can naturally read the data that it exports itself. Exporting and reading,
however, may result in loss of raw data (unlike ``save()``).

The ``ixdat_csv`` module
........................

.. automodule:: ixdat.readers.ixdat_csv
    :members:

Importing from other experimental data platforms
------------------------------------------------

**cinfdata** is a web-based database system for experimental data, developed and used at DTU SurfCat
(formerly CINF) in concert with The ``PyExpLabSys`` suite of experimental data acquisition tools.
Both are available at https://github.com/CINF.

As of yet, ``ixdat`` only has a text-file reader for data exported from **cinfdata**, but
in the future it will also have a reader which downloads from the website given e.g. a
setup and date.

The ``cinfdata`` module
.......................

.. automodule:: ixdat.readers.cinfdata
    :members:

Electrochemistry and sub-techniques
------------------------------------
These are readers which by default return an ``ECMeasurement``.
(See :ref:`electrochemistry`)

The ``biologic`` module
........................

.. automodule:: ixdat.readers.biologic
    :members:

The ``autolab`` module
......................

.. automodule:: ixdat.readers.autolab
    :members:

The ``ivium`` module
....................

.. automodule:: ixdat.readers.ivium
    :members:

Mass Spectrometry and sub-techniques
------------------------------------
These are readers which by default return an ``MSMeasurement``.
(See :ref:`mass-spec`)

The ``pfeiffer`` module
........................

.. automodule:: ixdat.readers.pfeiffer
    :members:

EC-MS and sub-techniques
------------------------
These are readers which by default return an ``ECMSMeasurement``.
(See :ref:`ec-ms`)

The ``zilien`` module
.....................

.. automodule:: ixdat.readers.zilien
    :members:

The ``ec_ms_pkl`` module
........................

.. automodule:: ixdat.readers.ec_ms_pkl
    :members:


EC-MS and sub-techniques
------------------------
These are readers which by default return a ``SpectroECMeasurement``.
(See :ref:`sec`)

The ``msrh_sec`` module
.......................

.. automodule:: ixdat.readers.msrh_sec
    :members: