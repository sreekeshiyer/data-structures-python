string = 'HelloWorld'


def reverse(s: str) -> str:
    return s if len(s) == 0 else reverse(s[1:]) + s[0]


print(reverse(string))
