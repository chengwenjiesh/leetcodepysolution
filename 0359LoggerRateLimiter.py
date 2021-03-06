class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msgTS = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.msgTS or self.msgTS[message] + 10 <= timestamp:
            self.msgTS[message] = timestamp
            return True

        return False



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
