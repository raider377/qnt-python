import qnt.data as qndata
import qnt.stats as qnstats
import qnt.xr_talib as qnxrtalib

import xarray as xr
import pandas as pd
from qnt.stepper import test_strategy

import xarray.ufuncs as xrf

data = qndata.load_cryptocurrency_data(min_date="2014-01-01", max_date=None, dims=("time", "field", "asset"),
                                       forward_order=True)

print(qnstats.calc_avg_points_per_year(data))

# exit(0)

print(data.sel(asset='BTC', field='close').to_pandas())

output = data.sel(field='close')
output = output / output
output = qndata.sort_and_crop_output(output)

output *= 1

print(output.to_pandas())
print(output[0, 0].item())

print(qnstats.calc_slippage(data).to_pandas()[13:])

stat2 = qnstats.calc_stat(data, output, slippage_factor=0.05)
# ss = qnstats.calc_stat(data, output, max_periods=252 * 3, slippage_factor=0.05, per_asset=True)

print(stat2.sel(field=[qnstats.stf.MEAN_RETURN, qnstats.stf.SHARPE_RATIO, qnstats.stf.EQUITY]).to_pandas())

qndata.write_output(output)