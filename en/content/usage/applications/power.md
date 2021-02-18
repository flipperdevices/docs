Flipper has power management system, that mainly consist of two special IC: Fuel gauge and charger.
Main goal of first IC is to moitor the charge level of battery. Its realized through precise calculations of energy, that going to battery and spent from battery.
Charger IC needed for control of charge process, that very important for battery life and user health.

![](../../assets/applications/power-state-screenshot.png)

Power state application obtains information from these ICs and shows it on display. Let's figure out, what it means.

In first line (Current) first value is current, reported by fuel gauge (consumed by battery). If Flipper is not connected to power supply (charge process not going on) that we'll get negative value here. It means Flipper own consumption current (calculated on battery circuit) at the moment. Second value is charge currnet, reported by charger IC. After the start of charging there will be a non-zero value.

Next line (Voltage) contains voltage levels on battery circuit, respectively recieved from fuel gauge and charger. Please note, that last value will be correct only during charge process.

Third line (Charge) is current charge level of battery. It calculated by fuel gauge using amount of energy, that has been consumed by battery during charge and spent from during the device usage.

Further located values of current capacity and full capacity of battery. First one can be correctly calculated only if actual battery has the same value of full capacity (second value), as used during fuel gauge calibration.

Last line contains temperature of the fuel gauge IC and temperature of the device battery respectively in Celsius degrees. Battery temperature measured by NTC-thermistor, located on the battery.

