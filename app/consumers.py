import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from.models import *
from django.contrib.auth.models import User

class chatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        await self.channel_layer.group_add(self.room_name,self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_name,self.channel_name)
        await self.close(code)

    async def receive(self, text_data):
        data=json.loads(text_data)
        message=data['message']
        username=data['username']
        roomName=data['roomname']
        await self.create_message(username,roomName,message)

        await self.channel_layer.group_send(
            self.room_name,
            {
                'type':'send_message',
                'message':message,
                'username':username,
                'roomname':roomName
            }
        )

    async def send_message(self,event):
        message=event['message']
        username=event['username']
        roomName=event['roomname']

        await self.send(text_data=json.dumps({
            'message':message,
            'username':username,
            'roomname':roomName
        }))

    @sync_to_async
    def create_message(self,username,roomName,message):
        username=User.objects.get(username=username)
        room=Rooms.objects.get(slug=roomName)
        message=Messages.objects.create(sender=username,messages=message,room=room)