from navigation.collision import Wall
from navigation.environment import Environment
import config as cfg

env = Environment(diff='hard')
env.reset()

difficulty = 'comparison'

if difficulty=='easy':
    # Interesting walls
    env.goal.x = 4*cfg.SLS//5
    env.goal.y = 1*cfg.SLS//4
    env.goal.update_bb()

    env.hazard.x = 0.75*cfg.SLS
    env.hazard.y = 0.45*cfg.SLS
    env.hazard.update_bb()

    env.tank.theta=-0.5
    env.tank.get_bounding_box()

    env.calculate_projections()

elif difficulty == 'medium':
    env.goal.x = 0.85*cfg.SLS
    env.goal.y = 0.7*cfg.SLS
    env.goal.update_bb()

    env.hazard.x = 0.65 * cfg.SLS
    env.hazard.y = 0.65 * cfg.SLS
    env.hazard.update_bb()

    env.WALLS.append(Wall((0.2*cfg.SLS,0),(cfg.SLS, 0.65*cfg.SLS)))

    env.tank.theta = 0.1
    env.tank.get_bounding_box()

    env.calculate_projections()

elif difficulty == 'hard':
    env.goal.x = 0.85 * cfg.SLS
    env.goal.y = 0.55 * cfg.SLS
    env.goal.update_bb()

    env.hazard.x = 0.75 * cfg.SLS
    env.hazard.y = 0.77 * cfg.SLS
    env.hazard.update_bb()

    env.WALLS.append(Wall((0.6 * cfg.SLS, 0), (0.62*cfg.SLS, 0.55 * cfg.SLS)))
    env.WALLS.append(Wall((0.6 * cfg.SLS+100, 0), (0.62 * cfg.SLS +100, 0.55 * cfg.SLS)))
    env.WALLS.append(Wall((0.62*cfg.SLS, 0.55 * cfg.SLS), (0.62 * cfg.SLS + 100, 0.55 * cfg.SLS)))

    env.tank.theta = 0.1
    env.tank.get_bounding_box()

    env.calculate_projections()

elif difficulty == 'comparison':
    env.goal.x = 0.7 * cfg.SLS
    env.goal.y = 0.35 * cfg.SLS
    env.goal.update_bb()

    env.hazard.x = 0.8 * cfg.SLS
    env.hazard.y = 0.5 * cfg.SLS
    env.hazard.update_bb()

    env.tank.theta = -0.45
    env.tank.get_bounding_box()
    env.calculate_projections()

env.render()
input()