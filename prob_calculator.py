import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for key, value in kwargs.items():
            self.contents += [key] * value

    def draw(self, num_to_draw):
        """Takes in the number of balls to draw, removes each ball drawn from the contents list and returns balls chosen in a list of strings"""
        hat = copy.deepcopy(self.contents)
        chosen = list()
        count = 0
        while count < num_to_draw:
            try:
                ball = random.choice(self.contents)
                chosen.append(ball)
                self.contents.remove(ball)
                count += 1
            except IndexError:
                ball = random.choice(hat)
                count += 1
        return chosen


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Returns the probability"""
    
    expected = len(expected_balls.keys())
    M = 0 #successful
    
    for x in range(0, num_experiments):
        balls_picked = dict()
        hat_copy = copy.deepcopy(hat.contents)
        removed = list()
        for x in range(0, num_balls_drawn):
            success = 0
            try:
                ball = random.choice(hat_copy)
                hat_copy.remove(ball)
                removed.append(ball)
            except IndexError:
                hat_copy.extend(removed)
                ball = random.choice(hat_copy)
            if ball in expected_balls:
               balls_picked[ball] = balls_picked.get(ball, 0) + 1
            
        for color in balls_picked:
            if balls_picked[color] < expected_balls[color] :
                success = 0
                break
            else:
                success += 1    
        
            if success == expected:
                M += 1    

    probability = M / num_experiments
    return probability
