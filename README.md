# pythonVDC
Python 3 GUI aplication for Vehicle value calculation. The application was developed in VB.NET and is in production operation and this is a practice attempt to transcribe it to Python

# Depencies
 - wxPython (https://wxpython.org/) use pip install -U wxPython
 - reportlab (https://docs.reportlab.com/) use pip install -U reportlab

# Run
python VDC.py

# Make exe file
pyinstaller VDC.py -F -w --icon="Car.ico" --add-binary "Car.ico;." --clean --log-level TRACE

# Účel:
- program slúži na výpočet technickej/všeobecnej hodnoty vozidla a skutočnej škody pri škodách na motorových vozidlách. Aplikácia bola vyvynutá v VB.NET a je v produkčnšj prevádzke a toto je cvičný pokus o jej prepis do Pythonu

# Určenie:
- VDC je určený pre likvidátorov a technikov poisťovní/znalcov

# Popis:
- program podľa zadaných parametrov o vozidle, škode a poškodenom počíta technickú hodnotu a následne všeobecnú hodnotu vozidla podľa znaleckého štandartu v zmysle vyhlášky č. 492/2004 Z. z.
 
![](https://github.com/stibla/pythonVDC/blob/master/Screenshot.png)

# To Do
 - dokončiť výpočet
 - vytvoriť tlač
 - ukladanie/načítanie do/z súboru / databaze
