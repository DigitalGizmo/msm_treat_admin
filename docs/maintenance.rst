Treat maint
===	

Collect static
Logged in as msm_user
::

    cd /var/www/msm_user/data
    [or]
    ../..
    ./collect-treat-admin.sh

Updates
::
	touch /var/www/msm_user/data/www/msm-treat-admin.digitalgizmo.com/treat_admin/config/wsgi.py

Database
- treat_db
- access via pgAdmin

Working with Django
Need to login as root 
::
	workon treat_admin

Local dev setup

(re)make virtual env
::
	mkvirtualenv -a /Users/don/Sites/gizmo_dev/msm-treat-admin/treat_admin --python=/usr/local/bin/python3 treat_admin


Django install
::
  Django==2.2.23
	django-cors-headers==3.2.0
	djangorestframework==3.9.4
	psycopg2-binary==2.8.4
	Unipath==1.1
	pytz==2019.3

Upgrade July 2021
::
  Django==3.2.4

