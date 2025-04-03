def rep_char(c,n):
    print(c*n)

def draw_line_string(msg1,msg2):
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-',nstr)
    print(f'{msg1}')
    print(f'{msg2}')
    rep_char('-',nstr)

msg1=input('input his/her name:')
msg1=f'Hello {msg1}, '
msg2=f'Welcome to Seoul.'
draw_line_string(msg1,msg2)
