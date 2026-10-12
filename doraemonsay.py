import sys
import textwrap

DORAEMON = r"""
   \
    \
      .-~~~~~~~~~-.
     /  .-.   .-.  \
    |  ( o ) ( o )  |
    | =--  (_)  --= |
    |   \_______/   |
     \             /
      `-.__(o)__.-'
        /  Doraemon  \
"""


def make_bubble(text, width=40):
    lines = textwrap.wrap(text, width) or [""]
    w = max(len(line) for line in lines)

    top = " " + "_" * (w + 2)
    bottom = " " + "-" * (w + 2)

    if len(lines) == 1:
        body = [f"< {lines[0].ljust(w)} >"]
    else:
        body = []
        for i, line in enumerate(lines):
            if i == 0:
                left, right = "/", "\\"
            elif i == len(lines) - 1:
                left, right = "\\", "/"
            else:
                left, right = "|", "|"
            body.append(f"{left} {line.ljust(w)} {right}")

    return "\n".join([top, *body, bottom])


def doraemonsay(text):
    print(make_bubble(text))
    print(DORAEMON)


def main():
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
    elif not sys.stdin.isatty():
        message = sys.stdin.read().strip()  # supports: fortune | doraemonsay
    else:
        message = "Doraemon desu!"
    doraemonsay(message)


if __name__ == "__main__":
    main()