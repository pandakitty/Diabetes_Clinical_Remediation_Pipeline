import pandas as pd
import numpy as np

class DataAuditor:
    def calculate_dqi(self, df):
        # We ensure we count '?' as nulls for the audit
        temp_df = df.replace('?', np.nan)
        completeness = 1 - (temp_df.isnull().sum().sum() / temp_df.size)
        return round(completeness * 100, 2)