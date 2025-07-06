# LSTM mFRR Prediction Model Documentation

## Overview

The `02_LSTM_mFRR_prediction.ipynb` notebook implements a deep learning approach for predicting Manual Frequency Restoration Reserve (mFRR) activation volumes in the Swedish electricity market. The model uses Long Short-Term Memory (LSTM) neural networks with PyTorch and includes automated hyperparameter optimization using Optuna.

## Model Architecture

### Core Components

**MaskedLSTM Model**:
- LSTM layers with optional bidirectional processing
- Dense layers for final prediction output
- Dropout regularization for both LSTM and dense layers
- Masking capability to handle missing values in time series data
- Support for multi-horizon forecasting

**Loss Function**:
- Weighted Mean Squared Error (MSE) loss
- Higher weights for larger activation volumes (alpha parameter)
- Mask-aware computation to handle missing data points

## Configuration Parameters

### Target Variable
- **Region**: SE2 (Swedish bidding zone 2)
- **Target**: `Balancing_ActivatedBalancingEnergy_SE2_mFRR_NotSpecifiedDownActivatedVolume`
- **Data Source**: `/results/results_merged.csv`

### Training Configuration
- **Optuna Trials**
- **Max Epochs per Trial**
- **Final Training Epochs**
- **Early Stopping Patience**

### Feature Engineering Flags
- **Indicator Features**: Creates missing value indicators (disabled by default)
- **Cyclical Features**: Hour, day-of-week, week-of-year sine/cosine encoding (disabled)
- **Lagged Features**: Previous time step values (lag 1, 24, 168 hours) (disabled)

## Data Processing Pipeline

### 1. Data Loading and Filtering
- Loads master dataset with all ENTSOE variables
- Applies region-specific filtering for SE2 bidding zone
- Excludes price and volume variables to prevent data leakage
- Stores price data separately for visualization purposes

### 2. Temporal Splitting
- **Training Set**: Data up to 2023-12-31
- **Validation Set 1**: 2024-01-01 to 2025-01-10 (for Optuna optimization)
- **Validation Set 2**: 2024-01-11 to 2025-01-31 (for final model early stopping)
- **Test Set**: 2025-02-01 onwards (for final evaluation)

### 3. Data Scaling
- **Scaler Type**: RobustScaler with 5th-95th percentile range
- **Separate Scalers**: Independent scaling for features (X) and targets (y)
- **Fitted on Training Data**: Prevents data leakage during scaling

### 4. Sequence Generation
- Creates sliding window sequences for time series prediction
- Configurable sequence length (lookback window)
- Supports multi-step ahead forecasting (horizon parameter)
- Handles missing values through masking mechanism

## Hyperparameter Optimization

### Optuna Configuration
- **Sampler**: Tree-structured Parzen Estimator (TPE)
- **Objective**: Minimize validation loss
- **Pruning**: Early trial termination for poor performers

### Search Space
- **Hidden Size**: [32, 64, 128, 256] LSTM units
- **Number of Layers**: 1-3 LSTM layers
- **Bidirectional**: True/False
- **Dense Layer Size**: [32, 64, 128] units
- **Dropout Rates**: 0.0-0.5 for both LSTM and dense layers
- **Learning Rate**: 1e-4 to 5e-3 (log scale)
- **Batch Size**: [64, 128, 256, 512]
- **Sequence Length**: [24, 72, 168] hours

## Training Process

### Optuna Phase
1. Sample hyperparameters from defined search space
2. Build and train model for limited epochs
3. Evaluate on validation set 1
4. Report intermediate results for pruning decisions
5. Return best validation loss as trial objective

### Final Training Phase
1. Use best hyperparameters from Optuna study
1. Save best model based on performance

### Training Features
- **Gradient Clipping**: Prevents exploding gradients (max norm: 1.0)
- **Early Stopping**: Prevents overfitting
- **Model Checkpointing**: Saves best performing model
- **Loss History Tracking**: Records training and validation curves

## Device Management

Automatic device selection with priority order:
1. **Apple Metal Performance Shaders (MPS)**: For Apple Silicon Macs
2. **CUDA**: For NVIDIA GPUs
3. **CPU**: Fallback option

## Output Artifacts

### Model Persistence
- **best_model.pth**: Trained PyTorch model state dictionary
- **scaler_X.joblib**: Feature scaler for preprocessing
- **scaler_y.joblib**: Target scaler for postprocessing
- **best_params.json**: Optimal hyperparameters with metadata

### Analysis Results
- **predictions.parquet**: Test set predictions vs ground truth
- **loss_history.csv**: Training and validation loss curves
- **study.pkl**: Complete Optuna study object

## Usage Guidelines

### Configuration Tuning
- Increase Optuna trials for more thorough hyperparameter search
- Adjust sequence length based on temporal dependencies
- Modify feature engineering flags based on domain knowledge

### Performance Optimization
- Use GPU acceleration when available
- Increase batch size for faster training (if memory permits)
- Enable parallel data loading for large datasets

### Model Validation
- Monitor training/validation loss curves for overfitting
- Analyze residual patterns for model adequacy
- Validate performance on out-of-sample test data
