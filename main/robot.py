#!/usr/bin/env python3

import sys
import time
import signal
import multiprocessing
from host_cls import ClassHoster
from ROBOT_SYSTEMS import SYSTEMS

def init_class_hoster():
    """Initialize ClassHoster and host itself."""
    class_hoster = ClassHoster()
    class_hoster.host_class(ClassHoster)

def start_hoster_process():
    """Start the ClassHoster in a separate process."""
    process = multiprocessing.Process(target=init_class_hoster)
    process.start()
    return process

def main(terminate_hoster=False):
    """Main function to coordinate processes and host classes."""
    class_hoster_process = start_hoster_process()

    def signal_handler(signum, frame):
        class_hoster_process.terminate()
        exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)

    time.sleep(0.3)

    systems = SYSTEMS
    from host_a_class import host_a_class # I know this is wack just go with it
    for system in systems:
        host_a_class(system)

    if terminate_hoster:
        class_hoster_process.terminate()

if __name__ == "__main__":
    terminate_flag = (len(sys.argv) > 1 and sys.argv[1] == 'g')
    main(terminate_hoster=terminate_flag)
