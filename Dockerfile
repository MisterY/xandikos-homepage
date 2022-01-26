FROM debian:sid-slim
ADD . /code
<<<<<<< HEAD
RUN apt -y update && apt -y install rsync git pelican make python3-webassets python3-typogrify python3-pygments python3-markdown python3-pip python3-sphinx && python3 -m pip install pelican-sitemap git+https://github.com/jelmer/googleanalytics && cd /code && make -C /code publish && apt -y purge pelican python3-typogrify python3-pygments python3-markdown && apt -y autoremove
RUN apt -y install node-static
EXPOSE 8080
CMD node /usr/bin/node-static -a 0.0.0.0 /code/output
=======
RUN apt -y update && apt -y install rsync git pelican make python3-webassets python3-typogrify python3-pygments python3-markdown python3-pip python3-sphinx man2html && python3 -m pip install pelican-sitemap git+https://github.com/jelmer/googleanalytics && cd /code && make -C /code publish && apt -y purge pelican python3-typogrify python3-pygments python3-markdown man2html && apt -y autoremove
RUN rm -rf /var/www/html && mkdir -p /var/www && mv /code/output /var/www/html && apt -y install nginx iputils-ping bind9-host curl
EXPOSE 80
CMD /usr/sbin/nginx -g "daemon off; error_log /dev/stdout info;"
>>>>>>> 531efb64c9f3b4855ffd911d42795d4aab25db1a
