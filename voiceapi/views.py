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
# server_socket.bind((socket.gethostname()))
@api_view(['GET'])
def client(request):
    if request.method == 'GET':
        id=socket.gethostbyname(socket.gethostname())
        receiver = AudioReceiver(id,1234)
        receive_thread=threading.Thread(target=receiver.start_server)

        # receive_thread.start()
        return Response(receive_thread.start())
    else:
        print('Error......')