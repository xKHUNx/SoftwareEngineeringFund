# Create project
django-admin startproject <site_name>

# Create app
python manage.py startapp <app_name>

# Run server
python manage.py runserver

# Make migrations
python manage.py makemigrations [APP_NAME]

# Migrate
python manage.py migrate

# Display SQL code for table
python manage.py sqlmigrate [APP_NAME] 0001


// Database API
# Use this when in doubt
python manage.py migrate --run-syncdb

# Go to Django shell
python manage.py shell

# Import model objects
from [APP_NAME].models import [CLASS]

# Create record in Django shell
a = [CLASS]([PARAMETERES])

# View all records
[CLASS].objects.all()

# View object's column field or ID
a.[COLUMN_NAME]

# Save object to database
a.save()

# Search certain record with filter
[CLASS].objects.filter([COLUMN_NAME]=<some_value>)
Eg
- Album.objects.filter(album_title__startswith="Hi")
- Album.objects.filter(artist="Taylor Swift")

# Create object from existing row
[CLASS].objects.get([COLUMN_NAME]=<some_value>)
Eg
- album1 = Album.objects.get(pk=3)

# Display all foreign key referenced object
[CLASS].[REFERENCING_CLASS]_set.all()
Eg
- album1.song_set.all()

# Create referencing object
[CLASS].[REFERENCING_CLASS]_set.create([COLUMN_NAME]=<some_value>)
eg
- album1.song_set.create(song_title='I love bacon', file_type='.avi')

# Check how many item are associated to another object
[CLASS].[REFERENCING_CLASS]_set.count()
eg
- album1.song_set.count()
// End of database API

// Admin stuff
# Create admin user
python manage.py createsuperuser

# Register database to admin interface
In the app's admin page, add this
from .models import [CLASS]
admin.site.register([CLASS])
// End of admin stuff

// Python in HTML
# To write python code
{% %}

# To write python variable to be display
{{ }}
