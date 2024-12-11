import re

class AdventDay3:

    def __init__(self):
        self.text_input = ''
        with open('inputday3.txt', 'r') as file:
            for line in file:
                self.text_input += line

        self.valid_instructions = []
        self.p1 = 0
        self.p2 = 0
    
    def find_valid_instructions(self):
        #self.valid_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", self.text_input)
        self.valid_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", self.text_input)
        #print(self.valid_instructions)
        
    def calculate_product_p1(self):
        for op in self.valid_instructions:
            nums = re.findall(r"\d{1,3}", op)
            print(nums)
            self.p1 += int(nums[0]) * int(nums[1])
        print(self.p1)

    def calculate_product_p2(self):
        mult = True
        for instr in self.valid_instructions:
            print(instr)
            if instr == 'do()':
                mult = True
            elif instr == 'don\'t()':
                mult = False
            elif mult:
                nums = re.findall(r"\d{1,3}", instr)
                self.p2 += int(nums[0]) * int(nums[1])
        print(self.p2)


if __name__ == '__main__':
    day3 = AdventDay3()
    day3.find_valid_instructions()
    #day3.calculate_product_p1()
    day3.calculate_product_p2()