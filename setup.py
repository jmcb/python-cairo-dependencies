#!/usr/bin/env python
from distutils.core import setup

def main ():
    dlls = ["bin/%s" % dll for dll in ["libcairo-2.dll", "libpng14-14.dll",
        "zlib1.dll", "freetype6.dll", "libfontconfig-1.dll"]]

    licenses = ["doc/%s" % license for license in ["LICENSE-LGPL.TXT",
        "LICENSE-CAIRO.TXT","LICENSE-FONTCONFIG.TXT", "LICENSE-LIBPNG.TXT",
        "LICENSE-ZLIB.TXT"]]

    others = ["README.rst", "LICENSE.rst"]

    long_description = """    This package contains dynamic link dependencies required to run the
    python-cairo library on Microsoft Windows. 

    Please see README.rst for more details."""

    classifiers = ["Development Status :: 6 - Mature",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: MIT License", "License :: zlib/libpng License",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries"]

    return setup(name="cairo-dependencies", version="0.1",
        maintainer="Jonathan McManus", maintainer_email="jonathan@acss.net.au", author="various",
        url="http://www.github.com/jmcb/python-cairo-dependencies",
        download_url="http://www.wxwhatever.com/jmcb/cairo", platforms="Microsoft Windows",
        description="Dynamic link library dependencies for pycairo.",
        license="GNU LGPLv2, MIT, MPL.",
        data_files=[("lib/site-packages/cairo", dlls), ("doc/python-cairo", licenses + others)],
        long_description=long_description, classifiers=classifiers)

if __name__=="__main__":
    main ()
