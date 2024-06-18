import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    print('mac')
    rc('font', family = 'Arial Unicode MS')

elif platform.system() =='Windows':
    print('windows')
    rc('font', family = 'Malgun Gothic' )

else:
    print('Unknown')

plt.rcParams['axes.unicode_minus'] = False

