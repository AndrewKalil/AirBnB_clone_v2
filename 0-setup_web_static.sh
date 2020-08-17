#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install Nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo -e '<html>\n
     <head>\n
     </head>\n
     <body>\n
	Holberton School\n
     </body>\n
</html>' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "38i location /hbnb_static {\nalias /data/web_static/current;\n}" /etc/nginx/sites-enabled/default
sudo service nginx restart
