*************************
python-cairo-dependencies
*************************

This package contains all of the files required to run the `python-cairo`_ module
compiled for Windows as provided by the GNOME Desktop Project's Windows binary
archive.

How to
======

 1. Install `python-cairo`_ from the binary package provided by the GNOME Project.
 2. Resolve the ``python-cairo`` dependencies by installing `python-cairo-dependencies`_
    (this module)

Binaries
========

This package provides:

 - libcairo-2.dll
 - freetype6.dll
 - libfontconfig-1.dll
 - libpng14-14.dll
 - zlib1.dll

License
=======

 - libfontconfig is licensed under the terms of the `GNU Lesser General Public
   License`_, version 2.
 - Freetype is dual licensed under the terms of the `FreeType license`_ and the
   terms of the `GNU General Public License`_, version 2.
 - cairo, which is dual licensed under the terms of the `GNU Lesser General
   Public License`_, version 2, and the `Mozilla Public License`_.
 - fontconfig, which is licensed under the terms of the `fontconfig license`_.
 - libpng, which is licensed under the terms of the `libpng license`_.
 - zlib, which is licensed under the terms of the `zlib license`_.

This individual package, its documentation, and the code required to build the
package, is licensed under the terms of the MIT License. See `LICENSE.RST`_.

Sources
=======

Binaries
--------

Binary packages were located at the following sources:

 - `GTK+ "development" bundle`_:
     - freetype6
     - libfontconfig-1
     - libpng14-14
     - zlib1
 - `libcairo-2.dll`_
 - `python-cairo-dependencies`_

Individual binaries from the GTK+ bundle can be found on the `GNOME Desktop
Project's Windows binaries page`_.

Sources
-------

Source packages for each of these can be found at the following locations:

 - `cairo`_
 - `freetype6`_
 - `libfontconfig-1`_
 - `libpng14-14`_
 - `zlib1`_
 - `python-cairo`_
 - `python-cairo-dependencies (source)`_ (this project)

.. Links
.. =====
.. 
.. Licenses
.. --------
.. 
.. _`FreeType license`: doc/LICENSE-FTL.TXT
.. _`GNU General Public License`: doc/LICENSE-GPL.TXT
.. _`GNU Lesser General Public License`: doc/LICENSE-LGPL.TXT
.. _`Mozilla Public License`: doc/LICENSE-CAIRO.TXT
.. _`fontconfig license`: doc/LICENSE-FONTCONFIG.TXT
.. _`libpng license`: doc/LICENSE-LIBPNG.TXT
.. _`zlib license`: doc/LICENSE-ZLIB.TXT
.. _`MIT License`: doc/LICENSE-LXML2.TXT
.. _`LICENSE.rst`: LICENSE.rst
.. 
.. Binaries
.. --------
.. 
.. _`GTK+ "development" bundle`: http://www.gtk.org/download-windows.html
.. _`libcairo-2.dll`: http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/cairo_1.10.2-1_win32.zip
.. _`python-cairo`: http://ftp.gnome.org/pub/GNOME/binaries/win32/pycairo/
.. _`python-cairo-dependencies`: http://www.wxwhatever.com/jmcb/cairo/cairo-dependencies-0.1.win32.exe
.. _`GNOME Desktop Project's Windows binaries page`: http://ftp.gnome.org/pub/GNOME/binaries/win32/
.. 
.. Sources
.. -------
.. 
.. _`cairo`: http://cairographics.org/download/
.. _`freetype6`: http://www.freetype.org/download.htm
.. _`libfontconfig-1`: http://www.freedesktop.org/software/fontconfig/release/
.. _`libpng14-14`: http://www.libpng.org/pub/png/libpng.html
.. _`zlib1`: http://zlib.net/
.. _`python-cairo (source)`: http://ftp.gnome.org/pub/GNOME/sources/gnome-python-desktop/
.. _`python-cairo-dependencies (source)`: http://www.github.com/jmcb/python-cairo-depedencies/
