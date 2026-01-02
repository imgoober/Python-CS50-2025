import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link_format = r'<iframe[^>]*src="(https?://(?:www\.)?youtube\.com/embed/([^"]+))"'
    if match := re.search(link_format, s):
        video_id = match.group(2)
        return f"https://youtu.be/{video_id}"


if __name__ == "__main__":
    main()
