"""Build MemeEngine.

Ingest and parse.
"""
import uuid
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Build MemeEngine.

    Init and make_meme.
    """

    def __init__(self, output_dir):
        """Return a boolean file is can ingest."""
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500):
        """Return a boolean file is can ingest."""
        try:
            image = Image.open(img_path)
            if image.size[0] != width:
                width_percent = (width / float(image.size[0]))
                height = int((float(image.size[1]) * float(width_percent)))
                image.thumbnail((width, height), Image.LANCZOS)

            im_draw = ImageDraw.Draw(image)
            im_font = ImageFont.truetype('MemeGenerator/font/AlexBrush-Regular.ttf', 40)
            words = text.split()
            grouped_words = [' '.join(words[i: i + 5]) for i in range(0, len(words), 5)]
            position = 10
            for word in grouped_words:
                im_draw.text((10, position), word, font=im_font)
                position += im_font.size
            
            im_draw.text((position + 10, position + 10), f'{author}', font=im_font)
            save_path = f"{self.output_dir}/meme-img-{str(uuid.uuid4())}.png"
            image.save(save_path)

            return save_path
        except Exception as e:
            raise e
