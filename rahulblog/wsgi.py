"""
WSGI config for rahulblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

from whitenoise import WhiteNoise
application = WhiteNoise(application)
