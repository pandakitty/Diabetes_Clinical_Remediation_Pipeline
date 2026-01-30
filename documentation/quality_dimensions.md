# Data Quality Dimensions & DQI Framework

This project utilizes a Data Quality Index (DQI) to measure the success of the remediation pipeline. The primary goal is a **25% improvement** in this composite score across three dimensions:

## 1. Completeness
* **Target Feature**: `weight`
* **Metric**: Null density reduction.
* **Current State**: High missingness (approx. 97% encoded as "?").
* **Remediation Goal**: Utilize **MICE/KNN imputation** to replace nulls with statistically viable values, reducing the information gap for predictive modeling.

## 2. Consistency
* **Target Feature**: `diag_1` (Primary Diagnosis)
* **Metric**: Standardization of clinical categories.
* **Remediation Goal**: Apply **Regex-based normalization** to map diverse ICD-9 codes into their primary clinical categories (e.g., Circulatory, Respiratory, Digestive) for uniform analysis.

## 3. Validity
* **Target Feature**: `num_lab_procedures`
* **Metric**: Range constraint validation.
* **Validation Goal**: Ensure all records fall within the expected clinical range of **1 to 132** lab procedures. Any outliers outside this range will be flagged during the **Clinical Audit** phase.

**Quick Navigation**
* [View Data Quality Framework](https://pandakitty.github.io/Diabetes_Clinical_Remediation_Pipeline/documentation/quality_dimensions.html)
