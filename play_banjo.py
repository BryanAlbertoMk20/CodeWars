def are_you_playing_banjo(name):
    if name[0] == 'r'.lower() or name[0] == 'r'.upper():
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


print(are_you_playing_banjo("Ronald"))
print(are_you_playing_banjo("James"))
print(are_you_playing_banjo("rice"))
print(are_you_playing_banjo("tom"))
