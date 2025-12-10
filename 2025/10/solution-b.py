import numpy as np

class FactoryMachine:
    def __init__(self, indicator_targets, button_wirings, joltage_targets):
        # read the indicator targets (for a running machine)
        #  indicated by an array of (0 and 1) to indicate lights off (0) and on (1)
        #  transformed into binary format for better handling later on
        self.indicator_targets = 0
        indicator_binary = "0b"
        for indicator_target in indicator_targets[::-1]:
            if indicator_target == ".": indicator_binary += "0"
            else: indicator_binary += "1"
        self.indicator_targets = int(indicator_binary, 2)
        #print("Indicator Targets read:", indicator_binary, "=", self.indicator_targets)

        # define the size of the indicator lights field
        self.number_of_lights = len(indicator_binary) - 2

        # read the button wiring to change the indicator lights
        #  indicated by an array of (0 and 1) to indicate if a light is altered (1) or not (0) by a button
        #  transformed into binary format for better handling later on
        self.button_wirings = []
        for button_wiring in button_wirings:
            buttons = int("0b" + ("0" * self.number_of_lights), 2)
            for button in button_wiring.split(","):
                #buttons = buttons[:2] + buttons[2:]
                button_binary = "0b" + "{0:b}".format(2**int(button))
                #print("Button", button_binary)
                buttons = (buttons | int(button_binary, 2))
            self.button_wirings.append(buttons)
            #print("Button Wiring:", buttons)
        print("Button Wirings read:", self.button_wirings)

        # read the button wiring, but interprete value as decimal
        wiring_joltages = []
        for button_wiring in button_wirings:
            button_wiring_split = button_wiring.split(",")
            button_joltage = []
            for button_joltage_index in range(self.number_of_lights):
                if str(button_joltage_index) in button_wiring_split:
                    button_joltage.append(1)
                else:
                    button_joltage.append(0)
            #print("Button", button_joltage)
            wiring_joltages.append(button_joltage)
            #print("Button Wiring:", buttons)
        self.wiring_joltages = np.array(wiring_joltages)
        print("Button Joltages read:\n", self.wiring_joltages)

        # read the joltages
        joltages = []
        for joltage in joltage_targets.split(",")[::-1]:
            joltages.append(int(joltage))
        self.joltages = np.array([joltages])
        print("Joltages read:", joltages, self.joltages)

        # define the starting condition of this machine (all lights turned off)
        self.indicator_lights = int("0b0", 2)
        #print("Default State:", self.indicator_lights)

        self.presses = len(button_wirings)
        self.jolt_presses = sum(self.joltages)

    def pretty_print(self, binary_value):
        pretty_value = "0b"
        pretty_value += ("{0:0"+str(self.number_of_lights)+"b}").format(binary_value)
        return pretty_value

    def increase_jolt(self, current_joltage, jolt_presses, wiring_joltage_options):
        if jolt_presses > self.jolt_presses: return

        # check if joltage is already too high
        for jolt_index in range(len(current_joltage)):
            if current_joltage[jolt_index] >= self.joltages[jolt_index]:
                return



        for wiring_joltage in wiring_joltage_options:
            return


    def jolt(self):
        #self.increase_jolt([0 for i in self.joltages], 0, self.wiring_joltages)
        return

machines, factory_machines = [], []
with open("test-input.txt", "r") as file:
    for line in file:
        indicators, buttons, joltages = [], [], []
        for section in line.strip("\n\r").split(" "):
            if section.startswith("("):
                buttons.append(section.replace('(','').replace(')',''))
            elif section.startswith("["):
                indicators.append(section.replace('[','').replace(']',''))
            elif section.startswith("{"):
                joltages.append(section.replace('{','').replace('}',''))

        machines.append([indicators, buttons, joltages])
        print([indicators, buttons, joltages])
        factory_machines.append(FactoryMachine(indicators[0], buttons, joltages[0]))

print("Machines:", machines)

max_presses, i = 0, 1
factory_machines[0].jolt()
'''
for factory_machine in factory_machines:
    max_press = factory_machine.start()
    print("Sub-Solution (", i, "):", max_press)
    i += 1
    max_presses += max_press
'''
print("Solution:", max_presses)

