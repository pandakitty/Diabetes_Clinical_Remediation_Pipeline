import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# ==========================================
# MODULE 1: AUDITOR (Christian - Data Wrangler)
# ==========================================
class ClinicalAuditor:
    """Handles the initial clinical data audit and DQI calculation."""
    def __init__(self, df):
        self.df = df

    def calculate_baseline_dqi(self):
        """Quantifies null density, specifically targeting '?' encodings."""
        temp_df = self.df.replace('?', np.nan)
        null_counts = temp_df.isnull().sum()
        total_cells = np.prod(temp_df.shape)
        null_density = (null_counts.sum() / total_cells) * 100
        dqi_score = 100 - null_density
        print(f"Audit Complete: Baseline DQI is {dqi_score:.2f}%")
        return dqi_score

# ==========================================
# MODULE 2: REMEDIATOR (Kirsten - Data Scientist)
# ==========================================
class DataRemediator:
    """Executes MICE/KNN imputation and medical code normalization."""
    def normalize_icd9(self, df, column):
        """Standardizes diagnosis codes using Regex."""
        df[column] = df[column].apply(lambda x: re.sub(r'[^0-9.]', '', str(x)))
        return df

    def apply_mice_imputation(self, df):
        """Implements MICE logic to reduce statistical bias."""
        # Selecting numeric columns for imputation example
        numeric_df = df.select_dtypes(include=[np.number])
        imputer = IterativeImputer(max_iter=10, random_state=0)
        imputed_data = imputer.fit_transform(numeric_df)
        return pd.DataFrame(imputed_data, columns=numeric_df.columns)

# ==========================================
# MODULE 3: VISUALIZER (Mugtaba - Data Visualizer)
# ==========================================
class QualityVisualizer:
    """Validates remediation via distribution analysis."""
    def plot_remediation_delta(self, before_df, after_df, column):
        """Generates KDE plots to ensure no statistical skew was introduced."""
        plt.figure(figsize=(10, 6))
        sns.kdeplot(before_df[column].replace('?', np.nan).dropna(), label='Before (Raw)', fill=True)
        sns.kdeplot(after_df[column], label='After (MICE)', fill=True)
        plt.title(f'RQ3: Distribution Validation for {column}')
        plt.legend()
        plt.savefig(f'plots/{column}_validation.png')
        print(f"Visual Validation saved to plots/{column}_validation.png")
        plt.show()

# ==========================================
# MAIN ORCHESTRATION PIPELINE
# ==========================================
if __name__ == "__main__":
    # 1. Load Data (Assumes file is in the data/ folder)
    try:
        raw_data = pd.read_csv('data/diabetic_data.csv')
        
        # 2. Run Audit
        auditor = ClinicalAuditor(raw_data)
        baseline = auditor.calculate_baseline_dqi()

        # 3. Run Remediation
        remediator = DataRemediator()
        # Cleaning diagnosis codes
        remediated_data = remediator.normalize_icd9(raw_data, 'diag_1')
        # Running MICE on numerical columns
        imputed_df = remediator.apply_mice_imputation(raw_data)

        # 4. Run Visualization
        visualizer = QualityVisualizer()
        visualizer.plot_remediation_delta(raw_data, imputed_df, 'num_lab_procedures')

    except FileNotFoundError:
        print("Error: Please ensure 'diabetic_data.csv' is placed in the 'data/' folder.")
