import math
import ANSI
import Goosefull as goose

print("Loading module: G_anicurves..")

# Definieer de tekst en RGB-kleuren
blue = (0, 0, 255)
green = (0, 255, 0)


def _bounce_out(t):
    n, d = 7.5625, 2.75
    if t < 1/d:       return n * t * t
    elif t < 2/d:     t -= 1.5/d;  return n*t*t + 0.75
    elif t < 2.5/d:   t -= 2.25/d; return n*t*t + 0.9375
    else:             t -= 2.625/d; return n*t*t + 0.984375

def _ease_out(f, t):    return 1 - f(1 - t)
def _ease_in_out(f, t): return f(2*t) / 2 if t < 0.5 else 1 - f(2 - 2*t) / 2

_in = {
    "Sine":    lambda t: 1 - math.cos((t * math.pi) / 2),
    "Quad":    lambda t: t ** 2,
    "Cubic":   lambda t: t ** 3,
    "Quart":   lambda t: t ** 4,
    "Quint":   lambda t: t ** 5,
    "Expo":    lambda t: 0 if t == 0 else 2 ** (10*t - 10),
    "Circ":    lambda t: 1 - math.sqrt(1 - t**2),
    "Back":    lambda t: 2.70158*t**3 - 1.70158*t**2,
    "Elastic": lambda t: 0 if t==0 else 1 if t==1 else -(2**(10*t-10)) * math.sin((t*10-10.75)*(2*math.pi)/3),
    "Bounce":  lambda t: 1 - _bounce_out(1 - t),
}

_easings = {}
for name, f in _in.items():
    _easings[f"easeIn{name}"]    = f
    _easings[f"easeOut{name}"]   = lambda t, f=f: _ease_out(f, t)
    _easings[f"easeInOut{name}"] = lambda t, f=f: _ease_in_out(f, t)

copya = _easings.copy()
for k,v in copya.items():
    _easings[k.lower()] = v

def a_curve(x, ease="easeInSine", start=0, end=1, strength=1):
    ease = ease.lower()
    x = (x - start) / (end - start)
    x = max(0.0, min(1.0, x))
    t = _easings[ease](x)
    t = t ** (1 / strength) if t >= 0 else -((-t) ** (1 / strength))
    return start + (end - start) * t

def lerp(progress, start, end, progress_min=0, progress_max=1):
    t = (progress - progress_min) / (progress_max - progress_min)
    return start + (end - start) * progress

def curve_info():
    goose.print_set(_in, True)


def credit():
    print(
        f"{ANSI.UP(1)+ANSI.CLEAR_LINE()+ANSI.C.GREEN}Loaded Module:{ANSI.C.END} Guli's {ANSI.C.END}", end=""
        )
    print(ANSI.grad("AnimationCurves", [blue, green])+ANSI.C.END+".")
credit()

