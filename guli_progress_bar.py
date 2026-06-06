import ANSI
filename = __file__.split("\\")[-1] 
print(f"(Loading module: {filename}..")

# this is just cool

def progress_bar(progress, max_progress, on="█", off="|", color_on=ANSI.C.GREEN, color_off=ANSI.C.RED, bar_width=5, bar_length=100, form=1, stick_out=0, name=""):
    bar_width = max(3, bar_width)
    print(ANSI.UP(bar_width + 2 + (1 if len(name) else 0)), end="")
    padding = (bar_length + stick_out - len(name)) // 2
    if len(name):
        print(color_on +"=" * (padding+(len(name)%2==0)) + name + "=" * padding + ANSI.C.END)

    on = on[0]
    off = off[0]
    if form==1:
        bar_length += stick_out
        percent = -(-progress*bar_length // max_progress)
        print(color_on +"╔" + "═"*(bar_length-stick_out-1) + "╗")
        print(color_on +"║"+on*min(percent, bar_length-stick_out-1) + color_off + off*(bar_length-percent-stick_out-1)+color_on+f"╚{"═"*stick_out}╗")

        for i in range(bar_width-2):
            print(color_on+"║" + on*percent +color_off + off*(bar_length-percent)+color_on+"║")

        print(color_on +"║"+on*min(percent, bar_length-stick_out-1) + color_off + off*(bar_length-percent-stick_out-1)  + color_on +  f"╔{"═"*stick_out}╝")
        print(color_on +"╚" + "═"*(bar_length-stick_out-1) + f"╝ {progress}/{max_progress}"+ANSI.C.END)
    if form==0:
        percent = -(-progress*bar_length // max_progress)
        if percent == bar_length:
            color_off = color_on
            off = on # wouw
        print(color_on+"╔" + "═"*bar_length + "╗")
        for i in range(bar_width):
            print(color_on+"║"+on*percent + color_off + off*(bar_length-percent)+ color_on +"║")
        print(color_on+"╚" + "═"*bar_length + f"╝ {progress}/{max_progress}", color_off)

def INFO():
    print(
        f"{ANSI.C.FAINT}{'='*80}{ANSI.C.END}\n"
        f"{ANSI.C.BOLD}Welcome to {ANSI.C.GREEN}PROGRESS{ANSI.C.RED}BAR{ANSI.C.END}\n\n"
        f"{ANSI.C.BOLD}Usage:{ANSI.C.END}\n"
        f"  {ANSI.C.BLUE}progress_bar(progress, max_progress, [optional stuff]){ANSI.C.END}\n\n"
        f"{ANSI.C.BOLD}Optional stuff:{ANSI.C.END}\n"
        f"  on          Character for filled portion    (default: '█')\n"
        f"  off         Character for empty portion     (default: '|')\n"
        f"  color_on    Color for filled portion        (default: GREEN)\n"
        f"  color_off   Color for empty portion         (default: RED)\n"
        f"  bar_width   Height of the bar               (default: 5, min: 3)\n"
        f"  bar_length  Width of the bar                (default: 100)\n"
        f"  form        Shape: 0=flat, 1=battery        (default: 1)\n"
        f"  stick_out   Battery end size                (default: 0)\n"
        f"  name        Label shown above the bar       (default: '')\n\n"
        f"{ANSI.C.RED}NOTE: Print empty lines before calling progress_bar() - at least (bar_width + 2).{ANSI.C.END}\n\n"
        f"Made by {ANSI.C.BOLD}{ANSI.C.UNDERLINE}GULI GULI{ANSI.C.END}\n"
        f"{ANSI.C.FAINT}{'='*80}{ANSI.C.END}\n"
    )




def main():
    bigness = int(input("bigness: "))
    width = 6  # AT LEAST 3
    print("\n"*(width+2))
    for i in range(bigness+1):
        progress_bar(i, bigness, "█", "|", bar_width=width, bar_length=50, stick_out=1)
        #time.sleep(0.1)
    print("\n")



def credit():
    print(
        f"{ANSI.UP(1)+ANSI.CLEAR_LINE()+ANSI.C.GREEN}Loaded Module:{ANSI.C.END} Guli's {ANSI.C.BOLD+ANSI.C.GREEN}PROGRESS{ANSI.C.RED}BAR{ANSI.C.END}."
    )
credit()

if __name__ == "__main__":
    main()
    INFO()



