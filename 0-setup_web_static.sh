#!/usr/bin/env bash
# set up web servers for the deployment of web_static

# Install Nginx if it is not already installed
if ! command -v nginx > /dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
<<<<<<< HEAD
</html>" >  sudo tee /data/web_static/releases/test/index.html
=======
</html>" > /data/web_static/releases/test/index.html
>>>>>>> c725f388793ea65bd93793434d1038dcf2ae591b

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership 
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
<<<<<<< HEAD
sudo sed -i '/server_name _;/a \ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
=======
nginx_config="server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /data/web_static/;
    index  index.html index.htm;
   
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
}

}"

# Nginx configuration to the default file
sudo echo "$nginx_config" > /etc/nginx/sites-available/default
>>>>>>> c725f388793ea65bd93793434d1038dcf2ae591b

# Restart Nginx
sudo systemctl restart nginx
