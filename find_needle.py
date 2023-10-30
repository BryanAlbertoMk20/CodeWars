def find_needle(haystack):
    if "needle" in haystack:
        index = haystack.index("needle")
        return f"found the neeldle at position {index}"
    else:
        return "needle is not in the haystack."


test = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]