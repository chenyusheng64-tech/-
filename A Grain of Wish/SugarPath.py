# SugarPath.py
import pygame

WIDTH, HEIGHT = 1500, 750

class SugarPath:
    def __init__(self, light_system, decay_rate):
        self.light_system = light_system
        self.decay_rate = decay_rate
        self.trail_segments = []
        self.current_path = None
        self.trail_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    def start_new_trail(self, record):
        if record["granules_count"] > 0:
            self.current_path = []
            self.trail_segments.append(self.current_path)
            #print(self.trail_segments)

    def add_trail_point(self, record, player_rect_center):
        if self.current_path is not None and record["granules_count"] > 0:
            new_point = player_rect_center
            self.current_path.append(new_point)
            record["granules_count"] -= self.decay_rate
            record["granules_count"] = max(0, record["granules_count"])
            self.light_system.add_trail_light(new_point)

    def stop_trail(self):
        self.current_path = None

    def draw(self, screen):
        self.trail_surface.fill((0, 0, 0, 0))
        for path in self.trail_segments:
            if len(path) > 1:
                pygame.draw.lines(self.trail_surface, (152, 245, 255, 120), False, path, 20)
        screen.blit(self.trail_surface, (0, 0))
    
    '''
    def clear(self):
        self.trail_segments.clear()
        self.light_system.clear_sugar_light()
    '''