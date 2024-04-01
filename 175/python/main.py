import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(person, address, on=['personId'], how='left').drop(columns=['personId', 'addressId'])

def main():
    person_df =  pd.DataFrame([{'personId': 1, 'lastName': 'Wang', 'firstName': 'Allen'},
                               {'personId': 2, 'lastName': 'Alice', 'firstName': 'Bob'}])
    address_df = pd.DataFrame([{'addressId': 1, 'personId': 2, 'city': 'New York City', 'state': 'New York'},
                               {'addressId': 2, 'personId': 3, 'city': 'Leetcode', 'state': 'California'}])
    desired_df = pd.DataFrame([{'firstName': 'Allen', 'lastName': 'Wang', 'city': np.nan, 'state': np.nan},
                               {'firstName': 'Bob', 'lastName': 'Alice', 'city': 'New York City', 'state': 'New York'}])
    result_df = combine_two_tables(person_df, address_df)
    assert_frame_equal(result_df, desired_df, check_like=True)

if __name__ == '__main__':
    main()