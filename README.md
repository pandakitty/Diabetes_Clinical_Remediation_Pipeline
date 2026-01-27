![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Data Quality](https://img.shields.io/badge/DQI%20Target-25%25%20Improvement-orange)
![Status](https://img.shields.io/badge/Project%20Status-Staged-brightgreen)

# Multi-Dimensional Risk Modeling and Clinical Data Remediation
## Analysis of the Diabetes 130-US Hospitals (1999-2008) Dataset.
### Project Abstract
This project develops an automated Python-based pipeline for the audit and remediation of clincal informatics. Utalizing the **Diabetes 130-US Hospitals (1999-2008)** dataset, the team aims to transform "dirty" medical records into a high-fidelity asset suitable for predictive modeling. The primary goal is to achieve a measurable **25% improvement in the Data Quality Index (DQI)** by implementing advanced **MICE (Multivariate Imputation by Chained Equations)** and **KNN** algorithims to address missingness and structural inconsistencies. 

## Research Questions & Responsibilites

* **RQ1 (Christain - Data Wrangler):** Can an automated Python-based pipeline achieve a measurbale **25% improvement in the Data Quality Index (DQI)** for the selected clinical dataset?
* **RQ2 (Kirsten - Data Scientist):** To what extent does applying **MICE/KNN imputation** reduce statistical bias in the dataset compared to **listwise deletion** of missing records?
* **RQ3 (Mugtaba - Data Visualizer):** How can visual analytics, such as **Comparative Distribution Plots**, effectively communicate the impact of data remediation to non-technical stakeholders?
* **RQ5 (Ashley - Project Manager):** Which spicific quality dimension (**Completeness, Validity, or Consistency**) shows the most significant **delta (improvement)** when processed through the autmated pipeline?

 ---
**Legend: Research Terminology – Delta:** The measurable change or improvement between the raw and remediated states | **Statistical Bias:** Systemic error introduced by improper handling of missingness | **Listwise Deletion:** The practice of dropping entire rows with missing data | **High-Fidelity Asset:** Data that has been verified for integrity, accuracy, and consistency.

### Technical Stack & Tooling

* **Data Wrangling (Christian):** **Pandas** and **NumPy** for clinical profiling, null detection ("?"), and establishing the baseline **DQI**.
*  **Data Scientist (Kirsten):** **Scikit-Learn (IterativeImputer)** for executing **MICE/KNN** remediation logic and **Regex** for ICD-9 normalization.
*  **Data Visualization (Mugtaba):** **Matplotlib** and **Seaborn** for generating **Comparative Distribution Plots** and **KDE** validation.
*  **Project Management (Ashley):** **GitHub** for version control, branch protection, and enforcing the **Peer Review** process. 
