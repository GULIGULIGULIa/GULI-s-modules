# usefull for projects that use the terminal allat
filename = __file__.split("\\")[-1] 
print(f"(Loading module: {filename}..")

class C:
    BLACK       = "\033[0;30m"
    RED         = "\033[0;31m"
    GREEN       = "\033[0;32m"
    BROWN       = "\033[0;33m"
    BLUE        = "\033[0;34m"
    PURPLE      = "\033[0;35m"
    CYAN        = "\033[0;36m"
    LIGHT_GRAY  = "\033[0;37m"
    DARK_GRAY   = "\033[1;30m"
    LIGHT_RED   = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW      = "\033[1;33m"
    LIGHT_BLUE  = "\033[1;34m"
    LIGHT_PURPLE= "\033[1;35m"
    LIGHT_CYAN  = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD     = "\033[1m"
    FAINT    = "\033[2m"
    DIM      = "\033[22m"
    ITALIC   = "\033[3m"
    UNDERLINE= "\033[4m"
    NEGATIVE = "\033[7m"
    CROSSED  = "\033[9m"
    END      = "\033[0m"

def UP(lines):
    return f"\033[{lines}A"

def DOWN(lines):
    return f"\033[{lines}B"

def RIGHT(amount):
    return f"\033[{amount}C"

def LEFT(amount):
    return f"\033[{amount}D"

def COLUMN(column):
    return f"\033[{column}G"

def SET_POS(line, column):
    return f"\033[{line};{column}H"

def CLEAR_TERMINAL():
    return f"\033[2J"

def CLEAR_LINE():
    return f"\r\033[2K"

def grad(text="\nU DIDN'T ADD TEXT DUMBASS\n", color_list=[[200,200,200],[200,200,200]]):
    steps = len(text)
    num_segments = len(color_list) - 1
    steps_per_segment = steps / num_segments
    result = []
    
    for i, char in enumerate(text):
        if steps > 1:
            # Determine which color segment this character belongs to
            segment = min(int(i / steps_per_segment), num_segments - 1)
            seg_start = segment * steps_per_segment
            seg_end = (segment + 1) * steps_per_segment
            # Calculate the interpolation factor inside the current segment
            factor = (i - seg_start) / (seg_end - seg_start)
        else:
            segment, factor = 0, 0.0
            
                # Ensure c1 and c2 are treated as tuples/lists with 3 items
        c1 = color_list[segment]
        c2 = color_list[segment + 1]
        
        # Line 76 fix: safely access index 0, 1, and 2
        r = int(c1[0] + (c2[0] - c1[0]) * factor)
        g = int(c1[1] + (c2[1] - c1[1]) * factor)
        b = int(c1[2] + (c2[2] - c1[2]) * factor)
        
        # Append the ANSI RGB code and character
        result.append(f"\x1b[38;2;{r};{g};{b}m{char}")
        
    # Return the string with a trailing style reset code
    return "".join(result) + "\x1b[0m"

def RGB_end():
    return "\x1b[0m"

class G:
    # --- THE CLASSICS ---
    RAINBOW      = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (139, 0, 255)]
    SUNSET       = [(255, 94, 87), (255, 159, 67), (255, 205, 86), (253, 121, 168), (108, 92, 231)]
    TWILIGHT     = [(15, 32, 67), (84, 90, 182), (179, 107, 202), (249, 133, 133), (255, 211, 153)]

    # --- CYBER & SCI-FI ---
    VAPORWAVE    = [(255, 113, 206), (1, 205, 254), (5, 255, 161), (185, 103, 255), (255, 251, 150)]
    AURORA       = [(5, 230, 140), (0, 180, 216), (123, 44, 191), (224, 170, 255)]
    MATRIX_DRIFT = [(0, 15, 0), (0, 75, 15), (0, 150, 30), (50, 255, 70), (200, 255, 210)]

    # --- NATURE & MOODS ---
    DEEP_OCEAN   = [(0, 7, 45), (0, 28, 85), (0, 53, 102), (0, 119, 182), (72, 202, 228)]
    FOREST_FIRE  = [(34, 76, 56), (143, 184, 112), (247, 147, 30), (218, 44, 56), (106, 4, 15)]
    GLACIER      = [(224, 251, 252), (152, 193, 217), (61, 90, 128), (41, 50, 65)]

    # Primary & Secondary Colors
    red          = (255, 0, 0)
    orange       = (255, 127, 0)
    yellow       = (255, 255, 0)
    green        = (0, 255, 0)
    cyan         = (0, 255, 255)
    blue         = (0, 0, 255)
    magenta      = (255, 0, 255)
    purple       = (128, 0, 128)

    # Neon & Cyberpunk Colors
    neon_pink    = (255, 0, 128)
    neon_purple  = (187, 0, 255)
    electric_cyan= (0, 225, 255)
    toxic_green  = (57, 255, 20)

    # Soft Pastels
    pastel_pink  = (255, 179, 186)
    pastel_peach = (255, 223, 186)
    pastel_yellow= (255, 255, 186)
    pastel_green = (186, 255, 201)
    pastel_blue  = (186, 225, 255)

    # Earthy & Rich Tones
    crimson      = (220, 20, 60)
    gold         = (255, 215, 0)
    lime         = (50, 205, 50)
    teal         = (0, 128, 128)
    indigo       = (75, 0, 130)

    # Monochromes
    white        = (255, 255, 255)
    gray         = (128, 128, 128)
    black        = (0, 0, 0)

def grad_x(x, color_list, length=100):
    x = max(0.0, min(1.0, x / length))
    num_segments = len(color_list) - 1
    segment = min(int(x * num_segments), num_segments - 1)
    factor = (x * num_segments) - segment

    c1 = color_list[segment]
    c2 = color_list[segment + 1]

    r = int(c1[0] + (c2[0] - c1[0]) * factor)
    g = int(c1[1] + (c2[1] - c1[1]) * factor)
    b = int(c1[2] + (c2[2] - c1[2]) * factor)

    result = f"\x1b[38;2;{r};{g};{b}m"
    return result


def rgb(r=200, g=200, b=200):
    result = f"\x1b[38;2;{r};{g};{b}m"
    return result



def info_colors():
    entries = [name for name, value in vars(G).items() if not name.startswith('_') and isinstance(value, list)]

    print(
        "\n"
        f"{'NAME':<14}"
    )
    print("-" * 35)


    for name in entries:
        colors = colors = getattr(G, name)
        print(grad(name, colors))
        print(grad("▀"*35, colors))
    print(
        "Use ANSI.grad('text', [ANSI.G.rainbow / ANSI.G.red / [0, 255, 255]])"
    )

def credit():
    print(
        f"{UP(1)+CLEAR_LINE()+C.GREEN}Loaded Module:{C.END} Guli's {C.BOLD+C.LIGHT_CYAN}A{C.LIGHT_BLUE}N{C.LIGHT_RED}S{C.DIM+C.YELLOW}I{C.END} decoder."
        )
credit()