import os

# Pinger is used to ping remote sites

class Pinger():
    # Function to check for internet connectivity.
    def check_internet_connectivity(self):
        #We just ping google. If it responds, we are connected to the internet.
        response = os.system('ping -c 4 google.com')
        #response will = 0 if we get at least 1 packet back
        if response == 0:
            return True
        else:
            return False
        
    def ping_site(self,location_ip):
        response = os.system(f"ping -c 4 {location_ip}")
        if response == 0:
            return True
        else:
            return False
        

pinger = Pinger()