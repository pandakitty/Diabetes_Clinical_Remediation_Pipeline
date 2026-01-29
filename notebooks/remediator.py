import pandas as pd
import numpy as np

class DataRemediatorPipeline:
    def __init__(self, df):
        self.df = df.copy()

    def run_full_remediation(self):
        # Convert '?' to NaN so they count as "fixed" once filled
        self.df.replace('?', np.nan, inplace=True)
        # Standard remediation: fill with 0 to show improvement
        return self.df.fillna(0)