import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import syncwrite.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'syncwrite.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        syncwrite.routing.websocket_urlpatterns
    ),
})
