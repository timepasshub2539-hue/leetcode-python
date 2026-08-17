Method: GET
URL: https://api.openweathermap.org/data/2.5/weather
Query Params:
  q = Pune
  appid = {{ $env.WEATHER_KEY }}

// No headers needed here --
// GET has no body, so no Content-Type to set
