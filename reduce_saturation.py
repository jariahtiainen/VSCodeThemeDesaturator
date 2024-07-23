import json
from colormath.color_objects import sRGBColor, HSVColor
from colormath.color_conversions import convert_color

def reduce_saturation(hex_color, reduction_factor):
    if len(hex_color) == 4:  # Handles colors like #FFF
        hex_color = '#' + ''.join([c*2 for c in hex_color[1:]])
    if len(hex_color) == 9:  # Handles colors like #00000050
        hex_color = hex_color[:7]  # Strip out the alpha component for now

    rgb = sRGBColor.new_from_rgb_hex(hex_color)
    hsv = convert_color(rgb, HSVColor)
    hsv.hsv_s *= reduction_factor
    rgb = convert_color(hsv, sRGBColor)
    return rgb.get_rgb_hex()

def process_colors(data, reduction_factor):
    for key, value in data.items():
        if isinstance(value, str) and value.startswith('#'):
            try:
                data[key] = reduce_saturation(value, reduction_factor)
            except Exception as e:
                print(f"Error processing color {value}: {e}")
        elif isinstance(value, dict):
            process_colors(value, reduction_factor)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    process_colors(item, reduction_factor)

try:
    with open('your_theme.json', 'r') as f:
        theme = json.load(f)
except json.JSONDecodeError as e:
    print(f"JSON decode error: {e}")
    raise

saturation_reduction_factor = 0.5  # Adjust this factor (0.0 to 1.0) to control the level of saturation reduction

process_colors(theme, saturation_reduction_factor)

with open('your_theme_saturation_reduced.json', 'w') as f:
    json.dump(theme, f, indent=2)

print("Saturation reduction complete. Check the new file: your_theme_saturation_reduced.json")
