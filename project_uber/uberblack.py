from cars import Car

class UberBlack(Car):
    typecaraccepted = []
    seatmaterial = []
    
    def __init__(self, license, driver, typecaraccepted, seatmaterial):
        super.__init__(license, driver)
        self.typecaraccepted = typecaraccepted
        self.seatmaterial = seatmaterial