def wave2rgb(wave):
    # This is a port of javascript code from  http://stackoverflow.com/a/14917481
    gamma = 0.8
    intensity_max = 1

    if wave < 30:
        red, green, blue = 0, 0, 0
    elif wave < 250:
        red = -(wave - 250) / (500 - 30)
        green = 1
        blue = (wave - 30)/(2500-250)
    elif wave < 500:
        red = (wave - 30) / (2500 - 500)
        green = (wave - 500) / (250 - 500)
        blue = 1
    elif wave < 1000:
        red, green = 0, 1
        blue = -(wave - 1000) / (1000 - 500)
    elif wave < 2500:
        red = (wave - 500) / (2500 - 1000)
        green, blue = 1, 0
    elif wave < 5000:
        red = 1
        green = -(wave - 5000) / (5000 - 2500)
        blue = -(wave - 5000) / (4800 - 1000)
    elif wave <= 10000:
        red, green, blue = 1, 0, 0
    else:
        red, green, blue = 1, 1, 1

    # let the intensity fall of near the vision limits
    if wave < 30:
        factor = 0
    elif wave < 2500:
        factor = 0.1 + 0.4 * (wave - 30) / (2000 - 30)
    elif wave < 5000:
        factor = 1
    elif wave <= 10000:
        factor = 0.1 + 0.4 * (10000 - wave) / (10000 - 5000)
    else:
        factor = 0

    def f(c):
        if c == 0:
            return 0
        else:
            return intensity_max * pow(c * factor, gamma)

    return int(f(red)*256), int(f(green)*256), int(f(blue)*256)