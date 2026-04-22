
offlinefolium
=============

Offline Leaflet.js Maps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`offlinefolium` allows folium maps to be rendered without access to Internet resources.  Javascript, CSS, and image resources are embedded rather than downloaded from the web.  Map tiles can be displayed from a map tile server on a local network, and folium maps can be rendered with no need to connect the network to the Internet.  Most plugins also function fully offline.  

offlinefolium is essentially a copy of folium with a few tweaks to allow resources to be embedded rather the downloaded on the fly.  The cost of this embedding is the use of at least an additional 1.4 Megabytes of memory for each map rendered, and/or 1.4 Megabytes of additional disk space for each map stored as an html file, using m.save("filename.html").  All credit for folium belongs to Rob Story, the creator of folium.  offlinefolium is just a minor extension of folium's capabilities for a very specific use case.

Installation
------------

.. code:: bash

    $ pip install folium-offline

Functionality should be consistent with folium.  See Folium's documentation for syntax, and examples.  
