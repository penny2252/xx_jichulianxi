import os
os.chdir('./test')
for name in os.listdir():
    new_name='xinjian_'+name
    os.rename(name,new_name)

