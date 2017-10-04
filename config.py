import os
from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP, AUTH_OAUTH
basedir = os.path.abspath (os.path.dirname (__file__))


APP_VERSION = '0.6'

# Your App secret key
SECRET_KEY = 'd64C<VkCcEf*`0<J;W`={1*F/pq$Ia~-gh[d4>#SAf9ix 3yy`FT/klHGP~7Q?7%'

# The SQLAlchemy connection string.
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://egas_user:5np@ss0c@localhost/egas_db'
#SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

#------------------------------
# GLOBALS FOR APP Builder
#------------------------------
# Uncomment to setup Your App name
APP_NAME = "EGAs"

# Uncomment to setup Setup an App icon
APP_ICON = "static/img/logo.png"

#----------------------------------------------------
# AUTHENTICATION CONFIG
#----------------------------------------------------
# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database (username/password()
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
AUTH_TYPE = AUTH_DB

# Uncomment to setup Full admin role name
#AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The default user self registration role
#AUTH_USER_REGISTRATION_ROLE = "Public"

# When using LDAP Auth, setup the ldap server
#AUTH_LDAP_SERVER = "ldap://ldapserver.new"

# Uncomment to setup OpenID providers example for OpenID authentication
#OPENID_PROVIDERS = [
#    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
#---------------------------------------------------
# Babel config for translations
#---------------------------------------------------
# Setup default language
BABEL_DEFAULT_LOCALE = 'en'
# Your application default translation path
BABEL_DEFAULT_FOLDER = 'translations'
# The allowed translation for you app
LANGUAGES = {
    'en': {'flag':'gb', 'name':'English'},
#    'pt': {'flag':'pt', 'name':'Portuguese'},
#    'pt_BR': {'flag':'br', 'name': 'Pt Brazil'},
#    'es': {'flag':'es', 'name':'Spanish'},
#    'de': {'flag':'de', 'name':'German'},
#    'zh': {'flag':'cn', 'name':'Chinese'},
#    'ru': {'flag':'ru', 'name':'Russian'},
#    'pl': {'flag':'pl', 'name':'Polish'}
}
#---------------------------------------------------
# Image and file configuration
#---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + '/app/static/uploads/'

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + '/app/static/uploads/'

# The image upload url, when using models with images
IMG_UPLOAD_URL = '/static/uploads/'
# Setup image size default is (300, 200, True)
#IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir structure to override
#APP_THEME = "bootstrap-theme.css"  # default bootstrap
#APP_THEME = "cerulean.css" # dark blue header
#APP_THEME = "amelia.css"  # striking aqua & yellow
#APP_THEME = "cosmo.css"   # light blue
#APP_THEME = "cyborg.css"  # dark/inverse
#APP_THEME = "flatly.css"   # green header
#APP_THEME = "journal.css" # red header, soft fonts
APP_THEME = "readable.css" # all white, crisp
#APP_THEME = "simplex.css" # bright red header, soft fonts
#APP_THEME = "slate.css" # grey header inverse
#APP_THEME = "spacelab.css" # classic dark blue header
#APP_THEME = "united.css" # magenta header
#APP_THEME = "yeti.css"  # blue header
