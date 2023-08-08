def getAssets(transportation, shelter):
    assets = []
    match transportation:
        case "Car Owner":
            assets.append("Car")
        case "Bicycle":
            assets.append("Bicycle")
        case "Bus":
            assets.append("Bus Pass")
        case "Train": 
            assets.append("Train Pass")
        case _:
            pass
    
    match shelter:
        case "Owns House":
            assets.append("House")
        case "Owns Apartment":
            assets.append("Apartment")
        case _:
            pass
         
    return assets