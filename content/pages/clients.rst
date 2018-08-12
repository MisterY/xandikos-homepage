:save_as: clients.html

Tested Clients
==============

Xandikos has been tested and works with the following CalDAV/CardDAV clients:

- `Vdirsyncer <https://github.com/pimutils/vdirsyncer>`_
- `caldavzap <https://www.inf-it.com/open-source/clients/caldavzap/>`_/`carddavmate <https://www.inf-it.com/open-source/clients/carddavmate/>`_
- `evolution <https://wiki.gnome.org/Apps/Evolution>`_
- `DAVdroid <https://davdroid.bitfire.at/>`_
- `sogo connector for Icedove/Thunderbird <http://v2.sogo.nu/english/downloads/frontends.html>`_
- `aCALdav syncer for Android <https://play.google.com/store/apps/details?id=de.we.acaldav&hl=en>`_
- `pycardsyncer <https://github.com/geier/pycarddav>`_
- `akonadi <https://community.kde.org/KDE_PIM/Akonadi>`_
- `CalDAV-Sync <https://dmfs.org/caldav/>`_
- `CardDAV-Sync <https://dmfs.org/carddav/>`_
- `Calendarsync <https://play.google.com/store/apps/details?id=com.icalparse>`_
- `Tasks <https://github.com/tasks/tasks/tree/caldav>`_
- `AgendaV <http://agendav.org/>`_
- `CardBook <https://gitlab.com/cardbook/cardbook/>`_
- `Tasks <https://github.com/tasks/tasks>`_

If you have tested Xandikos with another CalDAV/CardDAV client, please let us
know so we can (if necessary) fix support for it and add it to the list.

Client instructions
===================

Some clients can automatically discover the calendar and addressbook URLs from
a DAV server. For such clients you can simply provide the URL to Xandikos directly.

Clients that lack such automated discovery require the direct URL to a calendar
or addressbook. One such client is Thunderbird lightning in which case you
should provide a URL similar to the following:

::

  http://dav.example.com/user/calendars/my_calendar


