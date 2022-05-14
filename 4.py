class Monitor:
    dispRes = 8
    scrSize = 0
    rate = 0
    def __init__(self, px,dn,Hz):
        print("Create Monitor")
        self.dispRes = px
        self.scrSize = dn
        self.rate = Hz
    def printInfo(self,name):
        print(f"{name:^18}")
        print("DisplayRes:", lg.dispRes)
        print("ScreenSize:", lg.scrSize)
        print("Image refresh rate:", lg.rate)
lg = Monitor(1500,580,1880)
philips = Monitor(580,345,6789)
lg.printInfo("LG")
philips.printInfo("PHILIPS")
