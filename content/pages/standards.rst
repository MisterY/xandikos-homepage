:title: Implemented standards
:save_as: standards.html

The following standards are implemented:

- :RFC:`4918`/:RFC:`2518` (Core WebDAV) - *implemented, except for COPY/MOVE/LOCK operations*
- :RFC:`4791` (CalDAV) - *fully implemented*
- :RFC:`6352` (CardDAV) - *fully implemented*
- :RFC:`5397` (Current Principal) - *fully implemented*
- :RFC:`3253` (Versioning Extensions) - *partially implemented, only the REPORT method and {DAV:}expand-property property*
- :RFC:`3744` (Access Control) - *partially implemented*
- :RFC:`5995` (POST to create members) - *fully implemented*
- :RFC:`5689` (Extended MKCOL) - *fully implemented*

The following standards are not implemented:

- :RFC:`6638` (CalDAV Scheduling Extensions) - *not implemented*
- :RFC:`7809` (CalDAV Time Zone Extensions) - *not implemented*
- :RFC:`7529` (WebDAV Quota) - *not implemented*
- :RFC:`4709` (WebDAV Mount) - `intentionally <https://github.com/jelmer/xandikos/issues/48>`_ *not implemented*
- :RFC:`5546` (iCal iTIP) - *not implemented*
- :RFC:`4324` (iCAL CAP) - *not implemented*
- :RFC:`7953` (iCal AVAILABILITY) - *not implemented*

See `DAV compliance <notes/dav-compliance.rst>`_ for more detail on specification compliancy.
