import sys

def main():

    if len(sys.argv) > 1:
        print("none")
        return

    i = 0
    while i <= 10:
        j = 0
        line = f"Table de {i}:"
        while j <= 10:
            line += f" {i * j}"
            j += 1
        print(line)
        i += 1

if __name__ == "__main__":
    main()