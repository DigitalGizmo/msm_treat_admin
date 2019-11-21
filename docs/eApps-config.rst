Treat Admin - eApps config
==========================

Config
------
My virtual env setup is under msm_user, so I need to put treat admin there

create sub domain in portal and create in ISP

Change name of placeholder site
Login as msm_user
cd to www base
::
	cd /var/www/msm_user/data/www/
	git clone https://github.com/DigitalGizmo/msm_treat_admin.git msm-treat-admin.digitalgizmo.com

Set up virtual env
Even though this is not an msm-mural project, that's where I set up the virtual env
Need to login as root 
Then
::
	mkvirtualenv -a  /var/www/msm_user/data/www/msm-treat-admin.digitalgizmo.com/treat_admin --python=/usr/local/bin/python3.4 treat_admin

pip installs
::
	pip install django==2.0.13
	pip install psycopg2-binary
	pip install Unipath
