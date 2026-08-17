from PIL import Image
from io import BytesIO
from rich.text import Text

def bytes_to_ascii(image_bytes: bytes, target_width: int = 60) -> Text:
    img = Image.open(BytesIO(image_bytes))

    ratio = img.height / img.width
    target_height = int(target_width * ratio * 0.5)

    img = img.resize((target_width, target_height), Image.Resampling.LANCZOS) # image smoothing

    result = Text()
    for y in range(target_height):
        for x in range(target_width):        
            r, g, b = img.getpixel((x, y))
            result.append("█", style=f"rgb({r},{g},{b})") 
            # getting pixels and adding them to result
        result.append("\n")

    return result

        
        


