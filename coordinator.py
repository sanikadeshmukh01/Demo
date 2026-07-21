from resource_agent import allocate_resources
from communication_agent import generate_alert



def coordinator(city, risk):

    print("AI Coordinator Started")
    print("---------------------")


    print("Detected Risk:", risk)


    # Resource decision

    resources = allocate_resources(risk)


    print("\nResources:")

    print(resources)



    # Communication decision

    alert = generate_alert(
        city,
        risk,
        resources
    )


    print("\nALERT MESSAGE")

    print(alert)



city = "Chennai"

risk = "HIGH"


coordinator(city, risk)