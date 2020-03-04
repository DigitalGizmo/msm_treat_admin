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
