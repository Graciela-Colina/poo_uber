from cars import Car
from account import Account

if __name__ == "__main__":
    
    car = Car("AJH234", Account("Andrea Araque", "ANDA876"))
    print(vars(car.driver))