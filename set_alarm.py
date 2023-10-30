def set_alarm(employed, vacation):
    if employed and vacation: return False
    if employed and not vacation: return True
    if not employed and vacation: return False
    if not employed and not vacation: return False


print(set_alarm(True, True))


