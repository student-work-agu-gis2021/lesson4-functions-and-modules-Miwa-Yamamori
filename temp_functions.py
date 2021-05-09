def fahr_to_celsius(temp_fahrenheit):
  """
  Function for converting temperature in Fahrenheit to Celsius.

  Parameters
  ----------
  temp_fahrenheit: <numerical>
      Temperature in Fahrenheit

  Returns
  -------
  <float>
      Converted temperature in Celsius.
  """
  # Calculate converted temperature from temp_fahrenheit
  converted_temp = (temp_fahrenheit - 32) / 1.8
  # Return the result
  return converted_temp



def temp_classifier(temp_celsius):
  """
  Function for classifying temperature.

  Parameters
  ----------
  temp_celsius: <numerical>
      Temperature in Celsius.

  Returns
  -------
  <int>
      The class number.
  """
  # When the temperature is lower than -2.0, classify to 0.
  # Temp_celsius may be float type, so we use -2.0 but -2
  if(temp_celsius < -2.0):
    return 0
  # When it is equal or warmer than -2.0 and less than 2.0, classify to 1.
  elif(-2.0 <= temp_celsius and temp_celsius < 2.0):
    return 1
  # When it is equal or warmer than 2.0 and less than 15.0, classify to 2.
  elif(2.0 <= temp_celsius and temp_celsius < 15.0):
    return 2
  # Other case (It is equal or warmer than 15.0), classify to 3.
  else:
    return 3