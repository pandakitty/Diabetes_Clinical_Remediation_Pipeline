import pandas as pd
import numpy as np

class ClinicalAuditor:
    """Handles the initial clinical data audit and DQI calculation."""
    
    def __init__(self, df):
        self.df = df

    def calculate_baseline_dqi(self):
        """Quantifies null density, specifically targeting '?' encodings."""
        # Replace clinical '?' with NaN for calculation
        temp_df = self.df.replace('?', np.nan)
        null_counts = temp_df.isnull().sum()
        total_cells = np.prod(temp_df.shape)
        null_density = (null_counts.sum() / total_cells) * 100
        
        # DQI is a composite score (100 - null density for this example)
        dqi_score = 100 - null_density
        print(f"Baseline Data Quality Index (DQI): {dqi_score:.2f}%")
        return dqi_score
