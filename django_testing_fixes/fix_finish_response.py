#!/usr/bin/python
#
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:

import socket

from django.core.servers import basehttp


def finish_response(self, f=basehttp.ServerHandler.finish_response):
    try:
        f(self)
    except socket.error:
        self.close()
basehttp.ServerHandler.finish_response = finish_response
