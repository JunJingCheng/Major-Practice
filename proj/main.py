from pytools.logger import get_logger
logger = get_logger(__name__)
import traceback
from utils.fetch_bcw_dataset import fetch_local_bcw


def main():
	bcw_df = fetch_local_bcw()
	print(bcw_df)
	print(bcw_df.columns)


if __name__ == "__main__":
	main()
