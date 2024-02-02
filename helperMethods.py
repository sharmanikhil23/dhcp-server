import ipaddress
import threadingFile

def validate_ip_address(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
    
 #This will process user request   
def process_user_input(user_input,user_ip_manager):
    
    # launch a new thread
    parts = user_input.split()
    
    if is_valid_command(parts[0]) and len(parts)==2:
        command, ip_address_str = parts
        if validate_ip_address(ip_address_str):
            threadingFile.threadHandler(command,user_ip_manager,ip_address_str)
        else:
            print("Invalid Command")
    elif parts[0]=="ASK" and len(parts)==1:
        threadingFile.threadHandler(parts[0],user_ip_manager)
    else:
        print("Invalid Command")

    
#This method will check if the request is within our knowledge or not
def is_valid_command(command):
    valid = ["RENEW", "RELEASE", "STATUS"]
    if command not in valid:
        return False
    return True

def is_valid_ipv4(address):
    try:
        ipaddress.IPv4Address(address)
        return True
    except ipaddress.AddressValueError:
        return False