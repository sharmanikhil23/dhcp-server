from datetime import datetime, timedelta
import heapq
import threading

from datetime import datetime
import heapq

class UserIPAddresses:
    def __init__(self):
        self.used_ips = set()
        self.ip_heap = []
        self.ip_stack = []

        # Schedule the clearing function after 1 minute
        self.schedule_clearing()

    def generate_unique_ip(self):
        for i in range(256):
            for j in range(256):
                for k in range(256):
                    for l in range(256):
                        ip_address = f"{i}.{j}.{k}.{l}"
                        if ip_address not in self.used_ips:
                            self.used_ips.add(ip_address)
                            return ip_address
        raise Exception("Out of IP addresses")

    def add_ip(self):
        if self.ip_stack:
            ip_address = self.ip_stack.pop()
        else:
            ip_address = self.generate_unique_ip()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        heapq.heappush(self.ip_heap, (timestamp, ip_address))
        return ip_address, timestamp

    def delete_ip(self, ip_address):
        if ip_address in self.used_ips:
            self.used_ips.discard(ip_address)
            self._rebuild_heap()
            print("RELEASED for", ip_address)
        else:
            print(f"IP {ip_address} is not assigned.")

    def check_ip_status(self, ip_address):
        return ip_address in self.used_ips

    def release_all_ips(self):
        for ip_address in self.used_ips.copy():
            self.delete_ip(ip_address)
            print("RELEASED for", ip_address)

    def clear_and_add_to_stack(self):
        self.release_all_ips()
        self.add_all_to_stack()
        self.schedule_clearing()

    def add_all_to_stack(self):
        for ip_address in self.used_ips.copy():
            self.ip_stack.append(ip_address)

    def renew_ip(self, ip_address):
        if ip_address in self.used_ips:
            # Renew the IP address and print a message
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            heapq.heappush(self.ip_heap, (timestamp, ip_address))
            print("RENEWED for", ip_address)

    def schedule_clearing(self):
        # Schedule the clearing function after 1 minute
        threading.Timer(60, self.clear_and_add_to_stack).start()

    def _rebuild_heap(self):
        self.ip_heap = [(timestamp, ip) for timestamp, ip in self.ip_heap if ip in self.used_ips]
        heapq.heapify(self.ip_heap)

    def get_sorted_ips(self):
        return sorted(self.ip_heap)
