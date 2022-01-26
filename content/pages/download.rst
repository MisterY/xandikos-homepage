:title: Download
:save_as: download.html

Pypi
####

Xandikos can be installed from pypi using pip by running::

   $ python3 -m pip install --upgrade xandikos

Git
###

You can either clone the Xandikos repository at `GitHub <https://github.com/jelmer/xandikos/>`_ or from `my
personal server <https://www.jelmer.uk/code/xandikos>`_. E.g. by running either one of::

   $ git clone https://github.com/jelmer/xandikos
   $ git clone https://jelmer.uk/code/xandikos

Tarballs
########

.. include:: tarballs.rst

Debian/Ubuntu
#############

If you're running a recent version of Debian or Ubuntu, you can install a
nightly snapshot of Xandikos built by the `Debian Janitor
<https://janitor.debian.net/>`_. See `the instructions
<https://janitor.debian.net/fresh>`_ for details, or run::

    echo deb "[arch=amd64 signed-by=/usr/share/keyrings/debian-janitor.gpg]" \
        https://janitor.debian/net/ fresh-snapshots main | \
        sudo tee /etc/apt/sources.list.d/fresh-snapshots.list
    sudo curl -o /usr/share/keyrings/debian-janitor.gpg https://janitor.debian.net/pgp_keys
    sudo apt update
    sudo apt install -t fresh-snapshots xandikos
