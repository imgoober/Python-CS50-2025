import sys
import PIL.Image
import PIL.ImageOps
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1 = sys.argv[1].lower()
    file2 = sys.argv[2].lower()
    ext1 = os.path.splitext(file1)[1]
    ext2 = os.path.splitext(file2)[1]

    file_types = [".jpg", ".jpeg", ".png"]
    if ext1 not in file_types:
        sys.exit("Invalid input")
    if ext2 not in file_types:
        sys.exit("Invalid output")
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    try:
        shirt = PIL.Image.open("shirt.png")
        result = PIL.Image.open(sys.argv[1])
        result = PIL.ImageOps.fit(result, shirt.size)
        result.paste(shirt, shirt)
        result.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
