release: python manage.py makemigrations && release: python manage.py migrate
web: newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - icgbooks.wsgi:application
