# Host ANY Class!

## Description
Long READMEs are scary, so I'll keep this short. There is more info in the docs/README.md.
This package is meant to take YOUR class, and make it very easy to use. Do this

    git clone https://github.com/Repo-Factory/ClassHoster
    install.sh (you're using ROBOT_LIB right? https://github.com/Package-Repository/install)
    ROBOT.py
    cd ~/ROBOT_LIB/ROBOT_API
    python3 -m http.server 7000 &
    firefox http://localhost:7000

Installing this package to ROBOT_LIB and running the main ROBOT.py script will host the example classes I've provided.

Try it out. You can edit the ROBOT_SYSTEMS.py file and place any class there. This system will host all of them, making
their functions globally available to any other process. You do not have to set anything up. You're welcome.