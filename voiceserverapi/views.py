from django.shortcuts import render

# Create your views here.
import socket
import pyaudio
import wave
import threading
from vidstream import AudioSender
from vidstream import AudioReceiver
from rest_framework.decorators import api_view
from rest_framework.response import Response

# server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server_socket.bind((socket.gethostname(),1234))
# server_socket.listen(5)
# print("LISTENING AT:",server_socket)
@api_view(['GET'])
def server(request):
    if request.method == 'GET':
        id=socket.gethostbyname(socket.gethostname())

        sender = AudioSender(id,1234)
        sender_thread=threading.Thread(target=sender.start_stream)

        # sender_thread.start()
        return Response(sender_thread.start())
    else:
        return Response({'message':'Error...'})
