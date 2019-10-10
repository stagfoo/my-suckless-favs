# base00 - Default Background
# base01 - Lighter Background (Used for status bars)
# base02 - Selection Background
# base03 - Comments, Invisibles, Line Highlighting
# base04 - Dark Foreground (Used for status bars)
# base05 - Default Foreground, Caret, Delimiters, Operators
# base06 - Light Foreground (Not often used)
# base07 - Light Background (Not often used)
# base08 - Variables, XML Tags, Markup Link Text, Markup Lists, Diff Deleted
# base09 - Integers, Boolean, Constants, XML Attributes, Markup Link Url
# base0A - Classes, Markup Bold, Search Text Background
# base0B - Strings, Inherited Class, Markup Code, Diff Inserted
# base0C - Support, Regular Expressions, Escape Characters, Markup Quotes
# base0D - Functions, Methods, Attribute IDs, Headings
# base0E - Keywords, Storage, Selector, Markup Italic, Diff Changed
# base0F - Deprecated, Opening/Closing Embedded Language Tags, e.g. <?php ?>

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line + '\n' + content)

bspwm_path = "2019/.config/bspwm/bspwmrc"
kitty_path = "./2019/config/kitty/kitty.conf"
polybar_path = "./2019/config/polybar/config"
rofi_path = "./2019/config/rofi/rofi.rasi"

line_prepender(bspwm_path, """
[colors]
background = #000
background-alt = #111
foreground = #dfdfdf
foreground-alt = #555
primary = #00FF00
secondary = #e60053
alert = #bd2c40
""")

# open(kitty_path,"w+") as kitty_file


