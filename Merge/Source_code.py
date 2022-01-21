from hiloSerial import *
from hiloAleatorio import *

def main():

    # Register the signal handlers
    signal.signal(signal.SIGTERM, service_shutdown)
    signal.signal(signal.SIGINT, service_shutdown)
    print('Starting main program')

    # Start the job threads
    try:

        #j1 = ThreadSerial()
        #j1.start()
        j2 = ThreadRandom()
        j2.start()
        
        # Keep the main thread running, otherwise signals are ignored.
        while True:
            time.sleep(0.01)

    except ServiceExit:

        # Terminate the running threads.
        # Set the shutdown flag on each thread to trigger a clean shutdown of each thread.
        #j1.shutdown_flag.set()
        j2.shutdown_flag.set()

        #j1.join()
        j2.join()

    print('Exiting main program')


if __name__ == '__main__':
    main()
