def full_justify(words, max_width):
    """
    Justifies text so that each line has exactly max_width characters.

    Args:
        words (list): List of strings.
        max_width (int): Maximum width of a line.

    Returns:
        list: List of justified lines.
    """
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > max_width:
            for i in range(max_width - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(max_width)]


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    width = 16
    for line in full_justify(words, width):
        print(f"'{line}'")
