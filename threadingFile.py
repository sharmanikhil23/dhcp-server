import threading
import time
from dataStructure import UserIPAddresses

def askThread(user_ip_manager, stop_flag):
    ip1, timestamp1 = user_ip_manager.add_ip()
    print("Offer "+ip1)
    stop_flag.set()  # Set the flag to stop the thread

def renewThread(ip, user_ip_manager, stop_flag):
    user_ip_manager.renew_ip(ip)
    stop_flag.set()  # Set the flag to stop the thread

def releaseThread(ip, user_ip_manager, stop_flag):
    user_ip_manager.delete_ip(ip)
    stop_flag.set()  # Set the flag to stop the thread

def statusThread(ip, user_ip_manager, stop_flag):
    status=user_ip_manager.check_ip_status(ip)
    if status:
        print(ip, " ASSIGNED")
    else:
        print(ip, "AVALIABLE")
    stop_flag.set()  # Set the flag to stop the thread

def threadHandler(command, user_ip_manager, ip="0.0.0.0"):
    stop_flag = threading.Event()  # Create a stop flag for the thread
    
    if command == "ASK":
        my_thread = threading.Thread(target=askThread, args=(user_ip_manager, stop_flag))
    elif command == "RENEW":
        my_thread = threading.Thread(target=renewThread, args=(ip, user_ip_manager, stop_flag))
    elif command == "RELEASE":
        my_thread = threading.Thread(target=releaseThread, args=(ip, user_ip_manager, stop_flag))
    else:
        my_thread = threading.Thread(target=statusThread, args=(ip, user_ip_manager, stop_flag))
    
    my_thread.start()
    my_thread.join()  # Wait for the thread to complete before returning
