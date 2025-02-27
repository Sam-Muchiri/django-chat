from app.routing import wspattern
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watsapp.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(wspattern)
    
})
