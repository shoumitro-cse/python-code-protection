"""
WSGI config for als_social project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
from pytransform import pyarmor_runtime
pyarmor_runtime()

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'als_social.settings')
application = get_wsgi_application()


#import os
#from django.core.wsgi import get_wsgi_application
#import socketio


#async_mode = 'eventlet'
#basedir = os.path.dirname(os.path.realpath(__file__))
##mgr = socketio.RedisManager('redis://127.0.0.1:6379')
#sio_server = socketio.Server(
#    logger=True,
#    async_mode=async_mode,
#    #client_manager=mgr,
#    cors_allowed_origins='*',
#    async_handlers=True,
#    pingTimeout=900
#)

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'als_social.settings')
#django_app = get_wsgi_application()
#application = socketio.WSGIApp(
#    socketio_app=sio_server,
#    wsgi_app=django_app,
#    static_files={'/static/': 'static/', }
#)

