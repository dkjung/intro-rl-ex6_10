import numpy as np
import random
from windy_gridworld import Direction
from windy_gridworld import WindyGridworld, KingsWindyGridworld, StochasticWindKWG


class SarsaAgent:
    """Agent for SARSA learning of the gridworld"""

    def __init__(self, game: WindyGridworld):
        self.game = game
        self.alpha = 0.1
        self.epsilon = 0.1
        self.gamma = 1.0

        self.q = np.zeros(shape=(game.height, game.width, len(game.dir_list),), dtype=float)

    def choose_action(self, ) -> tuple[Direction, int]:
        """Choose next action"""
        p = random.random()
        if p <= self.epsilon:
            a_idx = random.randrange(0, len(self.game.dir_list))
            a = self.game.dir_list[a_idx]
        else:
            y, x = self.game.cur
            a_idx = np.argmax(self.q[y, x])
            a = self.game.dir_list[a_idx]
        return a, a_idx

    def learn(self, cnt: int):
        """Update q with SARSA"""
        avg_return = 0
        for i in range(cnt):
            self.game.reset()
            return_ = 0
            a, ai = self.choose_action()
            while not self.game.complete:
                sy, sx = self.game.cur
                reward, is_done = self.game.step(a)
                sy_, sx_ = self.game.cur
                return_ += reward
                a_, ai_ = self.choose_action()
                self.q[sy, sx, ai] += self.alpha * (reward + self.gamma * self.q[sy_, sx_, ai_] - self.q[sy, sx, ai])
                sy, sx = sy_, sx_
                a, ai = a_, ai_
            avg_return += return_
            if i % 1000 == 999:
                print(i, 'th episode, avg_return = ', avg_return / 1000)
                avg_return = 0

    def print_policy(self, ):
        """Print policy graphically"""
        policy = np.full((self.game.height, self.game.width,), ' ', dtype=str)
        for y in range(self.game.height):
            for x in range(self.game.width):
                a_idx = np.argmax(self.q[y, x])
                dir_ = self.game.dir_list[a_idx]
                if dir_.name == 'UP':
                    policy[y, x] = '↑'
                elif dir_.name == 'DOWN':
                    policy[y, x] = '↓'
                elif dir_.name == 'RIGHT':
                    policy[y, x] = '→'
                elif dir_.name == 'LEFT':
                    policy[y, x] = '←'
                elif dir_.name == 'UPRIGHT':
                    policy[y, x] = '↗'
                elif dir_.name == 'UPLEFT':
                    policy[y, x] = '↖'
                elif dir_.name == 'DOWNRIGHT':
                    policy[y, x] = '↘'
                elif dir_.name == 'DOWNLEFT':
                    policy[y, x] = '↙'
        print(policy)


def main():
    game = [WindyGridworld(), KingsWindyGridworld(), StochasticWindKWG()]
    for g in game:
        agent = SarsaAgent(g)
        agent.learn(10000)
        agent.print_policy()


if __name__ == '__main__':
    main()
