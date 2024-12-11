

class AdventDay5:

    def __init__(self):
        self.mapping_rules = {}
        self.orders = []
        self.total = 0
        with open('inputday5.txt', 'r') as file:
            onRules = True
            for line in file:
                line = line.strip()
                if line == '':
                    onRules = False
                else:
                    if onRules:
                        line = line.split('|')
                        key = int(line[0])
                        val = int(line[1])
                        if line[0] not in self.mapping_rules:
                            self.mapping_rules[key] = []
                        self.mapping_rules[key].append(val)
                    else:
                        line = line.split(',')
                        int_line = []
                        for n in line:
                            int_line.append(int(n))
                        self.orders.append(int_line)
        
        
    def check_each_order(self):
        middle_value_sum = 0
        for order in self.orders:
            print(order)
            order_list = order.copy()
            rules_followed = True
            while order:
                curr = order.pop()
                if curr in self.mapping_rules:
                    for num in order:
                        if num in self.mapping_rules[curr]:
                            rules_followed = False
                            order = []
                            break


            if rules_followed:
                middle_value = order_list[len(order_list) // 2]
                print(middle_value)
                middle_value_sum += middle_value
        print(middle_value_sum)
            
                    
if __name__ == '__main__':
    day5 = AdventDay5()
    day5.check_each_order()










#could use a hashmap to map the data
#brute force: we need to see if rules are broken.
#we could loop 
#29, 53, 61, 47, 75
#

#{47: [53, 13, 61, 29]}
#{29: [13]}
#{53: [29, 13]}
#{97: [13, 61, 47, 29, 53, 75]}
#{75: [29, 53, 47, 61, 13]}
#{61: [13, 53, 29]}

#start at 29. if any of the nums are opp[29] rule is broken
#then go to 53. none.
#then 61. none. 
#then 47. none.
#then 75. done.

## 61,13,29

#start at 61. 13 is in. so doesn't work.








# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47