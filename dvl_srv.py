#!/usr/bin/env python3

from mock_a50_server import DVLMockServer
from config.services import ServiceNames, ServicePorts
from main.gen_srv import start_generic_server

if __name__ == "__main__":
    start_generic_server(ServiceNames.DVL, ServicePorts[ServiceNames.DVL], DVLMockServer)