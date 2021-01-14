import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import Library_management.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Library_management.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            Library_management.routing.websocket_urlpatterns
        )
    ),
})
