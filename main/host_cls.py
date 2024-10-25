import os
import inspect
from typing import Type, Any
from gen_srv import start_generic_server
from port_allocator import generate_port
from multiprocessing import Process

output_file = os.path.join(os.getenv("HOME"), "ROBOT_LIB", "ROBOT_API.py")

class ClassHoster:

    _instance = None

    """
        Singleton since we are using class hoster to host itself
    """
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClassHoster, cls).__new__(cls)
            with open(output_file, 'w') as f:
                f.write(f"# Generated stubs for All Classes Hosted By ClassHoster\n\n")
                f.write(f"from client import call_service\n")
                f.write(f"from req_resp import GenericRequest\n")
                f.write(f"from typing import Type, Any\n\n")
            cls._instance.port = generate_port()
        return cls._instance

    def host_class(self, class_type: Type[Any]):
        name = class_type.__name__
        port = self._allocate_new_port()
        self._generate_function_stubs(class_type, port)
        process = Process(target=start_generic_server, args=[name, port, class_type])
        process.start()
        return None

    def _allocate_new_port(self):
        self.port += 1
        port = self.port
        return port

    @staticmethod
    def _generate_function_stubs(class_type: Type[Any], class_port: int):
        functions = inspect.getmembers(class_type, predicate=inspect.isfunction)
        with open(output_file, 'a') as f:
            f.write(f"# Generated stubs for class_type: {class_type.__name__}\n\n")
            for func_name, func in functions:
                if func_name.startswith('_'):
                    continue
                signature = inspect.signature(func)
                params = [param.name for param in signature.parameters.values() if param.name != 'self']
                param_str = ', '.join(str(param) for param in params)
                args_dict = ', '.join(f'"{param}": {param}' for param in params)
                f.write(f"def {func_name}({param_str}):\n")
                f.write(f"   return call_service(port={class_port}, \n"
                        f"      request=GenericRequest(function=\"{func_name}\", \n"
                        f"      args={{{args_dict}}}))\n\n")
