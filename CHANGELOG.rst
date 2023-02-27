Changelog - pytracking
======================

0.4.5 - February 27th 2023
------------------------

Added support for Django 4.2 and Python 3.11, drop support for old Pythons and Djangos.

0.4.4 - September 23rd 2022
------------------------

Added support for Django 4.1, drop support for old Pythons and Djangos.

0.4.3 - December 8th 2021
------------------------

Added support for Django 4.0

0.4.2 - October 18th 2021
------------------------

Added support for Python 3.10

0.4.1 - April 8th 2021
------------------------

Added support for Python 3.9, dropped support for Django <3.1, added support for Django 3.2.

0.4.0 - August 14th 2020
------------------------

Dropped support for Django <2.2, Python <3.5.

0.2.0 - June 6th 2017
---------------------

- Added request parameter to notify_decoding_error callback in
  ``pytracking.django.TrackingView``
- Added a reference to professional services in README.rst


0.1.0 - August 10th 2016
------------------------

- First release!
- Support encoding and decoding of open/click tracking links.
- Basic Django Views.
- Can send webhook POST requests with tracking data.
- Can encrypt tracking data instead of relying on base64.
- Can modify HTML content to replace links and add tracking pixel.
