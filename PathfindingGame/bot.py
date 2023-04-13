import json
import timeit
from astar import *
import import_data as dt
from bot_utils import output_file
from map import Map
class Bot:
    def __init__(self, name, pos, end, status, score, grid):
        self.pos = Cell(pos[0], pos[1])
        self.end = Cell(end[0], end[1])
        self.name = name
        self.status = status
        self.score = score
        self.path = None
        self.start_time = None
        self.grid = grid
    def move(self, start, dest):
            #convert_to_direction
        dir = self.convert_to_step(start, dest)
            #write direction to txt file
        self.write_to_text(dir, output_file)
            #update status
            #check other bot
            #get new end value if other bot too close to old end
            #(new end will be taken later)
    def check_other(self, bot):
        ## if input_1 > input_2 update new dest for self
        self.pos.update_neighbors(self.grid.map)
        if bot.pos in self.pos.neighbors:
            self.grid.obstacles.append(bot.pos.coor())
            temp = self.grid.obstacles
            self.grid.update_map(temp)
        if self.go_middle_check(self.find_path(), bot.find_path(), 0.3):
            self.end = self.get_new_end()
        
        ## if input_1 < input_2 update new dest for bot
        ## update astar coin into bot.dest
    def go_middle_check(self, path_1, path_2, percentage):
        if (len(path_1) - len(path_2))/len(path_1) > percentage:
            return True
        return False
    def find_path(self):
        path = AStar(self).find_shortest_path(self.grid)
        self.start_time = AStar(self).start_time
        return path
    def get_all_neighbor(self,point):
        return [[point[0], point[1]-1],
                [point[0], point[1]+1],
                [point[0]-1, point[1]],
                [point[0]+1, point[1]]]
    def get_new_end(self):
        grid = Map()
        midpoint = Cell(round(self.grid.width/2), round(self.grid.height/2))
        if midpoint.coor() in self.grid.obstacles:
            visited = []
            queue = []
            visited.append(midpoint.coor())
            queue.append(midpoint.coor())
            while queue:
                m = queue.pop(0)
                for neighbor in self.get_all_neighbor(m):
                    if neighbor not in self.grid.obstacles:
                        return Cell(neighbor[0], neighbor[1])
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
        return midpoint
    def convert_to_step(self, start, dest):
            # current [3, 2] vs [4, 2]
        dir = None
        if (start[0] > dest[0] ) and (start[1]  == dest[1]):
            stop_time = timeit.default_timer()
            dir = 'up'
            return [dir, (stop_time - self.start_time)*1000]
        if (start[0] < dest[0] ) and (start[1]  == dest[1]):
            stop_time = timeit.default_timer()
            dir = 'down'
            return [dir, (stop_time - self.start_time)*1000]
        if (start[0] == dest[0] ) and (start[1]  > dest[1]):
            stop_time = timeit.default_timer()
            dir = 'left'
            return [dir, (stop_time - self.start_time)*1000]
        if (start[0] == dest[0] ) and (start[1]  < dest[1]):
            stop_time = timeit.default_timer()
            dir = 'right'
            return [dir, (stop_time - self.start_time)*1000]
    def write_to_json(self):
        if self.name == 'tadao':
            with open("maze_metadata.json", "r") as jsonFile:
                data = json.load(jsonFile)
            data["bots"][0]['status'] = "stop"
            with open("maze_metadata.json", "w") as jsonFile:
                json.dump(data, jsonFile)
        if self.name == 'top':
            with open("maze_metadata.json", "r") as jsonFile:
                data = json.load(jsonFile)
            data["bots"][1]['status'] = "stop"
            with open("maze_metadata.json", "w") as jsonFile:
                json.dump(data, jsonFile)
    def write_to_text(self, content, filename):
        f = open(filename, 'a')
        f.close()
        f = open(filename, 'r')
        temp = f.read()
        f.close()
        f = open(filename, 'w')
        f.write(content[0] + ' ' + str(content[1]) + '\n')
        f.write(temp)
        f.close()