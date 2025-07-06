# Feature Attribution Analysis Documentation

## Overview

The `03_feature_attribution.ipynb` notebook provides comprehensive feature attribution analysis for the trained LSTM mFRR prediction model. It employs multiple attribution methods to understand which input features most significantly influence model predictions during different market conditions and time periods.

## Objectives

- **Model Interpretability**: Understand which features drive LSTM predictions for mFRR activation volumes
- **Feature Importance**: Quantify the relative contribution of different market variables
- **Temporal Analysis**: Analyze how feature importance changes during different market events
- **Method Comparison**: Compare multiple attribution techniques for robust insights
- **Case Study Analysis**: Examine model behavior during specific high-activity periods

## Attribution Methods

### 1. Integrated Gradients (IG)
**Approach**: Computes gradients of the model output with respect to input features along a path from baseline to input
**Implementation**: Uses Captum library with configurable baselines and integration steps
**Advantages**: Satisfies axioms of sensitivity and implementation invariance  
**Configuration**:
- Integration steps: 64 (Riemann trapezoid method)
- Internal batch size: 32 for memory efficiency
- Multiple baseline strategies: zeros, median, mean

### 2. DeepLIFT SHAP (DL_SHAP)
**Approach**: Combines DeepLIFT attribution with SHAP value computation
**Implementation**: Leverages Captum's DeepLiftShap implementation
**Advantages**: Provides unified framework connecting gradients and game-theoretic concepts  
**Features**: Handles non-linear activation functions and multiplicative interactions

### 3. Feature Ablation (FA)
**Approach**: Measures importance by systematically removing features and observing prediction changes
**Implementation**: Captum's FeatureAblation with configurable perturbations
**Advantages**: Model-agnostic and intuitive interpretation  
**Configuration**:
- Perturbations per evaluation: 32 for statistical stability
- Baseline replacement values for ablated features

## Baseline Strategies

### Zero Baseline
- **Description**: All input features set to zero (scaled space)
- **Use Case**: Measures absolute contribution from absence of signal
- **Interpretation**: How much each feature contributes relative to no information

### Median Baseline
- **Description**: Features set to median values across analysis window
- **Use Case**: Measures contribution relative to typical market conditions
- **Interpretation**: Deviation from normal market state influence

## Analysis Pipeline

### 1. Data Preprocessing
- **Model Loading**: Loads trained LSTM model with optimal hyperparameters
- **Data Filtering**: Applies region-specific filtering (SE2) with balancing variable exclusion
- **Scaling**: Uses saved RobustScaler objects for consistent preprocessing
- **Sequence Building**: Creates sliding window sequences matching training configuration

### 2. Attribution Computation
- **Input Tensor Construction**: Properly scaled and masked sequences
- **Baseline Generation**: Multiple baseline strategies for robust comparison
- **Attribution Calculation**: Parallel computation across all methods

### 3. Importance Aggregation
- **Temporal Aggregation**: Mean absolute attribution across time steps
- **Sample Aggregation**: Average across multiple prediction windows
- **Normalization**: Convert to percentage contributions for interpretability
- **Ranking**: Identify top-k most important features

## Output Analysis

### Feature Importance Rankings
- **Cross-Method Consensus**: Features consistently ranked high across methods
- **Baseline Sensitivity**: How importance rankings change with different baselines
- **Temporal Stability**: Consistency of feature importance across different time periods
- **Market Condition Dependence**: Feature importance during normal vs. stressed conditions
