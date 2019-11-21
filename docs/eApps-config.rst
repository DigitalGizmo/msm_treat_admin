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

Set up apache with wsgi
in /etc/httpd/conf/httpd.conf
For the ssl version 

<VirtualHost 68.169.50.201:443 >
	SSLCertificateFile /var/www/httpd-cert/gizmo_user/digitalgizmo.com.crt
	SSLCertificateKeyFile /var/www/httpd-cert/gizmo_user/digitalgizmo.com.key
        SSLCaCertificateFile /var/www/httpd-cert/gizmo_user/digitalgizmo.com.ca
	SSLEngine on

	ServerName msm-treat-admin.digitalgizmo.com
	CustomLog /var/www/httpd-logs/msm-treat-admin.digitalgizmo.com.access.log combined
	DocumentRoot /var/www/msm_user/data/www/msm-treat-admin.digitalgizmo.com
	ErrorLog /var/www/httpd-logs/msm-treat-admin.digitalgizmo.com.error.log
	ServerAdmin donpublic@digitalgizmo.com
	ServerAlias www.msm-treat-admin.digitalgizmo.com
	SuexecUserGroup msm_user msm_user


	# Wsgi part
	Alias /static/ /var/www/msm_user/data/www/msm-treat-admin-static/
	WSGIDaemonProcess treat_staging python-path=/var/www/msm_user/data/www/msm-treat-admin.digitalgizmo.com/treat_admin:/var/www/msm_user/data/.envs/treat_admin/lib/python3.4/site-packages
	WSGIProcessGroup treat_staging
	WSGIScriptAlias / /var/www/msm_user/data/www/msm-treat-admin.digitalgizmo.com/treat_admin/config/wsgi.py

	<Directory /var/www/msm_user/data/www/msm-treat-admin.digitalgizmo.com/treat_admin/config>
	   <Files wsgi.py>
	      Order deny,allow
	     Allow from all
	  </Files>
	</Directory>

</VirtualHost>

For the regular url -- add the redirect
<VirtualHost 68.169.50.201:80 >
	ServerName msm-treat-admin.digitalgizmo.com
	CustomLog /var/www/httpd-logs/msm-treat-admin.digitalgizmo.com.access.log combined
	DocumentRoot /var/www/msm_user/data/www/msm-treat-admin.digitalgizmo.com
	ErrorLog /var/www/httpd-logs/msm-treat-admin.digitalgizmo.com.error.log
	ServerAdmin donpublic@digitalgizmo.com
	ServerAlias www.msm-treat-admin.digitalgizmo.com
	SuexecUserGroup msm_user msm_user

	Redirect Permanent / https://msm-treat-admin.digitalgizmo.com/

</VirtualHost>


and then?

	<Directory /var/www/msm_user/data/www/msm-treat-admin.digitalgizmo.com>
        Options +Includes +ExecCGI
	</Directory>

