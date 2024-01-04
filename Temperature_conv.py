# converting from celcius to Fahrenheit
temperature = float(input('Temperature in Celcius ' ))

def fahrenheit_temperature(temperature):
    return(temperature*1.8 + 32 )
print('The temperature in Fahrenheit is ' + str(fahrenheit_temperature(temperature)))

# converting from Fahrenheit to celcius
temperature_in_fahrenheit = float(input('Enter the temperature in Fahrenheit ' ))

def temperature_in_celcius (temperature_in_fahrenheit):
    return(int(( temperature_in_fahrenheit -32 )*0.56))

print('Your temperature in degrees celcius is ' +str(temperature_in_celcius(temperature_in_fahrenheit)))