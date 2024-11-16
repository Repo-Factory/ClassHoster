# Generated stubs for All Classes Hosted By ClassHoster

from classhoster.main.client import call_service
from classhoster.utility.types.req_resp import GenericRequest
from typing import Type, Any

# Generated stubs for class_type: ClassHoster

def host_class(class_type):
   return call_service(port=38851, 
      request=GenericRequest(function="host_class", 
      args={"class_type": class_type}))

# Generated stubs for class_type: ZixClass

def whats_my_name():
   return call_service(port=38852, 
      request=GenericRequest(function="whats_my_name", 
      args={}))

# Generated stubs for class_type: TimeClass

def get_seconds_passed():
   return call_service(port=38853, 
      request=GenericRequest(function="get_seconds_passed", 
      args={}))

# Generated stubs for class_type: BucketClass

def add_to_bucket(things):
   return call_service(port=38854, 
      request=GenericRequest(function="add_to_bucket", 
      args={"things": things}))

def sub_from_bucket(things):
   return call_service(port=38854, 
      request=GenericRequest(function="sub_from_bucket", 
      args={"things": things}))
