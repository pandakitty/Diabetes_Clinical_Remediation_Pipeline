import matplotlib.pyplot as plt
import seaborn as sns

class QualityVisualizer:
    """Validates remediation via distribution analysis."""

    def plot_remediation_delta(self, before_df, after_df, column):
        """Generates KDE plots to ensure no statistical skew was introduced."""
        plt.figure(figsize=(10, 6))
        sns.kdeplot(before_df[column], label='Before Remediation', shade=True)
        sns.kdeplot(after_df[column], label='After Remediation (MICE)', shade=True)
        plt.title(f'Distribution Validation for {column}')
        plt.legend()
        plt.show()
