# auditor.py 
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

class DataAuditor:
    """Data quality auditor for diabetes readmission dataset with clinical profiling and DQI."""
    
    def __init__(self, path: str):
        self.path = path
        self.raw_df = None
        self.df = None
        self.raw_duplicates = 0
        self.profiling_report = {}
        self.dqi_components = {}
        self.dqi_score = None

        # Lookup mappings
        self.admission_type_map = {
            1: 'Emergency', 2: 'Urgent', 3: 'Elective', 4: 'Newborn',
            5: 'Not Available', 6: 'NULL', 7: 'Trauma Center', 8: 'Not Mapped'
        }

        self.discharge_map = {
            1: 'Discharged to home',
            2: 'Discharged/transferred to another short term hospital',
            3: 'Discharged/transferred to SNF',
            4: 'Discharged/transferred to ICF',
            5: 'Discharged/transferred to another type of inpatient care institution',
            6: 'Discharged/transferred to home with home health service',
            7: 'Left AMA',
            8: 'Discharged/transferred to home under care of Home IV provider',
            9: 'Admitted as an inpatient to this hospital',
            10: 'Neonate discharged to another hospital for neonatal aftercare',
            11: 'Expired',
            12: 'Still patient or expected to return for outpatient services',
            13: 'Hospice / home',
            14: 'Hospice / medical facility',
            15: 'Discharged/transferred within this institution to Medicare approved swing bed',
            16: 'Discharged/transferred/referred another institution for outpatient services',
            17: 'Discharged/transferred/referred to this institution for outpatient services',
            18: 'NULL',
            19: 'Expired at home. Medicaid only, hospice.',
            20: 'Expired in a medical facility. Medicaid only, hospice.',
            21: 'Expired, place unknown. Medicaid only, hospice.',
            22: 'Discharged/transferred to another rehab fac including rehab units of a hospital.',
            23: 'Discharged/transferred to a long term care hospital.',
            24: 'Discharged/transferred to a nursing facility certified under Medicaid but not certified under Medicare.',
            25: 'Not Mapped', 
            26: 'Unknown/Invalid',
            27: 'Discharged/transferred to a federal health care facility.',
            28: 'Discharged/transferred/referred to a psychiatric hospital of psychiatric distinct part unit of a hospital',
            29: 'Discharged/transferred to a Critical Access Hospital (CAH).',
            30: 'Discharged/transferred to another Type of Health Care Institution not Defined Elsewhere'
        }

        self.admission_source_map = {
            1: 'Physician Referral', 
            2: 'Clinic Referral', 
            3: 'HMO Referral',
            4: 'Transfer from a hospital',
            5: 'Transfer from a Skilled Nursing Facility (SNF)',
            6: 'Transfer from another health care facility',
            7: 'Emergency Room',
            8: 'Court/Law Enforcement', 
            9: 'Not Available',
            10: 'Transfer from critial access hospital',
            11: 'Normal Delivery',
            12: 'Premature Delivery',
            13: 'Sick Baby',
            14: 'Extramural Birth',
            15: 'Not Available', 
            17: 'NULL',
            18: 'Transfer From Another Home Health Agency',
            19: 'Readmission to Same Home Health Agency',
            20: 'Not Mapped',
            21: 'Unknown/Invalid',
            22: 'Transfer from hospital inpt/same fac reslt in a sep claim',
            23: 'Born inside this hospital',
            24: 'Born outside this hospital',
            25: 'Transfer from Ambulatory Surgery Center',
            26: 'Transfer from Hospice'
        }

    def load_data(self):
        """Load CSV and track raw duplicate count."""
        self.raw_df = pd.read_csv(self.path)
        self.raw_duplicates = self.raw_df.duplicated().sum()
        self.df = self.raw_df.copy()
        return self

    def apply_basic_cleaning(self):
        """Convert ?→NaN, unknowns→NaN, create descriptions, remove duplicates."""
        df = self.df

        # Ensure IDs are numeric
        id_cols = ['admission_type_id', 'discharge_disposition_id', 'admission_source_id']
        for col in id_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        # Create descriptive columns (Unknown for unmapped IDs)
        df['admission_type_desc'] = df['admission_type_id'].map(self.admission_type_map).fillna('Unknown')
        df['discharge_disposition_desc'] = df['discharge_disposition_id'].map(self.discharge_map).fillna('Unknown')
        df['admission_source_desc'] = df['admission_source_id'].map(self.admission_source_map).fillna('Unknown')

        # Convert '?' to NaN across entire dataframe
        df = df.replace('?', np.nan)

        # Convert all "unknown" variants to NaN
        unknown_variants = ['Unknown', 'unknown', 'UNKNOWN', 'Not Available', 'NULL', 'Not Mapped', 'Unknown/Invalid']
        df = df.replace(unknown_variants, np.nan) 

        # Remove brackets for weight and age
        for col in ['weight', 'age']:
            if col in df.columns:
                df[col] = df[col].astype(str).str.replace('[', '', regex=False).str.replace(')', '', regex=False)

        # Remove duplicate rows
        initial_rows = len(df)
        df = df.drop_duplicates()
        print(f"Removed {initial_rows - len(df)} duplicate rows")

        self.df = df
        return self

    def clinical_profile(self):
        """Generate baseline clinical demographics, utilization, and outcomes."""
        df = self.df
        profile = {}

        # Demographics
        profile['n_rows'] = len(df)
        profile['n_patients'] = df['patient_nbr'].nunique()
        profile['gender_distribution'] = df['gender'].value_counts(dropna=False).to_dict()
        profile['race_distribution'] = df['race'].value_counts(dropna=False).to_dict()
        profile['age_groups'] = df['age'].value_counts(dropna=False).to_dict()

        # Utilization
        profile['mean_time_in_hospital'] = float(df['time_in_hospital'].mean())
        profile['num_admissions_by_type'] = df['admission_type_desc'].value_counts().to_dict()
        profile['num_admissions_by_source'] = df['admission_source_desc'].value_counts().to_dict()
        profile['num_admissions_by_discharge'] = df['discharge_disposition_desc'].value_counts().to_dict()

        # Outcomes/readmission
        profile['readmitted_distribution'] = df['readmitted'].value_counts().to_dict()

        self.profiling_report = profile
        return profile

    def compute_dqi(self):
        """Compute Baseline DQI: completeness + consistency + duplicates."""
        df = self.df

        # Completeness: average non-null ratio
        completeness_by_col = 1.0 - (df.isna().mean())
        completeness_score = float(completeness_by_col.mean())

        # Coded-field consistency
        coded_scores = []
        allowed_gender = {'Male', 'Female'}
        if 'gender' in df.columns:
            coded_scores.append((df['gender'].isin(allowed_gender)).mean())

        allowed_readmitted = {'NO', '<30', '>30'}
        if 'readmitted' in df.columns:
            coded_scores.append((df['readmitted'].isin(allowed_readmitted)).mean())

        for col in ['admission_type_id', 'discharge_disposition_id', 'admission_source_id', 'time_in_hospital']:
            if col in df.columns:
                coded_scores.append((df[col] > 0).mean())

        coded_consistency_score = float(np.mean(coded_scores)) if coded_scores else 1.0

        # Duplicates penalty
        duplicate_ratio = self.raw_duplicates / max(len(self.raw_df), 1)
        duplicates_score = 1.0 - duplicate_ratio

        # Aggregate DQI
        self.dqi_components = {
            'completeness': completeness_score,
            'coded_consistency': coded_consistency_score,
            'duplicates': duplicates_score
        }
        self.dqi_score = float(np.mean(list(self.dqi_components.values())))
        return self.dqi_score

    def run_full_audit(self, verbose: bool = True):
        """Complete pipeline: load → clean → profile → DQI."""
        self.load_data()
        self.apply_basic_cleaning()
        profile = self.clinical_profile()
        dqi = self.compute_dqi()

        if verbose:
            print("Rows (cleaned):", len(self.df))
            print("Unique patients:", profile['n_patients'])
            print("Baseline DQI:", round(dqi, 3))
            print("\nDQI Components:", {k: round(v, 3) for k, v in self.dqi_components.items()})
        
        return {
            'profile': profile,
            'dqi_score': dqi,
            'dqi_components': self.dqi_components,
            'cleaned_data': self.df
        }
