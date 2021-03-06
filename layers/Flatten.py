import numpy as np


class Flatten:
    def __init__(self):
        self.input_array = None
        self.result = 0
        self.name = "Flatten"

    def calculate(self):
        input_shape = self.input_array.shape
        result = self.input_array
        temp = self.input_array[0]
        for i in range(len(input_shape)-1):
            for slices in result[1:]:
                temp = np.concatenate((temp,slices),axis=0)
            result = temp
            temp = temp[0]
        self.result = result 
        return self.result

