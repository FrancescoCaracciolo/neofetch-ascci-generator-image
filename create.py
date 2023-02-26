from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style

def hex_to_bash_color(hex_color:str):
    """Converts hex color to bash color
    """
    hex_color = hex_color.replace("#", "")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f"\033[38;2;{r};{g};{b}m"

# initialize colorama
init()

# Open ascii file with html version of the image
ascii = open("ascii.html")
asciitxt = ascii.read()
ascii.close()

# Analyze text from the ascii
soup = BeautifulSoup(asciitxt, 'html.parser')
elements = soup.find_all(["span", "br"])

# Initialize variables used in the loop
text = ""  # Output text
maxline_length = 0  # Max line length (in content) in the ascii art
linelen = 0  # Line length, auxisliary variable
sium = False
for element in elements:
    if element.name == "span":
        span = element
        try:
            # Get the color from the element
            color = span["style"].split(':')[1]
            text += hex_to_bash_color(color.replace("#", ""))  # Convert the color to bash color and append it to the text
            text += span.text  # Write span content and append it to text
            linelen += len(span.text) # Increase line length
            if linelen > maxline_length:  # Update maxline_length variable
                maxline_length = linelen
        except Exception as e:
            print(e)
    elif element.name == "br":  # New line
        text += "\n"
        linelen = 0  # Reset line length
print(text)  # print result

leng = 0  # Find the longest line (not content)
for line in text.split("\n"):
    if leng < len(line):
        leng = len(line)

# Calculate and print neofetch gap
gap = leng-maxline_length
print("To use the ascii execute the command", "neofetch --ascii output --gap '-{}'".format(gap))

# Save the file
out = open("output", "w+")
out.write(text)
out.close()

