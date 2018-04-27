:title: Xandikos
:hidden: True
:url:
:save_as: index.html

Xandikos is a lightweight yet complete CardDAV/CalDAV server that backs onto a Git repository.

Xandikos (Ξανδικός or Ξανθικός) takes its name from the name of the March month
in the ancient Macedonian calendar, used in Macedon in the first millennium BC.

Features
--------

- Easy to set up
- Share calendars (events, todo items, journal entries) via CalDAV and contacts (vCard) via CardDAV
- Automatically keep history and back up changes in Git
- Supports synchronization extensions for CalDAV/CardDAV for quick and efficient syncing
- Automatically keep history and back up
- Works with `all tested CalDAV and CardDAV clients </clients.html>`_
- Licensed under the `GNU GPLv3 (or later) <https://www.gnu.org/licenses/gpl-3.0.en.html>`_

Limitations
-----------

- No multi-user support
- No support for CalDAV scheduling extensions

Dependencies
------------

At the moment, Xandikos supports Python 3.3 and higher as well as Pypy 3. It
also uses `Dulwich <https://github.com/jelmer/dulwich>`_,
`Jinja2 <http://jinja.pocoo.org/>`_,
`icalendar <https://github.com/collective/icalendar>`_, and
`defusedxml <https://github.com/tiran/defusedxml>`_.

E.g. to install those dependencies on Debian:

.. code:: shell

  sudo apt install python3-dulwich python3-defusedxml python3-icalendar python3-jinja2

Or to install them using pip:

.. code:: shell

  python setup.py develop

Running
-------

Testing
=======

To run a standalone (low-performance, no authentication) instance of Xandikos,
with a pre-created calendar and addressbook (storing data in *$HOME/dav*):

.. code:: shell

  ./bin/xandikos --defaults -d $HOME/dav

A server should now be listening on `localhost:8080 <http://localhost:8080/>`_.

Note that Xandikos does not create any collections unless --defaults is
specified. You can also either create collections from your CalDAV/CardDAV client,
or by creating git repositories under the *contacts* or *calendars* directories
it has created.

Production
==========

The easiest way to run Xandikos in production is using
`uWSGI <https://uwsgi-docs.readthedocs.io/en/latest/>`_.

One option is to setup uWSGI with a server like
`Apache <http://uwsgi-docs.readthedocs.io/en/latest/Apache.html>`_,
`Nginx <http://uwsgi-docs.readthedocs.io/en/latest/Nginx.html>`_ or another web
server that can authenticate users and forward authorized requests to
Xandikos in uWSGI. See `examples/uwsgi.ini <examples/uwsgi.ini>`_ for an
example uWSGI configuration.

Alternatively, you can run uWSGI standalone and have it authenticate and
directly serve HTTP traffic. An example configuration for this can be found in
`examples/uwsgi-standalone.ini <examples/uwsgi-standalone.ini>`_.

This will start a server on `localhost:8080 <http://localhost:8080/>`_ with username *user1* and password
*password1*.

.. code:: shell

  mkdir -p $HOME/dav
  uwsgi examples/uwsgi-standalone.ini
