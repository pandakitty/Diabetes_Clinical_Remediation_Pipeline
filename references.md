# Annotated Bibliography: Clinical Data Remediation

### Theoretical Frameworks
* **Pipino, L. L., et al. (2002)**: Defines the data quality dimensions (Completeness, Validity, Consistency) used to establish our DQI.
* **Strack, B., et al. (2014)**: Provides the foundational "Diabetes 130-US Hospitals" dataset and identifies the systemic missingness in lab results.

### Remediation Methodology
* **Azur, M. J., et al. (2011)**: Justifies the use of **MICE (Multiple Imputation by Chained Equations)** as a superior alternative to listwise deletion for clinical data.
* **Van Buuren, S. (2018)**: Offers the statistical basis for **Iterative Imputation**, which our `DataRemediator` class implements via Scikit-Learn.
