import time
import socket
class TestCases:
    # TestCase Attributes
    #message list with two values message content and relative time to send in ms

    # Replace .description() with __str__()
    def __init__(self, timeLineInit:list):
        self.__destinationAddr = (('', 12000))
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.bind(self.__destinationAddr)

        self.__timeLine = timeLineInit
    
    # Declaring private method
    def __tearUp(self):
        pass
        
    # Declaring private method
    def __tearDown(self):
        pass

    def __runner(self):        
        for x in self.__timeLine:
            startTime = int(time.time() * 1000) # time in ms
            self.__socket.sendto(x[0], self.__destinationAddr)
            sleepTime_ms = ( x[1]/1000 - ((int(time.time() * 1000)) - startTime) / 1000)
            if sleepTime_ms < 0:
                print("Timeout!")
            else: 
                time.sleep(sleepTime_ms)

    def executeTests(self):
        self.__tearUp()
        self.__runner()
        self.__tearDown()
        return 0

timeLine = [
            ["Hallo ".encode(), 100],
            ["wie ".encode(), 200],
            ["geht ".encode(), 300],
            ["es ".encode(), 200],
            ["dir?".encode(), 100],
        ]
Obj = TestCases(timeLine)
Obj.executeTests()