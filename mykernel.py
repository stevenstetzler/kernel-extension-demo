import socket
import logging
import os
from threading import Thread

def start_listener(ipython):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind to a random port
    sock.bind(("localhost", 0))
    host, port = sock.getsockname()
    # listen as a server
    sock.listen(5)

    # inject variables into the user space
    ipython.push(
        {
            "_kernel_port" : port,
        }
    )

    def f():
        import time
        while True:
            (client, addr) = sock.accept()
            msg = client.recv(4096)

            code = msg.decode()
            print("executing:", code)
            try:
                # execute the code given
                ipython.ex(code)
            except Exception as e:
                print("error executing code:", str(e))

            client.shutdown(socket.SHUT_RDWR)
            client.close()

    # start a thread that executes the function f
    t = Thread(target=f)
    t.start()

# this function gets imported and executed when the IPython kernel is started
def load_ipython_extension(ipython):
    # The `ipython` argument is the currently active `InteractiveShell`
    # instance, which can be used in any way. This allows you to register
    # new magics or aliases, for example.
    start_listener(ipython)

def unload_ipython_extension(ipython):
    # If you want your extension to be unloadable, put that logic here.
	pass

