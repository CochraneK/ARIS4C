# join_and_run.py - concat _n1+_n2 -> data/code/s3a_numerators.py then exec (cmd arg-slash workaround)
src = open('_n1.py', encoding='utf-8').read() + open('_n2.py', encoding='utf-8').read()
open('data/code/s3a_numerators.py', 'w', encoding='utf-8', newline='\n').write(src)
import os
os.remove('_n1.py'); os.remove('_n2.py')
exec(compile(src, 'data/code/s3a_numerators.py', 'exec'), {'__file__': 'data/code/s3a_numerators.py'})
