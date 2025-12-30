#!/usr/bin/env python3
"""
Stratified analysis script for risk-taking genetics study.
Calculates correlation between sensation-seeking scores and risk task metrics,
separately for each genotype group.
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
    if len(x) < 2:
        return None  # Not enough data to compute correlation
    x = np.array(x)
    y = np.array(y)
    return np.corrcoef(x, y)[0, 1]

def stratified_correlation(genotypes, scores, metrics):
    """
    Group data by genotype and compute correlation for each group.
    Returns a dictionary mapping genotype -> correlation coefficient.
    """
    # Map genotype to lists of scores and metrics
    groups = {}
    for gt, sc, rm in zip(genotypes, scores, metrics):
        groups.setdefault(gt, {'scores': [], 'metrics': []})
        groups[gt]['scores'].append(sc)
        groups[gt]['metrics'].append(rm)
    
    # Compute correlation per group
    results = {}
    for gt, data in groups.items():
        n = len(data['scores'])
        if n >= 2:
            corr = pearson_correlation(data['scores'], data['metrics'])
            results[gt] = corr
        else:
            results[gt] = None  # insufficient data
    return results

if __name__ == "__main__":
    print("Risk-Taking Genetics Analysis - Stratified by Genotype")
    print("======================================================")
    print(f"Genotypes: {genotypes}")
    print(f"Sensation-seeking scores: {sensation_scores}")
    print(f"Risk task metrics: {risk_metrics}")
    print()
    
    # Calculate overall correlation (for reference)
    overall_corr = pearson_correlation(sensation_scores, risk_metrics)
    print(f"Overall Pearson correlation (ignoring genotype): {overall_corr:.3f}")
    print()
    
    # Stratified analysis
    stratified_results = stratified_correlation(genotypes, sensation_scores, risk_metrics)
    print("Stratified correlations by genotype:")
    for gt, corr in sorted(stratified_results.items()):
        if corr is None:
            print(f"  {gt}: insufficient data (n < 2)")
        else:
            print(f"  {gt}: r = {corr:.3f}")
    print()
    print("Note: This analysis accounts for genotype as a grouping factor.")