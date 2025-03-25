# For handling all the interactive Brokers API interactions 
#from ibapi.client import EClient
#from ibapi.wrapper import EWrapper

class IBConnection(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        return 