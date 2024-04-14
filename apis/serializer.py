from rest_framework import serializers

from base.models import item

class Itemserialize(serializers.ModelSerializer):
    class Meta:
        model = item
        fields  ='__all__'


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-md4gxa-swf5icp#qh$y_)34j(x)q&0qkxsuenmw28wqez-0o6#'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []