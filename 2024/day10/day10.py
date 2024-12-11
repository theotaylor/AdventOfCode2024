#after finding each 9, then use depth first to find possible trails


class AdventDay10:

    def __init__(self):
        self.arr_2d = []
        with open('inputday10.txt', 'r') as file:
            for line in file:
                self.arr_2d.append([int(digit) for digit in line.strip()])
        self.rows = len(self.arr_2d)
        self.cols = len(self.arr_2d[0])
        self.trailhead_sum = 0

    def all_possible_trails(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.arr_2d[i][j] == 0:
                    self.trailhead_sum += self.trails_from_pos(i, j)
        print(self.trailhead_sum)
        

    def trails_from_pos(self, r, c):
        trail_count = [0]
        visited = set()

        def dfs(x, y):
            #if (x, y) in visited:
            #    return
            #visited.add((x, y))
            if self.arr_2d[x][y] == 9:
                trail_count[0] += 1
                return
        
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.valid_position(self.arr_2d[x][y], nx, ny):
                    dfs(nx, ny)
        dfs(r, c)
        return trail_count[0]
    
    def valid_position(self, val, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols and self.arr_2d[r][c] == val + 1
            

if __name__ == '__main__':
    day10 = AdventDay10()
    day10.all_possible_trails()
    
