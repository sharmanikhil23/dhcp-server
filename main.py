import threading
import dataStructure
import helperMethods

def main():
    user_ip_manager = dataStructure.UserIPAddresses()
    stop_flag = threading.Event()
    my_thread = threading.Thread(target=releaseThread, args=(user_ip_manager, stop_flag))
    my_thread.start()

    print("\nServer is up and Running")
    try:
        while True:
            helperMethods.process_user_input(input(), user_ip_manager)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully.")
    finally:
        user_ip_manager.release_all_ips()
        stop_flag.set()
        my_thread.join()

def releaseThread(user_ip_manager, stop_flag):
    user_ip_manager.schedule_clearing()
    stop_flag.wait()

if __name__ == "__main__":
    main()
