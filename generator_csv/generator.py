import numpy as np
import pandas as pd
 
n_rows = 1000000
n_cols = 10
 
df = pd.DataFrame(np.random.randint(0, 100, size=(n_rows, n_cols)), columns=['col%d' % i for i in range(n_cols)])
df.head()
 
file_path = 'file.csv'
df.to_csv(file_path, index=False)
print('Всё, создано')