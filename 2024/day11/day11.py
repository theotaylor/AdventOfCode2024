#0 1 10 99 999
#1 2024 1 0 9 9 2021976

#if stone=0 -> replaced with 1
#if stone has even number of digits -> replaced with 2 stones of those digits split (don't keep extra leading 0s)
#if none of rules apply: multiply is by 2024
import time

class AdventDay11:

    def __init__(self):
        self.blinks = 75
        self.initial_list = []
        with open('inputday11.txt', 'r') as file:
            content = file.readline()
            self.initial_list = [int(x) for x in content.split()]
        
    
    def solve(self):
        stone_counts = {}
        for num in self.initial_list:
            stone_counts[num] = stone_counts.get(num, 0) + 1
        
        for _ in range(self.blinks):
            stone_counts = self.blink(stone_counts)
        
        print("Final stone counts:", stone_counts)
        print("Total Stones:", sum(stone_counts.values()))
        
        
    def blink(self, stone_counts):
        new_stone_counts = {}
        
        for num, count in stone_counts.items():
            if num == 0:
                new_stone_counts[1] = new_stone_counts.get(1, 0) + count
            elif len(str(num)) % 2 == 0:
                part1, part2 = self.split_number(num)
                new_stone_counts[part1] = new_stone_counts.get(part1, 0) + count
                new_stone_counts[part2] = new_stone_counts.get(part2, 0) + count
            else:
                new_stone_counts[num * 2024] = new_stone_counts.get(num * 2024, 0) + count
        return new_stone_counts

    def split_number(self, num):
        digits = str(num)
        mid = len(digits) // 2
        return int(digits[:mid]), int(digits[mid:])
    
if __name__ == '__main__':
    start_time = time.time()
    day11 = AdventDay11()
    day11.solve()
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Execution Time: {elapsed_time:.2f} ms")




