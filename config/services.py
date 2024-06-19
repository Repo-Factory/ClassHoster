#!/usr/bin/env python3

from defaults import Defaults

class ServiceNames():
    DEFAULT = "DEFAULT"
    DVL = "DVL"

ServicePorts = {
    ServiceNames.DEFAULT: Defaults.PORT,
    ServiceNames.DVL: 6000,
}