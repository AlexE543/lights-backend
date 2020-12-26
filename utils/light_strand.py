import board
import neopixel
import time

GPIO_PIN = board.D18

ANIMATIONS = {
    0: "Alternating two colors",
    1: "Alternating three colors"
}


class LightStrand:

    def __init__(self, num_pixels, brightness, auto_write=False):
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(GPIO_PIN, num_pixels, brightness=brightness, auto_write=auto_write)
        self.playing = False
        self.current_animation = None

    def get_pixel(self, pixel_index):
        return self.pixels[pixel_index]

    def set_pixel(self, pixel_index, color, show=True):
        self.playing = False
        if pixel_index < self.num_pixels:
            self.pixels[pixel_index] = color
            if show:
                self.pixels.show()
        else:
            raise IndexError(f"Pixel index out of bounds. {pixel_index} is not less than {self.num_pixels}")

    def fill_range(self, start_index, end_index, color):
        self.playing = False
        if start_index < end_index and (0 < start_index < self.num_pixels and 0 < end_index < self.num_pixels):
            for i in range(start_index, end_index):
                self.pixels[i] = color
            self.pixels.show()
        else:
            raise IndexError(f"Indices out of bounds or in incorrect order. Start: {start_index}. End: {end_index}")

    def clear(self):
        self.playing = False
        self.pixels.fill((0, 0, 0))
        self.pixels.show()

    def fill(self, color):
        self.playing = False
        self.pixels.fill(color)
        self.pixels.show()

    def set_alternating(self, color_one, color_two, animate=False):
        self.playing = animate
        for i in range(self.num_pixels):
            if i % 2 == 1:
                self.pixels[i] = color_one
            else:
                self.pixels[i] = color_two
        self.pixels.show()

    def set_tri_alternating(self, color_one, color_two, color_three, animate=False):
        self.playing = animate
        for i in range(self.num_pixels):
            if i % 3 == 2:
                self.pixels[i] = color_one
            elif i % 3 == 1:
                self.pixels[i] = color_two
            else:
                self.pixels[i] = color_three
        self.pixels.show()

    def start_alternating(self, color_one, color_two):
        self.playing = True
        self.current_animation = 0
        while self.current_animation == 0 and self.playing:
            self.set_alternating(color_one, color_two, animate=True)
            color_one, color_two = color_two, color_one
            self.pixels.show()
            time.sleep(1)

    def start_tri_alternating(self, color_one, color_two, color_three):
        self.playing = True
        self.current_animation = 1
        while self.current_animation == 1 and self.playing:
            self.set_tri_alternating(color_one, color_two, color_three, animate=True)
            color_one, color_two, color_three = color_two, color_three, color_one
            self.pixels.show()
            time.sleep(1)

    def flash_fade(self, color):
        self.playing = False
        for i in range(5):
            self.fill(color)
            color = (int(x*.75) for x in color)

    def slide_left(self, color):
        self.playing = False
        for i in range(0, self.num_pixels, 1):
            self.set_pixel(i, color)

    def slide_right(self, color):
        self.playing = False
        for i in range(self.num_pixels-1, -1, -1):
            self.set_pixel(i, color)

    def slide_middle(self, color):
        self.playing = False
        middle = self.num_pixels//2
        for i in range(0, middle):
            self.set_pixel(middle-i, color, show=False)
            self.set_pixel(middle+i, color, show=False)
            self.pixels.show()

    def shoot_left(self, color):
        prev = 0
        for i in range(0, self.num_pixels, 3):
            self.set_pixel(prev, (0, 0, 0), show=False)
            self.set_pixel(i, color, show=False)
            prev = i
            self.pixels.show()

    def shoot_right(self, color):
        prev = -1
        for i in range(self.num_pixels-1, -1, -3):
            self.set_pixel(prev, (0, 0, 0), show=False)
            self.set_pixel(i, color, show=False)
            prev = i
            self.pixels.show()

    def stop_playing(self):
        self.playing = False
