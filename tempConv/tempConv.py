# a function which takes celcius as an input and returns fahrenheit temperature
def celciusToFahrenheit(celcius):
  return ((celcius * 9/5) + 32)

#a function which takes fahrenheit as an input and returns celcius temperature
def fahrenheitToCelcius(fahrenheit):
    return((fahrenheit - 32) * 5/9)

#function which takes kelvin as an input and returns celcius temperature
def kelvinToCelcius(kelvin):
  return (kelvin - 273.15)

#function which takes celcius as an input and returns kelvin temperature
def celciusToKelvin(kelvin):
  return (kelvin + 273.15)

#function which takes kelvin input to Fahrenheit temperature
def kelvinToFahrenheit(kelvin):
  #first convert kelvin to celcius, and then return that value to celcius to 
  #farenheit function, which conversts celcius to fahrenheit
  return (celciusToFahrenheit(kelvinToCelcius(kelvin)))

#function which takes Fahrenheit input to Kelvin temperature
def fahrenheitToKelvin(fahrenheit):
  #fistr convert farenheit to celcius and use that returned celcius to kelvin again 
  return(celciusToKelvin(fahrenheitToCelcius(fahrenheit)))


print(celciusToFahrenheit(10))
print(kelvinToCelcius(300))
print(kelvinToFahrenheit(40))
print(fahrenheitToKelvin(44))