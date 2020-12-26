import board
import neopixel

GPIO_PIN = board.D18


class LightStrand:

    def __init__(self, num_pixels, brightness, auto_write=False):
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(GPIO_PIN, num_pixels, brightness=brightness, auto_write=auto_write)
        print("Setting pixels to white to start")
        self.pixels.fill((1, 1, 1))

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

    def fill(self, color):
        self.pixels.fill(color)
        self.pixels.show()
