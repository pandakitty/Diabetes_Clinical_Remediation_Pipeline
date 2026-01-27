# Data Quality Dimensions & DQI Targets

This pipeline targets a **25% improvement** in the overall Data Quality Index (DQI) by addressing:

1. **Completeness**: Reducing the density of "?" null encodings in features like `weight` and `medical_specialty`.
2. **Validity**: Ensuring clinical markers (HbA1c, glucose levels) fall within realistic physiological ranges.
3. **Consistency**: Using Regex to standardize diagnosis codes (ICD-9) across all 10 years of data.
