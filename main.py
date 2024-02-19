from PIL import ImageGrab, Image
import pyautogui
import random
import time

def capture_screenshot():
    screenshot = pyautogui.screenshot()
    return screenshot

def get_random_pixels(screenshot, num_pixels):
    width, height = screenshot.size
    pixels = []
    for _ in range(num_pixels):
        random_width = random.randint(0, width - 1)
        random_height = random.randint(0, height - 1)
        pixel = screenshot.getpixel((random_width, random_height))
        pixels.append(pixel)
    return pixels

def create_canvas(size):
    return Image.new('RGB', size, "black")

def fill_canvas(canvas, duration_minutes, num_pixels_per_screenshot):
    total_pixels = canvas.width * canvas.height
    current_pixel_count = 0
    start_time = time.time()

    while current_pixel_count < total_pixels and (time.time() - start_time) < (duration_minutes * 60):
        screenshot = capture_screenshot()
        pixels = get_random_pixels(screenshot, num_pixels_per_screenshot)
        for pixel in pixels:
            if current_pixel_count >= total_pixels:
                break
            x = current_pixel_count % canvas.width
            y = current_pixel_count // canvas.width
            canvas.putpixel((x, y), pixel)
            current_pixel_count += 1

def main(duration_minutes):
    screen_width, screen_height = pyautogui.size()
    canvas = create_canvas((screen_width, screen_height))

    total_pixels = screen_width * screen_height
    total_seconds = duration_minutes * 60
    screenshot_interval = 1  # Interval in seconds between screenshots
    num_screenshots = total_seconds / screenshot_interval
    num_pixels_per_screenshot = max(1, total_pixels // int(num_screenshots))

    print(f"Pixels per screenshot to meet the duration: {num_pixels_per_screenshot}")

    fill_canvas(canvas, duration_minutes, num_pixels_per_screenshot)

    canvas.save("final_canvas.png")
    print("Canvas saved as final_canvas.png.")

if __name__ == "__main__":
    duration_minutes = 1  # Adjust as needed
    main(duration_minutes)
