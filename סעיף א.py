class Analog_To_Digital_Converter:
    analog_value = 0
    def __init__(self, analog_value):
        self.analog_value = analog_value

    def Analog_To_Digital(self):
        analog_value_precent = self.analog_value/5
        portion1024 = int(1023*analog_value_precent)
        print(portion1024)
        binary_num = bin(portion1024)
        print (binary_num[2:])

analog1 = Analog_To_Digital_Converter(4.63)

analog1.Analog_To_Digital()