import threading
import ipaddress
import dataStructure

import helperMethods

def main():
    user_ip_manager = dataStructure.UserIPAddresses()
    stop_flag = threading.Event()
    my_thread= threading.Thread(target=releaseThread, args=(user_ip_manager, stop_flag))
    my_thread.start()
    
    print("\nServer is up and Running")
    while(True): 
        try:
            helperMethods.process_user_input(input(),user_ip_manager)
        except KeyboardInterrupt:
            user_ip_manager.release_all_ips()
            print("\nProgram interrupted. Exiting gracefully.")
            return;
        
    
    
    
def releaseThread(user_ip_manager, stop_flag):
    user_ip_manager.schedule_clearing()
    stop_flag.set()

if __name__=="__main__":
    main()