from django.urls import path
from.consumers import chatConsumer  
wspattern=[
    path('ws/chat/<str:room_name>/',chatConsumer.as_asgi())
]