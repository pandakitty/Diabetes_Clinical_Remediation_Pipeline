# remediator.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from remediator import DataRemediator

class DataRemediatorPipeline:
    """Remediation pipeline for clinical dataset."""

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.final_df = None
        self.numeric_cols = None
        self.id_cols = ['encounter_id', 'patient_nbr']
        self.icd9_cols = ['diag_1', 'diag_2', 'diag_3']

    def scale_and_impute(self):
        remediator = DataRemediator()
        self.numeric_cols = [col for col in self.df.select_dtypes(include=[np.number]).columns
                             if col not in self.id_cols]
        scaler = StandardScaler()
        scaled_numeric = pd.DataFrame(
            scaler.fit_transform(self.df[self.numeric_cols]),
            columns=self.numeric_cols,
            index=self.df.index
        )
        imputed_scaled_numeric = remediator.apply_mice_imputation(scaled_numeric)
        imputed_numeric_df = pd.DataFrame(
            scaler.inverse_transform(imputed_scaled_numeric),
            columns=self.numeric_cols,
            index=self.df.index
        )
        self.df[self.numeric_cols] = imputed_numeric_df
        return self

    def normalize_icd9_codes(self):
        remediator = DataRemediator()
        for col in self.icd9_cols:
            self.df = remediator.normalize_icd9(self.df, col)
        self.final_df = self.df.copy()
        return self

    def create_target(self):
        """Map readmitted and create <30 day readmission target."""
        self.final_df['readmitted'] = self.final_df['readmitted'].map({
            'NO': 0, 'YES': 1, '>30': 1, '<30': 1
        })
        self.final_df['readmit_30days'] = (self.final_df['readmitted'] == 1).astype(int)
        return self

    def run_full_remediation(self):
        self.scale_and_impute().normalize_icd9_codes().create_target()
        # Return a dict so the next person can access metadata if needed
        return {
            'final_df': self.final_df,
            'numeric_cols': self.numeric_cols,
            'id_cols': self.id_cols,
            'icd9_cols': self.icd9_cols
        }