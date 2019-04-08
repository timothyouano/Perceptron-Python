import math
import random

class Perceptron:

    INPUT_STATE = [0] * 35
    LETTER = []
    WEIGHTS = []
    PATTERN_COUNT = 0
    EXPECTED = []
    LEARNING_RATE = 0
    MAX_ITERATION = 0

    def __init__(self, letter, expected, learning_rate, max_iteration):
        self.LETTER = letter
        self.EXPECTED = expected
        self.LEARNING_RATE = learning_rate
        self.MAX_ITERATION = max_iteration
    
    def set_input_state(self, index, value):
        self.INPUT_STATE[index] = value

    def get_input_state(self, index):
        return self.INPUT_STATE[index]
    
    def get_letter(self, index):
        return self.LETTER[index]

    def check_random(self, randomizer):
        ctr = 0
        for i in range(len(randomizer)):
            if randomizer[i]:
                ctr += 1
        return ctr

    def calculate_output(self, generated, weights):
        sum = 0.0
        data = self.LETTER[generated].replace('\n', '')
        data = data.split(',')
        for j in range(self.PATTERN_COUNT):
            sum += int(data[j]) * weights[j]
        sum += weights[35]
        return 1 if sum >= 0 else 0
    
    def train(self):
        self.PATTERN_COUNT = len(self.LETTER)

        # Randomize weights
        for x in range(self.PATTERN_COUNT+1):
            self.WEIGHTS.append(random.random())
        iteration = 0
        global_error = 999
        output = 0.0
        randomizer = [False] * len(self.WEIGHTS)
        generated = 0

        while global_error != 0 and iteration != self.MAX_ITERATION:
            global_error = 0
            # Randomize Feeded Pattern
            randomizer.clear()
            randomizer = [False] * len(self.WEIGHTS)
            while self.check_random(randomizer) != 26:
                generated = math.floor(random.random() * 26)
                if randomizer[generated] == False:
                    # calculate output
                    output = self.calculate_output(generated, self.WEIGHTS)
                    # calculate error
                    local_error = self.EXPECTED[generated] - output
                    if local_error != 0:
                        # update weights
                        splitted = self.LETTER[generated].replace('\n', '')
                        splitted = splitted.split(',')
                        for i in range(self.PATTERN_COUNT):
                            self.WEIGHTS[i] = self.WEIGHTS[i] + self.LEARNING_RATE * local_error * int(splitted[i])
                    randomizer[generated] = True
                    # Convert error to absolute
                    global_error += abs(local_error)
            print("Iteration: " + str(iteration) + " Error: " + str(global_error))
            iteration += 1

        print("Finished Training")

    def recognize(self):
        sum = 0
        for i in range(len(self.WEIGHTS) - 1):
            sum += self.INPUT_STATE[i] * self.WEIGHTS[i]
        sum += self.WEIGHTS[35]
        print(sum)
        return "VOWEL" if sum >= 0 else "CONSONANT"