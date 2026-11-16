from utils.fetch_bcw_dataset import fetch_local_bcw
from scikit_roughsets.roughsets import RoughSetsReducer
from scikit_roughsets.rs_reduction import RoughSetsSelector
import numpy, time


def main():
	bcw_df = fetch_local_bcw()
	# print(bcw_df)
	# print(bcw_df.columns)
	# print(bcw_df.dtypes)
	# print(bcw_df.isna().any(), end="\n\n")

	reducer = RoughSetsReducer()
	X = bcw_df[bcw_df.columns[0:-1]].to_numpy()
	y = numpy.array([bcw_df[bcw_df.columns[-1]]]).T
	
	# start = time.time()
	# bcw_reduced_B_line_num = reducer.reduce(X, y).astype("int64")
	# reduction_time = time.time()
	# bcw_core_line_num = reducer.core(X, y)
	# end = time.time()

	# bcw_reduced_B_line_num = bcw_reduced_B_line_num.astype("int64")
	# bcw_core_line_num = bcw_core_line_num.astype("int64")
	# bcw_reduced_B = bcw_df.columns[bcw_reduced_B_line_num-1]
	# bcw_core = bcw_df.columns[bcw_core_line_num-1]

	# print(f"One of reduction of condition attributes set:\n{set(bcw_reduced_B)}")
	# print(f"The core of condition attributes set:\n{set(bcw_core)}\n")
	# print(f"Total time comsumption:")
	# print(f"Reduction: {reduction_time - start}")
	# print(f"Core: {end-reduction_time}\n")

	selector = RoughSetsSelector()
	selector.fit(X, y)
	print(selector.mask_)
	print(list(bcw_df.columns[0:-1][selector.mask_]))


if __name__ == "__main__":
	main()
