class Analog_To_Digital_Converter:
    analog_value = 0
    max_voltage = 5
    number_of_bits = 10
    def __init__(self, analog_value, max_voltage , number_of_bits):
        self.analog_value = analog_value
        self.max_voltage = max_voltage
        self.number_of_bits = number_of_bits

    def Analog_To_Digital(self):
        analog_value_precent = self.analog_value/self.max_voltage
        portion1024 = int((2**self.number_of_bits-1)*analog_value_precent)
        print(portion1024)
        binary_num = bin(portion1024)
        print (binary_num[2:])

analog1 = Analog_To_Digital_Converter(4.63)

analog1.Analog_To_Digital()