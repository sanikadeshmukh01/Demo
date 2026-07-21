def allocate_resources(risk):

    if risk == "HIGH":

        resources = {

            "priority":"Emergency",

            "ambulances":10,

            "rescue_teams":5,

            "food_packets":1000,

            "water_supply":"5000 liters"

        }


    elif risk == "MEDIUM":

        resources = {

            "priority":"Alert",

            "ambulances":5,

            "rescue_teams":2,

            "food_packets":500,

            "water_supply":"2000 liters"

        }


    else:

        resources = {

            "priority":"Normal",

            "ambulances":1,

            "rescue_teams":1,

            "food_packets":100,

            "water_supply":"500 liters"

        }


    return resources