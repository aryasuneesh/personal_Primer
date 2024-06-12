import json
import random
from PIL import Image, ImageDraw, ImageFont
from waveshare_epd import epd5in65f

class ColorQuoteDisplayer:
    def __init__(self, config_path, json_path):
        self.json_path = json_path
        import yaml
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.font = self.config['gfx']['font']
        self.font_path = f'/home/fibel/personal_Primer/assets/fonts/open/schuldruck.ttf'
        self.output_image_path = 'quote_image.png'

    def load_quotes(self):
        with open(self.json_path, 'r') as file:
            return json.load(file)

    def get_random_quote(self):
        quotes = self.load_quotes()
        return random.choice(quotes)

    def generate_quote_image(self, quote):
        # Set up image parameters
        image_width, image_height = 800, 480  # E-ink display resolution
        background_color = (255, 255, 255)  # White background
        text_color = (0, 0, 0)  # Black text

        # Create a blank image with white background
        image = Image.new('RGB', (image_width, image_height), background_color)
        draw = ImageDraw.Draw(image)

        # Load font
        font_size = 24
        font = ImageFont.truetype(self.font_path, font_size)

        # Format the text
        text = f'"{quote["quote"]}"\n\n- {quote["author_of_quote"]}'

        # Calculate text size and position
        text_width, text_height = draw.textsize(quote, font=font)
        text_x = (image_width - text_width) // 2
        text_y = (image_height - text_height) // 2

        # Add text to image
        draw.text((text_x, text_y), text, font=font, fill=text_color)

        # Save image
        image.save(self.output_image_path)

    def display_image(self):
        # Initialize and clear the display
        epd = epd5in65f.EPD()
        epd.init()
        Himage = Image.open(self.output_image_path)
        epd.display(epd.getbuffer(Himage))
        epd.sleep()

    def display_random_quote(self):
        # self.load_quotes()
        quote = self.get_random_quote()
        self.generate_quote_image(quote)
        self.display_image()

