def generate_alert(city, risk, resources):

    if risk == "HIGH":

        message = f"""
🚨 EMERGENCY ALERT 🚨

Location:
{city}

Risk Level:
HIGH

Immediate Action Required.

Deploy:
- {resources['ambulances']} Ambulances
- {resources['rescue_teams']} Rescue Teams

Supplies:
- {resources['food_packets']} Food Packets
- {resources['water_supply']}

Priority:
{resources['priority']}

"""

    elif risk == "MEDIUM":

        message = f"""
⚠️ WARNING ALERT ⚠️

Location:
{city}

Risk Level:
MEDIUM

Prepare emergency resources.

Deploy:
- {resources['ambulances']} Ambulances
- {resources['rescue_teams']} Rescue Teams

Priority:
{resources['priority']}

"""


    else:

        message = f"""
✅ NORMAL STATUS

Location:
{city}

Risk Level:
LOW

Continue monitoring.

"""


    return message