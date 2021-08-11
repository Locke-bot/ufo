# -*- coding: utf-8 -*-

from django.urls import re_path
from . import consumers
websocket_urlpatterns = [
    re_path(r'ws/rtt/$', consumers.RealTimeText.as_asgi()),
]