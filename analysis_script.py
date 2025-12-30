#!/usr/bin/env python3
"""
Simple analysis script for risk-taking genetics study.
Calculates correlation between sensation-seeking scores and risk task metrics.
"""

import numpy as np

# Sample data
genotypes = ['AA', 'AG', 'GG', 'AA']
sensation_scores = [1.2, 3.5, 2.8, 1.5]
risk_metrics = [10, 50, 35, 12]

def pearson_correlation(x, y):
    """Compute Pearson correlation coefficient between two lists."""
    if len(x) != len(y):
        raise ValueError("Lists must have same length")
    x = np.array(x)
    y = np.array(y)
    return np.corrcoef(x, y)[0, 1]

if __name__ == "__main__":
    print("Risk-Taking Genetics Analysis")
    print("=============================")
    print(f"Genotypes: {genotypes}")
    print(f"Sensation-seeking scores: {sensation_scores}")
    print(f"Risk task metrics: {risk_metrics}")
    print()
    
    # Calculate correlation
    corr = pearson_correlation(sensation_scores, risk_metrics)
    print(f"Pearson correlation between sensation-seeking and risk-taking: {corr:.3f}")
    print()
    print("Note: This is a simple bivariate correlation ignoring genotype effects.")