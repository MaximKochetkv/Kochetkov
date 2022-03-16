import RPi.GPIO as GPIO

def set_values(LEDS, values):
    for i in range(len(LEDS)):
        GPIO.output(LEDS[i], values[i])

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def off_leds(LEDS):
    for LED in LEDS:
        GPIO.output(LED,0)

def main():
    dac = [10,9,11,5,6,13,19,26]
    dac.reverse()
    GPIO.setmode(GPIO.BCM)
    #setup leds
    for LED in dac:
        GPIO.setup(LED,GPIO.OUT)
    try:
        num = input ("Print number:")
        if(num.lower()== 'q'):
            raise Exception
        else:
            num = int(num)

        if( num < 0 or num > 255):
            raise ValueError("Try again")

        bin = decimal2binary(num)
        print("Voltage: {:.5f} V".format(3.3*num/255.0))
        print("Binary:", *bin)
        set_values(dac,bin)
        if (input("Press any key to stop:")):
            raise Exception

    except KeyboardInterrupt:
        print("Interrupted by Keyboard")
    except ValueError as err:
        print("Value incorrect:", err)
    except Exception:
        print("Interrupted by user")
    finally:
        off_leds(dac)
        GPIO.cleanup()

if __name__ == "__main__":
    main()     