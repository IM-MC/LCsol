def lengthLongestPath(input):
    """
    :type input: str
    :rtype: int
    """

    map = {0:0}
    depth = 0
    maxlength = 0

    for string in input.splitlines():
        name = string.lstrip("\t")
        depth = len(string) - len(name)

        if "." in string:
            maxlength = max(map[depth] + len(name), maxlength)
        else:
            map[depth + 1] = map[depth] + len(name) + 1

    return maxlength

print(lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
