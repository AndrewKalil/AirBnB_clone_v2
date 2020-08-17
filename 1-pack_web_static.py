#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack """
from datetime import datetime
from fabric.operations import local


def do_pack():
    '''
        Creating an archive with the files in web_static folder
    '''
    time = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(time.year,
                                                             time.month,
                                                             time.day,
                                                             time.hour,
                                                             time.minute,
                                                             time.second)
    print("Packing web_static to versions/{}".format(filename))
    local("mkdir -p versions")
    result = local("tar -vczf {} web_static".format(filename))
    if result.succeeded:
        return (filename)
    else:
        return None
