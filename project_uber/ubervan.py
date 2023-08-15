from cars import Car

class UberVan:
    typecaraccepted = []
    seatsmaterial = []

    def __init__(self, license, driver, typecaraccepted, seatsmaterial):
        super.__init__(license,driver)
        self.typecaraccepted = typecaraccepted
        self.seatsmaterial = seatsmaterial
        