def words_sorting(*args, a=0, s=None):
    if s is None:
        s = {}
    for arg in args:
        for ch in arg:
            a += ord(ch)
        s[arg] = int(a)
        a = 0
    new = dict(sorted(s.items(), key=lambda item: (-item[1], item[0])))
    return "\n".join([f"{''.join(key)} - {''.join(str(value))}" for key, value in new.items()])


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
