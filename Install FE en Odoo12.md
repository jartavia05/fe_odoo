# Instalar modulo de Factura Electronica de https://github.com/odoocr/l10n_cr

## Introduccion
```
Autor: @jartavia05
En este documento se muestra como instalar el modulo de factura electronica de Costa Rica, utilizando Odoo 12 y con un servidor Ubuntu 18.04. Algunas configuraciones podrian variar dependiendo el Sistema Operativo.

Esto es una versión BETA, usar bajo su propio riesgo y responsabilidad.

"Open Source prevents backdoors"
```

## Clonar el modulo l10n_cr en el servidor 
```
git clone --branch '12.0' --depth 1 --single-branch https://github.com/odoocr/l10n_cr

*Ruta predeterminado de addons: /usr/lib/python3/dist-packages/odoo/addons
```
## Instalar requerimientos para FE
```
cd /your/path/l10n_cr
sudo pip3 install -r requirements.txt
```

## Mover las carpetas de FE hacia addons.
```
Ahora vamos a mover las carpetas de FE hacia addons. 

cd /your/path/l10n_cr
sudo cp -R cr_electronic_invoice /usr/lib/python3/dist-packages/odoo/addons/
sudo cp -R cr_electronic_invoice_pos /usr/lib/python3/dist-packages/odoo/addons/
sudo cp -R l10n_cr_country_codes /usr/lib/python3/dist-packages/odoo/addons/
sudo cp -R l10n_cr_hacienda_info_query /usr/lib/python3/dist-packages/odoo/addons/
sudo cp -R res_currency_cr_adapter /usr/lib/python3/dist-packages/odoo/addons/
```

## Instalar el Modulo QWEB mejorado
```
cd /usr/lib/python3/dist-packages/odoo/addons/
git clone https://github.com/jartavia05/cr_electronic_invoice_qweb_fe_boxed.git


```
