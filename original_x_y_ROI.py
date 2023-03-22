import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import ast
df1 = pd.read_csv('/Users/x/x/x/x.csv')
df1 = df1.drop(df1.index[np.where(df1.index > 100)])
df = df1.iloc[::1, :]
# convert there the ROI coordinates to list of dictionaries
roi_coords = []
for i in range(len(df)):
    coords_str = df['ROI_coordinates'][i]
    coords_dict = ast.literal_eval(coords_str)
    xs_nested = coords_dict['xs']
    xs = []
    for sublist in xs_nested:
        xs.extend(sublist)
    xs = [float(x) for x in xs]
    ys_nested = coords_dict['ys']
    ys = []
    for sublist in ys_nested:
        ys.extend(sublist)
    ys = [float(y) for y in ys]
    roi_coords.append({'xs': xs, 'ys': ys})
#plot
fig, ax = plt.subplots(figsize=(8, 6))
for i in range(len(roi_coords)):
    xs = roi_coords[i]['xs']
    ys = roi_coords[i]['ys']
    ax.plot(xs + [xs[0]], ys + [ys[0]], label=f'Frame {i+1}')
#ax.legend()
plt.savefig('Pattern.png')
plt.show()