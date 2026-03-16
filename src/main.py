import miku
# DEBUG FILE, WILL UPDATE TO RUN VIA FILE LATER
while True:
    text = input('miku > ')
    result, error  = miku.run('placeholder', text)

    if error: print(error.as_string())
    else: print(result)
