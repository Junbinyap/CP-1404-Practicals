
COLOUR_TO_CODE = {"AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a", "AliceBlue": "#f0f8ff", "BanyPink": "#f4c2c2",
                "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7",
                "BananaYellow": "#ffe135", "BarnRed": "#7c0a02"}
print(COLOUR_TO_CODE)

while True:
    colour_name = input("Enter the name of colour (or press Enter to quit): ").strip()
    if colour_name == "":
        print("Goodbye!")
    elif colour_name in COLOUR_TO_CODE:
         print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    else:
         print("Invalid colour name")
