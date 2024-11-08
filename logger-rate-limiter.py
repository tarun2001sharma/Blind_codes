class Logger:

    def __init__(self):
        self.total_messages = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.total_messages or timestamp >= self.total_messages[message] + 10:
            self.total_messages[message] = timestamp
            return True
        else:
            return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
