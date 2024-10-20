"""
Hex Colour Lookup Program
"""

# Constant dictionary of colour names and their hex codes
HEX_COLOURS = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
               "Alizarin Crimson": "#e32636", "Amaranth": "#e52b50",
               "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
               "AntiqueWhite2": "#eedfcc"}

# Displays what colours are included within this code
print("\nAll Colours:")
for colour, hex_code in HEX_COLOURS.items():
    print(f"{colour:<3}")

# Input loop for colour names
colour_name = input("Enter colour name: ").strip().title()
while colour_name != "":
    try:
        # Convert input to match dictionary keys and get hex code
        print(f"The hex code for {colour_name} is {HEX_COLOURS[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").strip().title()

print("Goodbye!")
