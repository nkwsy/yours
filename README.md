# yours

install dependancies

`pip install -r requirements.txt`

copy .env.example to .env

`cp .env.example .env`

Add in your openai key to .env

`flask run`

tell it to make the site look however you want it

Examples queries:
- Make a nav bar which has a chatbox in it that auto resizes as one types. Include a 'send', 'reset', and 'save' button. Do this sans-serif
- Make a tribute site to Mies Van Der Rohe written in the style of a young Winston Churchill. Stlyize the webpage in a 90's cyberpunk asthetic.
- Use https://data.cityofchicago.org/resource/k7hf-8y75.json to create a dashboard of the weather from "station_name":"Oak Street Weather Station". Theme the entire website to look like a green terminal. Data retrieved looks like this `{"station_name":"Oak Street Weather Station","measurement_timestamp":"2023-03-10T08:00:00.000","air_temperature":"1.5","wet_bulb_temperature":"0.7","humidity":"87","rain_intensity":"0","interval_rain":"0","total_rain":"23.5","precipitation_type":"0","wind_direction":"56","wind_speed":"3.1","maximum_wind_speed":"3.5","barometric_pressure":"993.8","solar_radiation":"31","heading":"358","battery_life":"11.9","measurement_timestamp_label":"03/10/2023 8:00 AM","measurement_id":"OakStreetWeatherStation202303100800"}`
