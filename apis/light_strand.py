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
        self.playing = False  # Used to start and stop animations
        self.current_animation = None  # Used to make sure only one animation goes at once

    def get_pixel(self, pixel_index):
        return self.pixels[pixel_index]

    def set_pixel(self, pixel_index, color):
        if pixel_index < self.num_pixels:
            self.pixels[pixel_index] = color
            self.pixels.show()
        else:
            raise IndexError(f"Pixel index out of bounds. {pixel_index} is not less than {self.num_pixels}")

    def fill_range(self, start_index, end_index, color):
        if start_index < end_index and (0 < start_index < self.num_pixels and 0 < end_index < self.num_pixels):
            for i in range(start_index, end_index):
                self.pixels[i] = color
            self.pixels.show()
        else:
            raise IndexError(f"Indices out of bounds or in incorrect order. Start: {start_index}. End: {end_index}")

    def clear(self):
        self.pixels.fill((0, 0, 0))
        self.playing = False
        self.pixels.show()

    def fill(self, color):
        self.pixels.fill(color)
        self.pixels.show()

    def set_alternating(self, color_one, color_two):
        for i in range(self.num_pixels):
            if i % 2 == 1:
                self.pixels[i] = color_one
            else:
                self.pixels[i] = color_two
        self.pixels.show()

    def set_tri_alternating(self, color_one, color_two, color_three):
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
            self.set_alternating(color_one, color_two)
            color_one, color_two = color_two, color_one
            self.pixels.show()
            time.sleep(1)

    def start_cycling(self, color_one, color_two, color_three):
        self.playing = True
        self.current_animation = 1
        while self.current_animation == 1 and self.playing:
            self.set_tri_alternating(color_one, color_two, color_three)
            color_one, color_two, color_three = color_two, color_three, color_one
            self.pixels.show()
            time.sleep(1)

    def stop_playing(self):
        self.playing = False



