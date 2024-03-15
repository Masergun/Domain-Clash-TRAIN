import arcade
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Circular Sector Game"

RING_RADIUS = 200
RING_CENTER_X = SCREEN_WIDTH // 2
RING_CENTER_Y = SCREEN_HEIGHT // 2

ARROW_LENGTH = 150
ARROW_SPEED = 3

SECTOR_COLORS = [arcade.color.WHITE, arcade.color.YELLOW, arcade.color.ORANGE, arcade.color.RED]
SECTOR_SCORES = [1, 3, 6, 10]
SECTOR_RATIOS = [0.1, 0.2, 0.3, 0.4]

class Arrow(arcade.Sprite):
    def update(self):
        self.center_x = RING_CENTER_X
        self.center_y = RING_CENTER_Y
        self.angle += ARROW_SPEED

class CircularSectorGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.arrow = None
        self.sector_start_angle = 0
        self.score = 0
        self.score_history = []
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

    def setup(self):
        self.arrow = Arrow(":resources:images/space_shooter/laserBlue01.png", 0.5)
        self.arrow.angle = 0
        self.arrow.center_x = RING_CENTER_X
        self.arrow.center_y = RING_CENTER_Y

    def on_draw(self):
        arcade.start_render()
        self.draw_ring()
        self.draw_arrow()
        self.draw_score_history()
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.BLACK, 20)

    def draw_ring(self):
        angle = self.sector_start_angle
        for i in range(len(SECTOR_COLORS)):
            color = SECTOR_COLORS[i]
            ratio = SECTOR_RATIOS[i]
            arcade.draw_arc_filled(RING_CENTER_X, RING_CENTER_Y, RING_RADIUS, RING_RADIUS,
                                   color, angle, angle + 60 * ratio, 0)
            angle += 60 * ratio

    def draw_arrow(self):
        arrow_end_x = RING_CENTER_X + math.cos(math.radians(self.arrow.angle)) * ARROW_LENGTH
        arrow_end_y = RING_CENTER_Y + math.sin(math.radians(self.arrow.angle)) * ARROW_LENGTH
        arcade.draw_line(RING_CENTER_X, RING_CENTER_Y, arrow_end_x, arrow_end_y, arcade.color.RED, 4)

    def draw_score_history(self):
        for i, color in enumerate(self.score_history):
            arcade.draw_circle_filled(30 + i * 40, 30, 15, color)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arrow_angle = self.arrow.angle % 360
            angle = self.sector_start_angle
            for i in range(len(SECTOR_RATIOS)):
                ratio = SECTOR_RATIOS[i]
                if arrow_angle <= angle + 60 * ratio:
                    self.score += SECTOR_SCORES[i]
                    self.score_history.append(SECTOR_COLORS[i])
                    self.sector_start_angle = angle
                    break
                angle += 60 * ratio

    def on_update(self, delta_time):
        self.arrow.update()

        if self.score >= 30:
            arcade.close_window()
            print("Congratulations! You won the game.")

def main():
    game = CircularSectorGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()