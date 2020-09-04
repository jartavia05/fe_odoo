# Instructions to Install Odoo 12 in Ubuntu 18.04 with nginx and Let's Encrypt

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
sudo apt install -f
sudo systemctl status odoo
```

## Install Addons
```
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.bionic_amd64.deb
sudo dpkg -i wkhtmltox_0.12.6-1.bionic_amd64.deb
sudo apt install -f
```

## Install Nginx
```
sudo apt install nginx -y
sudo systemctl status nginx
cd /etc/nginx/sites-enabled
sudo ln -s /etc/nginx/sites-available/odoo.yourdomain.com odoo.yourdomain.com
```

## Install letscrypt
```
sudo add-apt-repository ppa:certbot/certbot
sudo apt install python-certbot-nginx
sudo certbot --nginx -d odoo.yourdomain.com
sudo systemctl restart nginx
```

### Nginx config file of /etc/nginx/sites-available/odoo.yourdomain.com
```
upstream odoo {
    server 127.0.0.1:8069;
}

server {
    listen 443 ssl; # managed by Certbot
    server_name odoo.domain.com.au;

    access_log  /var/log/nginx/odoo.access.log;
    error_log   /var/log/nginx/odoo.error.log;

    ssl on;
    ssl_certificate /etc/letsencrypt/live/odoo.yourdomain.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/odoo.yourdomain.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    keepalive_timeout   60;

    proxy_buffers 16 64k;
    proxy_buffer_size 128k;

    location / {
        proxy_pass  http://odoo;
        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
        proxy_redirect off;

        proxy_set_header    Host            $host;
        proxy_set_header    X-Real-IP       $remote_addr;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    X-Forwarded-Proto https;
    }

    location ~* /web/static/ {
        proxy_cache_valid 200 60m;
        proxy_buffering on;
        expires 864000;
        proxy_pass http://odoo;
    }



}

server {
    listen      80;
    server_name odoo.yourdomain.com;

    add_header Strict-Transport-Security max-age=2592000;
    rewrite ^/.*$ https://$host$request_uri? permanent;
}
```
### Final notes
```
Remember to replace odoo.yourdomain.com with your own domain. 
```