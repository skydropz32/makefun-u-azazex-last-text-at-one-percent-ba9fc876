"""Last Text at One Percent: the final text a dying phone sends."""

LINE = "I read every text you deleted. Your secrets die with me. The charger gets nothing."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space, and exactly one line.
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry must be 1-200 characters")
    if not LINE.strip() or "\n" in LINE:
        raise ValueError("entry must be one non-blank line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
