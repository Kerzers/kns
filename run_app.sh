#!/bin/bash

export KNS_MYSQL_USER=KNS_dev
export KNS_MYSQL_PWD=KNS_dev_pwd
export KNS_MYSQL_HOST=localhost
export KNS_MYSQL_DB=KNS_dev_db

gunicorn --bind 0.0.0.0:5000 api.v1.app:app
