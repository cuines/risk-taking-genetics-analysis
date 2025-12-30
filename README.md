# Risk-Taking Genetics Analysis

This repository contains analysis code for a study on the genetic basis of risk-taking behavior.

## Dataset
The hypothetical dataset includes three key pieces of information for each participant:
1. **Genotype** for a specific SNP (e.g., `rs12345`).
2. **Sensation-seeking score** from a standardized personality questionnaire.
3. **Risk-taking metric** from a computerized behavioral task (average amount bet in a gambling game).

## Initial Analysis Goal
The initial analysis aims to compute the Pearson correlation between sensation-seeking scores and risk-taking metrics to explore the relationship between personality traits and actual risk-taking behavior.

## Project Structure
- `analysis_script.py`: Python script for performing correlation analysis.
- `README.md`: This file.

## Future Work
Planned improvements include incorporating genotype as a factor in the analysis, performing stratified correlations by genotype group, and implementing more sophisticated statistical models.