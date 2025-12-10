
class FactoryMachine:
    def __init__(self, indicator_targets, button_wirings, joltages):
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
        #print("Button Wirings read:", self.button_wirings)

        # read the joltages
        self.joltages = []
        for joltage in joltages.split(","):
            self.joltages.append(int(joltage))
        #print("Joltages read:", self.joltages)

        # define the starting condition of this machine (all lights turned off)
        self.indicator_lights = int("0b0", 2)
        #print("Default State:", self.indicator_lights)

        self.presses = 200

    def pretty_print(self, binary_value):
        string_value = bin(binary_value)
        #string_value = "0b100"
        #print("string:", string_value, int(string_value, 2))
        #"0b" + "{0:b}".format(2**int(button))

        pretty_value = "0b"
        '''
        for i in range(self.number_of_lights):
            if i <= len(string_value) - 3:
                pretty_value += string_value[i+2]
            else:
                pretty_value += "0"
        '''
        #pretty_value += "0"*(self.number_of_lights-len(string_value))
        #pretty_value += string_value
        pretty_value += ("{0:0"+str(self.number_of_lights)+"b}").format(binary_value)
        return pretty_value

    # defines the machines to work with
    @staticmethod
    def press_buttons(indicator_lights, button_wiring):
        # pressing buttons on the current state
        #print(indicator_lights, "XOR", button_wiring, "=", indicator_lights ^ button_wiring)
        return indicator_lights ^ button_wiring

    def start_machine(self, indicator_lights, presses, indicator_cache):
        # try starting the machine by pressing the buttons (defined in the wiring all together)
        #  until all lights (defined in the indicator targets) are in the correct state
        #print("Analysing...", indicator_lights, presses, "deep", indicator_cache)

        if presses > self.presses: return

        # if indicator is the same as target, we can finish
        if indicator_lights == self.indicator_targets:

            #print(presses, "Presses needed")
            if self.presses > presses:
                print("Solution", self.pretty_print(indicator_lights), "found",
                      self.pretty_print(self.indicator_targets))
                self.presses = presses
                print(presses, "Presses needed")
                return
            else: return
            #return [0]

        # check cache if we've seen this solution already
        local_indicator_cache = []
        local_indicator_cache += indicator_cache
        if indicator_lights in indicator_cache:
            #print("Already seen this, will not search further")
            #return [1]
            return
        else:
            local_indicator_cache.append(indicator_lights)

        #print("Starting from", self.pretty_print(indicator_lights))

        button_presses = []
        for button_wiring in self.button_wirings:
            if (indicator_lights ^ self.indicator_targets) & button_wiring > 1:
                #print("Button", self.pretty_print(button_wiring), "could be of help for", self.pretty_print(indicator_lights), self.pretty_print(indicator_lights ^ button_wiring))
                #FactoryMachine.press_buttons(indicator_lights, button_wiring)
                #future_button_presses = self.start_machine(indicator_lights ^ button_wiring)
                self.start_machine(indicator_lights ^ button_wiring, presses+1, local_indicator_cache)

                #print("Presses", future_button_presses)
                #button_presses.append(list(lambda x: x + 1, future_button_presses))
                #future_button_presses.sort()
                #future_button_presses[0] += 1
                #print("button press", future_button_presses[0])
                #button_presses.append(future_button_presses[0])
                #map(lambda x: x + 1, button_presses))
            else:
                #print("Skip Button")
                continue
            #FactoryMachine.press_buttons(self.indicator_lights, self.button_wirings[0])
        #if not button_presses:
            #print("nothing found")
            #return
            #return [99]
        #else:
        return
            #return button_presses

    def start(self):
        #button_presses = self.start_machine(self.indicator_lights)
        self.start_machine(self.indicator_lights, 0, [])
        #button_presses.sort()
        #print("Solution", button_presses[0]+1)
        #return(button_presses[0]+1)
        return self.presses

machines, factory_machines = [], []
with open("input.txt", "r") as file:
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
for factory_machine in factory_machines:
    max_press = factory_machine.start()
    print("Sub-Solution (", i, "):", max_press)
    i += 1
    max_presses += max_press

print("Solution:", max_presses)
