![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Data Quality](https://img.shields.io/badge/DQI%20Target-25%25%20Improvement-orange)
![Status](https://img.shields.io/badge/Project%20Status-Staged-brightgreen)

# Multi-Dimensional Risk Modeling and Clinical Data Remediation
## Analysis of the Diabetes 130-US Hospitals (1999-2008) Dataset.

### Project Abstract
This project develops an automated Python-based pipeline for the audit and remediation of clinical informatics. Utilizing the **Diabetes 130-US Hospitals (1999-2008)** dataset, the team aims to transform "dirty" medical records into a high-fidelity asset suitable for predictive modeling. The primary goal is to achieve a measurable **25% improvement in the Data Quality Index (DQI)**.

## Research Questions & Responsibilities

* **RQ1 (Christian - Data Wrangler):** Can an automated Python-based pipeline achieve a measurable **25% improvement in the Data Quality Index (DQI)**?
* **RQ2 (Kirsten - Data Scientist):** To what extent does applying **MICE/KNN imputation** reduce statistical bias?
* **RQ3 (Mugtaba - Data Visualizer):** How can visual analytics effectively communicate the impact of data remediation?
* **RQ5 (Ashley - Project Manager):** Which specific quality dimension shows the most significant **delta**?

 ---
**Legend: Research Terminology – Delta:** The measurable change or improvement between the raw and remediated states | **Statistical Bias:** Systemic error introduced by improper handling of missingness | **Listwise Deletion:** The practice of dropping entire rows with missing data | **High-Fidelity Asset:** Data that has been verified for integrity, accuracy, and consistency.

### Technical Stack & Tooling

* **Data Wrangling**: Pandas and NumPy
* **Data Science**: Scikit-Learn
* **Data Visualization**: Matplotlib and Seaborn
* **Project Management**: GitHub Version Control

## Results & Impact
This table tracks the performance of the pipeline against the project's success metrics.

| Quality Dimension | Raw Baseline | Remediated Score | Delta (%) |
| :--- | :--- | :--- | :--- |
| Completeness | 3% | 98% | +3166% |
| Consistency | 70% | 95% | +35% |
| Validity | 85% | 99% | +16% |
| **Composite DQI** | **52.6%** | **97.3%** | **+85%** |

## Conclusion
The automated remediation pipeline successfully achieved a significant improvement in data integrity, moving the Composite DQI from 52.6% to 97.3%. By utilizing MICE/KNN imputation to handle clinical missingness and Regex for ICD-9 normalization, the team reduced statistical bias and transformed the raw UCI dataset into a high-fidelity asset. Visual analytics (provided in the plots folder) confirm that the remediated distributions maintain clinical relevance, making the dataset suitable for advanced predictive modeling.

### 📂 Quick Navigation
* **[Clinical Data Quality Dimensions](https://github.com/pandakitty/Diabetes_Clinical_Remediation_Pipeline/blob/main/documentation/quality_dimensions.md)**: Definitions for Completeness, Validity, and Consistency.
* **[Clinical Audit Report](https://github.com/pandakitty/Diabetes_Clinical_Remediation_Pipeline/blob/main/documentation/audit_report.md)**: Detailed summary of remediation logic and verification.
* **[Clinical Data Dictionary](https://github.com/pandakitty/Diabetes_Clinical_Remediation_Pipeline/blob/main/documentation/data_dictionary.md)**: Feature descriptions and clinical ranges.
* **[Remediation Methodology](https://github.com/pandakitty/Diabetes_Clinical_Remediation_Pipeline/blob/main/references.md)**: Justification for MICE/KNN vs. Listwise Deletion.
* **[Setup Requirements](https://github.com/pandakitty/Diabetes_Clinical_Remediation_Pipeline/blob/main/requirements.txt)**: Environment dependencies.
