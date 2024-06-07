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
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership 
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="server {
    listen 80 default_server;
    listen [::]:80 default_server;
   

    location /hbnb_static/ {
        root /data/web_static/current/;
        index index.html index.htm;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}"

# Nginx configuration to the default file
sudo echo "$nginx_config" > /etc/nginx/sites-available/default

# Restart Nginx
sudo systemctl restart nginx