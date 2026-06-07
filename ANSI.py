# usefull for projects that use the terminal allat
filename = __file__.split("\\")[-1] 
print(f"(Loading module: {filename}..")

class F:
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

def grad(text="\nU DIDN'T ADD TEXT DUMBASS\n", color_list=[[200,200,200],[200,200,200]], size=0):
    if size > 0:
        color_list = list(color_list) + [color_list[0]]
    steps = len(text)
    num_segments = len(color_list) - 1
    steps_per_segment = (size if size > 0 else steps) / num_segments
    result = []
    
    for i, char in enumerate(text):
        cycle_i = i % (size if size > 0 else steps)
        if steps > 1:
            segment = min(int(cycle_i / steps_per_segment), num_segments - 1)
            seg_start = segment * steps_per_segment
            seg_end = (segment + 1) * steps_per_segment
            factor = (cycle_i - seg_start) / (seg_end - seg_start)
        else:
            segment, factor = 0, 0.0
            
        c1 = color_list[segment]
        c2 = color_list[segment + 1]
        
        r = int(c1[0] + (c2[0] - c1[0]) * factor)
        g = int(c1[1] + (c2[1] - c1[1]) * factor)
        b = int(c1[2] + (c2[2] - c1[2]) * factor)
        
        result.append(f"\x1b[38;2;{r};{g};{b}m{char}")
        
    return "".join(result) + "\x1b[0m"

def RGB_end():
    return "\x1b[0m"

class C:
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

    # Standard
    red_light    = (255, 100, 100)
    red          = (255, 0,   0  )
    red_dark     = (180, 0,   0  )
    green_light  = (100, 255, 100)
    green        = (0,   200, 0  )
    green_dark   = (0,   120, 0  )
    blue_light   = (70, 130, 255)
    blue         = (10,   20,   255)
    blue_dark    = (10,   10,   180)
    cyan_light   = (100, 255, 255)
    cyan         = (0,   255, 255)
    cyan_dark    = (0,   180, 180)
    yellow_light = (255, 255, 100)
    yellow       = (255, 255, 0  )
    yellow_dark  = (180, 180, 0  )
    magenta_light= (255, 100, 255)
    magenta      = (255, 0,   255)
    magenta_dark = (180, 0,   180)
    orange_light = (255, 180, 80 )
    orange       = (255, 140, 0  )
    orange_dark  = (180, 90,  0  )
    white        = (255, 255, 255)
    gray_light   = (200, 200, 200)
    gray         = (128, 128, 128)
    gray_dark    = (60,  60,  60 )
    black        = (0,   0,   0  )

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
    if isinstance(r, tuple):
        r, g, b = r
    return f"\x1b[38;2;{r};{g};{b}m"

def progress_bar(percent, color_list, length=20):
    filled = int((percent / 100) * length)
    bar = "".join(
        grad_x(i, color_list, length) + '█' if i < filled else rgb(C.gray_dark) + '░'
        for i in range(length)
    )
    return f"[{bar}{F.END}] {grad(f'{percent}%', color_list)} {rgb(C.gray_dark)}| {rgb(C.red_light)}{100 - percent}% remaining{F.END}"

