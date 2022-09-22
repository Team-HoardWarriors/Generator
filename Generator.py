import random
import sys
import os
print("""
\033[36m=================================================================
\033[36m=                \033[37mCellphone Number Generator                     \033[36m=
\033[36m=================================================================
\033[36m=                                                               \033[36m=
\033[36m=   \033[32m██████╗██████╗                ██████╗ ███████╗███╗   ██╗    \033[36m=
\033[36m=  \033[32m██╔════╝██╔══██╗              ██╔════╝ ██╔════╝████╗  ██║    \033[36m=
\033[36m=  \033[32m██║     ██████╔╝    █████╗    ██║  ███╗█████╗  ██╔██╗ ██║    \033[36m=
\033[36m=  \033[32m██║     ██╔═══╝     ╚════╝    ██║   ██║██╔══╝  ██║╚██╗██║    \033[36m=
\033[36m=  \033[32m╚██████╗██║                   ╚██████╔╝███████╗██║ ╚████║    \033[36m=
\033[36m=   \033[32m╚═════╝╚═╝                    ╚═════╝ ╚══════╝╚═╝  ╚═══╝    \033[36m=
\033[36m=================================================================
\033[36m=                \033[37mFor Educational Purpose Only                   \033[36m=
\033[36m=================================================================                                                       
""")
def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)

    last = (str(random.randint(1, 999)).zfill(3))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 999)).zfill(3))

    return '+639{}{}{}'.format(first, second, last)

n = int(input("\033[32mEnter Value of number: "))
for i in range(0, n):
    print(random_phone_num_generator())
    file = open('Generated.txt','a')
    file.write('\n'+random_phone_num_generator())
file.close()