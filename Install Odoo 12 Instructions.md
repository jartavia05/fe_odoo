# Install Odoo 12 in Ubuntu 18.04 with nginx and Let's Encrypt

## Update OS
```
sudo apt update && sudo apt upgrade
sudo apt autoremove
```

## Install Postgress
```
sudo apt install postgresql -y
```

## Install Odoo
```
wget https://nightly.odoo.com/12.0/nightly/deb/odoo_12.0.latest_all.deb
sudo dpkg -i odoo_12.0.latest_all.deb
sudo apt install -f -y
sudo systemctl status odoo
```

## Install Addons
```
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb
sudo dpkg -i wkhtmltox_0.12.6-1.bionic_amd64.deb
sudo apt install -f -y
```

## Install Nginx
```
sudo apt install nginx -y
sudo systemctl status nginx
cd /etc/nginx/sites-enabled
sudo ln -s /etc/nginx/sites-available/odoo.yourdomain.com odoo.yourdomain.com
```

## Configuration of Nginx
```

sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-available/default
sudo ln -s /etc/nginx/sites-available/odoo.conf /etc/nginx/sites-enabled/odoo.conf
sudo vim /etc/nginx/sites-available/odoo.conf

#odoo server
upstream odoo {
 server 127.0.0.1:8069;
}
upstream odoochat {
 server 127.0.0.1:8072;
}

# http -> https
server {
   listen 80;
   server_name odoo.yourdomain.com;
   add_header Strict-Transport-Security max-age=2592000;
   rewrite ^(.*) https://$host$1 permanent;
}

server {
 listen 443 ssl; # managed by Certbot
 server_name odoo.yourdomain.com;
 proxy_read_timeout 720s;
 proxy_connect_timeout 720s;
 proxy_send_timeout 720s;

 # Add Headers for odoo proxy mode
 proxy_set_header X-Forwarded-Host $host;
 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 proxy_set_header X-Forwarded-Proto $scheme;
 proxy_set_header X-Real-IP $remote_addr;

 # SSL parameters
 ssl on;
 ssl_certificate /etc/letsencrypt/live/odoo.yourdomain.com/fullchain.pem; # managed by Certbot
 ssl_certificate_key /etc/letsencrypt/live/odoo.yourdomain.com/privkey.pem; # managed by Certbot
 include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
 ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
 keepalive_timeout   60;

 # log
 access_log /var/log/nginx/odoo.access.log;
 error_log /var/log/nginx/odoo.error.log;

 # Redirect longpoll requests to odoo longpolling port
 location /longpolling {
 proxy_pass http://odoochat;
 }

 # Redirect requests to odoo backend server
 location / {
   proxy_redirect off;
   proxy_pass http://odoo;
 }

 # common gzip
 gzip_types text/css text/scss text/plain text/xml application/xml application/json application/javascript;
 gzip on;
}
```

## Install letscrypt
```
sudo add-apt-repository ppa:certbot/certbot
sudo apt install python3-certbot-nginx -y
sudo certbot --nginx -d odoo.yourdomain.com
sudo systemctl restart nginx
```



### Final notes
```
Remember to replace [odoo.yourdomain.com] with your own domain. 
```
