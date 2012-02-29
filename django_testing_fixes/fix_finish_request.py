#!/usr/bin/python
#
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:

import socket

try:
    from liveserver.test.testcases import StoppableWSGIServer

    def finish_request(self, request, client_address, f=StoppableWSGIServer.finish_request):
        try:
            f(self, request, client_address)
        except socket.error:
            self.close_request(request)
    StoppableWSGIServer.finish_request = finish_request

except ImportError:
    pass
