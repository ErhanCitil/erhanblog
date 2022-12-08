Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess erhanblog-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/erhanblog/log/apache2/error.log"
        CustomLog "/srv/sites/erhanblog/log/apache2/access.log" common

        WSGIProcessGroup erhanblog-<target>

        Alias /media "/srv/sites/erhanblog/media/"
        Alias /static "/srv/sites/erhanblog/static/"

        WSGIScriptAlias / "/srv/sites/erhanblog/src/erhanblog/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-erhanblog-<target>]
    user = <user>
    command = /srv/sites/erhanblog/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/erhanblog/src/erhanblog/wsgi/wsgi_<target>.py
    home = /srv/sites/erhanblog/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/erhanblog/log/uwsgi_err.log
    stdout_logfile = /srv/sites/erhanblog/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_erhanblog_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/erhanblog/log/nginx-access.log;
      error_log /srv/sites/erhanblog/log/nginx-error.log;

      location /500.html {
        root /srv/sites/erhanblog/src/erhanblog/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/erhanblog/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/erhanblog/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_erhanblog_<target>;
      }
    }
