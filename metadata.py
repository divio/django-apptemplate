package_name = 'myapp'
name = 'django-myapp'
author = 'My Name'
author_email = 'mymail@example.com'
description = "myapp description."
version = __import__(package_name).__version__
project_url = 'http://github.com/myuser/%s' % name
license = 'BSD'