def info_colors(show=["colors", "example", "use", "alternate", "class"]):
    entries = [name for name, value in vars(C).items() if not name.startswith('_') and isinstance(value, list)]

    if "colors" in show:
        print()
        for name in entries:
            colors = colors = getattr(C, name)
            print(grad(name, colors), end=" "*(15-len(name)))
            print(grad("█"*40, colors), grad("█"*40, colors, 20))
            print()
        for name, value in vars(C).items():
            if not name.startswith('_') and isinstance(value, tuple):
                print(rgb(*value) + name, "▇"*(30-len(name)), F.END)
                if "dark" in name or name == "black" or name in ("toxic_green", "pastel_blue", "lime", "white"):
                    print()
    
    if "example" in show:
        print(
            f"\n  {F.BOLD}grad{F.END}(text, color_list, size=0)\n"
            f"  {rgb(C.gray_dark)}basic   {F.END}{grad('grad(\"hello\", [(255,0,0),(0,0,255)])', [(255,0,0),(0,0,255)])}\n"
            f"  {rgb(C.gray_dark)}G class {F.END}{grad('grad(\"hello\", C.RAINBOW)', C.RAINBOW)}\n"
            f"  {rgb(C.gray_dark)}tiling  {F.END}{grad('grad(\"hello\", C.AURORA, 10)  ← cycle size, empty for no cycle', C.AURORA, 10)}\n"
            f"\n  {F.BOLD}rgb{F.END}(r, g, b)\n"
            f"  {rgb(C.gray_dark)}usage   {F.END}{rgb(255,100,50)}rgb(255,100,50) + your text{F.END}\n"
            f"  {rgb(C.gray_dark)}C class {F.END}{rgb(C.neon_pink)}rgb(C.neon_pink) + your text{F.END}\n"
            f"\n  {F.BOLD}grad_x{F.END}(x, color_list, length=100)\n"
            f"  {rgb(C.gray_dark)}usage   {F.END}{grad_x(0, C.SUNSET, 3)}x=0 {grad_x(1, C.SUNSET, 3)}x=1 {grad_x(2, C.SUNSET, 3)}x=2{F.END}  ← x is position along length\n"
            f"  {rgb(C.gray_dark)}tip     {F.END}{rgb(C.gray_dark)}use in loops: grad_x(i, C.SUNSET, total){F.END}\n"
            f"\n  {F.BOLD}alternate{F.END}(text, colors)\n"
            f"  {rgb(C.gray_dark)}basic   {F.END}{alternate('alternate(\"hello\", [C.cyan_light, C.blue_dark])', [C.cyan_light, C.blue_dark])}\n"
            f"  {rgb(C.gray_dark)}multi   {F.END}{alternate('alternate(\"hello\", [C.pastel_blue, C.pastel_green, C.pastel_yellow, C.pastel_pink])', [C.pastel_blue, C.pastel_green, C.pastel_yellow, C.pastel_pink])}\n"
            f"  {rgb(C.gray_dark)}tip     {F.END}{rgb(C.gray_dark)}cycles through colors per character{F.END}\n"
        )
    
    if "use" in show:
        print(
            f"\n"
            f"  {grad('  ANSI use 101  ', C.SUNSET)}\n"
            f"\n"
            f"  {rgb(C.gray_dark)}Solid color with rgb():{F.END}\n"
            f"  {rgb(C.red_dark)}✦ error:{F.END} file not found\n"
            f"  {rgb(C.toxic_green)}✦ success:{F.END} connected\n"
            f"  {rgb(C.yellow)}✦ warning:{F.END} retrying in 3s\n"
            f"\n"
            f"  {rgb(C.gray_dark)}Gradient label with grad():{F.END}\n"
            f"  {grad('  LOADING  ', C.AURORA)}  ← status badge\n"
            f"  {grad('  WARNING  ', C.SUNSET)}  ← swap palette for tone\n"
            f"  {grad('  SUCCESS  ', C.MATRIX_DRIFT)}  ← any color_list works\n"
            f"\n"
            f"  {rgb(C.gray_dark)}Progress_bar() made with grad_x():{F.END}\n"
            f"  {(progress_bar(75, C.DEEP_OCEAN))}\n"
            f"  {(progress_bar(40, C.SUNSET))}\n"
            f"\n"
            f"  {rgb(C.gray_dark)}Combine them:{F.END}\n"
            f"  {grad('  ★ TOP SCORE  ', C.VAPORWAVE)} {rgb(C.gold)}{F.BOLD}9,420pts{F.END}\n"
            f"  {rgb(C.gray_dark)}user:{F.END} {grad('guli', C.AURORA)}  {rgb(C.gray_dark)}status:{F.END} {grad('online', [(0,220,100),(0,180,80)])}\n"
        )
    if "class" in show:
        print(
            f"\n"
            f"  {F.BOLD}Class Overview{F.END}\n"
            f"  {rgb(C.gray_dark)}C {F.END}= Colors  {rgb(C.gray_dark)}→{F.END} tuples like {rgb(C.cyan)}(r, g, b){F.END} used with {F.BOLD}rgb(){F.END} or {F.BOLD}grad(){F.END}\n"
            f"  {rgb(C.gray_dark)}F {F.END}= Formats {rgb(C.gray_dark)}→{F.END} ANSI escape codes for {F.BOLD}bold{F.END}, {F.ITALIC}italic{F.END}, {F.UNDERLINE}underline{F.END}, etc.\n"
            f"  {rgb(C.gray_dark)}tip     {F.END}combine them: {rgb(C.neon_pink)+F.BOLD}rgb(C.neon_pink) + F.BOLD{F.END}\n"
            f"\n"
        )
def alternate(text, colors):
    result = []
    color_len = len(colors)
    for i in range(len(text)):
        r = colors[i%color_len][0]
        g = colors[i%color_len][1]
        b = colors[i%color_len][2]
        
        result.append(f"\x1b[38;2;{r};{g};{b}m{text[i]}")
    
    return "".join(result) + "\x1b[0m"



def credit():
    print(
        f"{UP(1)+CLEAR_LINE()+rgb(C.green_dark)}Loaded Module:{F.END} Guli's {F.BOLD+alternate("ANSI", [C.cyan_light, C.blue_light, C.red_light, C.yellow_light])} decoder."
        )
credit()

if __name__ == "__main__":
    info_colors()