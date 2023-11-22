import configparser
import datetime


class config_controller():
    def __init__(self) -> None:
        #Initilizing the config parser
        self.config = configparser.RawConfigParser()
        self.config_path = './config.cfg'
        self.config.read(self.config_path)

        #Enviroment Section
        self.date = self.config.get('Enviroment','DATE')
        #Location Section
        self.location_name = self.config.get('Location','LOCATION_NAME')
        self.location_ip = self.config.get('Location','LOCATION_IP')
        #Email_Credentials Section
        self.from_address = self.config.get('Email_Credentials','FROM_ADDRESS')
        self.from_password = self.config.get('Email_Credentials','FROM_PASSWORD')
        self.to_address = self.config.get('Email_Credentials','TO_ADDRESS')
        #Email_Server Section
        self.hostname = self.config.get('Email_Server',"HOSTNAME")
        self.port = self.config.get('Email_Server',"PORT")
        #Email_Information Section
        self.subject = self.config.get('Email_Information','SUBJECT')

    def get_date(self):
        return self.date
    
    def set_date(self):
        self.date = datetime.date.today().strftime('%m/%d/%y')
        self.config.read(self.config_path)
        self.config.set('Enviroment','DATE',self.date)
        with open(self.config_path, "w+") as configfile:
            self.config.write(configfile)

    def get_location_name(self):
        return self.location_name
    
    def get_location_ip(self):
        return self.location_ip
    
    def get_from_address(self):
        return self.from_address
    
    def get_from_password(self):
        return self.from_password
    
    def get_to_address(self):
        return self.to_address
    
    def get_hostname(self):
        return self.hostname
    
    def get_port(self):
        return self.port
    
    def get_subject(self):
        return self.subject
    
configuration = config_controller()