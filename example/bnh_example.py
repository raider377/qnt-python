import qnt.data as qndata
import qnt.stats as qnstats
import qnt.forward_looking as qnfl
import time

data = qndata.load_data(
    min_date="2015-01-01", max_date="2018-01-01",
    forward_order=True,
                        dims=("time", "field", "asset"))

print(qnstats.calc_avg_points_per_year(data))

output = data.sel(field=qndata.f.IS_LIQUID)
output = qndata.sort_and_crop_output(output)

output *= 1

print(output.to_pandas())
print(output[0, 0].item())

print(qnstats.calc_slippage(data).to_pandas()[13:])

stat2 = qnstats.calc_stat(data, output, slippage_factor=0.05, per_asset=True)
# ss = qnstats.calc_stat(data, output, max_periods=252 * 3, slippage_factor=0.05, per_asset=True)

print(stat2.sel(field=[  # qnstats.stf.RELATIVE_RETURN,
    qnstats.stf.MEAN_RETURN,
    # qnstats.stf.VOLATILITY,
    qnstats.stf.SHARPE_RATIO,
    # qnstats.stf.EQUITY,
    # qnstats.stf.MAX_DRAWDOWN
    qnstats.stf.AVG_HOLDINGTIME
]).isel(asset=0).to_pandas())

qndata.write_output(output)
