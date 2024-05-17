#!/usr/bin/env python3

from utility.defaults import Defaults

class ServiceNames():
    DEFAULT = "DEFAULT"
    DVL = "DVL"

ServicePorts = {
    ServiceNames.DEFAULT: Defaults.PORT,
    ServiceNames.DVL: 56789,
}