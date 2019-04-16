from uber_rides.session import Session
from uber_rides.client import UberRidesClient

session = Session(server_token = "pHSH-0aqsOGrkE5AlSVb_qXxM02PhaIiJgDiduT6")
client = UberRidesClient(session)

response = client.get_price_estimates(
	start_latitude = 40.499310,
	start_longitude =  -3.653272,
	end_latitude = 40.466057,
	end_longitude = -3.688798,
	seat_count = 2
)

estimate = response.json.get('prices')

print(estimate)