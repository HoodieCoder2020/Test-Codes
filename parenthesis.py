def parenthesis(s):
    while "()" in s or "{}" in s or '[]' in s:
        s = s.replace("()", "").replace('{}', "").replace('[]', "")
    if s == '':
        print(1)
    else:
        print(0)

