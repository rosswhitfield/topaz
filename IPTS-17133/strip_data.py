import h5py
import numpy as np

in_filename = '/SNS/TOPAZ/IPTS-17133/shared/Sr_100K/Visualization/3D_vol_full/T90K_combined_symm-oP.nxs'
out_filename = 'Sr14Cu24O41.h5'

with h5py.File(in_filename, "r") as f:
    path = 'MDHistoWorkspace/data/'

    signal = f[path+'signal']
    signal_data = np.array(signal)

    axes = signal.attrs['axes'].decode().split(":")

    dims_list = []
    coords_list = []
    name_list = []
    unit_list = []
    for a in axes:
        dims_list.append(a)
        axis = f[path+a]
        coords_list.append(np.array(axis))
        name_list.append(axis.attrs['long_name'])
        unit_list.append(axis.attrs['units'])

with h5py.File(out_filename, "w") as f:
    entry = f.create_group('entry1')
    entry.attrs['NX_class'] = 'NXentry'
    data = entry.create_group("data")
    data.attrs['NX_class'] = 'NXdata'

    signal = data.create_dataset('signal', data=signal_data, compression='gzip')
    signal.attrs['axes'] = str(':'.join(dims_list))
    signal.attrs['signal'] = 1

    for n in range(len(dims_list)):
        d = data.create_dataset(dims_list[n], data=coords_list[n])
        d.attrs['frame'] = 'HKL'
        d.attrs['long_name'] = name_list[n]
        d.attrs['units'] = unit_list[n]
