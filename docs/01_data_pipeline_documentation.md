# Data Pipeline Documentation

## Overview

The `01_data_pipeline.ipynb` notebook implements a complete data processing pipeline for ENTSOE (European Network of Transmission System Operators) electricity market data. This pipeline downloads, processes, filters, and transforms raw data into analysis-ready formats for Swedish electricity market research.

## Pipeline Steps

### 1. Data Download

**Function**: Downloads ENTSOE data from SFTP server

**Process**:
- Connects to `sftp-transparency.entsoe.eu` using SSH credentials
- Downloads all ZIP files based on defined year from `/TP_export/zip` subdirectories
- Saves files locally under `TP_export_zip/` directory structure
- Requires USERNAME and PASSWORD environment variables

**Input**: Remote ENTSOE SFTP server
**Output**: Local ZIP files in `TP_export_zip/` folders

### 2. ZIP Extraction and CSV Processing

**Function**: Extracts and consolidates CSV data from ZIP files

**Process**:
- Extracts CSV files from downloaded ZIP archives
- Processes CSV files with both tab and comma separators
- Combines multiple CSV files per folder into single consolidated files
- Sorts data by date columns when available
- Uses parallel processing for improved performance
- Removes original ZIP and CSV files after processing

**Input**: ZIP files in `TP_export_zip/` folders
**Output**: Combined CSV files in `processed_data/` directory

### 3. Data Filtering

**Function**: Filters data for Swedish electricity market entries

**Process**:
- Searches for Swedish entries using "SE" in map code columns
- Checks multiple possible column names: `mapcode`, `outareamapcode`, `inaremapcode`, `outmapcode`, `inmapcode`, `areamapcode`, `location`
- Creates filtered datasets containing only Swedish data
- Generates processing logs for each file

**Input**: Combined CSV files from `processed_data/`
**Output**: Filtered CSV files in `filtered_data/` directory

### 4. Data Organization

**Function**: Organizes data by electricity market categories

**Process**:
- Categorizes files based on ENTSOE document codes in filenames
- Moves files to appropriate category subfolders

**Input**: Filtered CSV files from `filtered_data/`
**Output**: Organized files in `filtered_data/{category}/` subfolders

### 5. Data Transformation (Long to Wide Format)

**Function**: Converts time series data from long format to wide format

**Process**:
- Processes each data category separately (starting with Balancing)
- Uses configuration-driven approach with file-specific settings
- Creates unique identifiers by combining specified columns (MapCode, ReserveType, etc.)
- Pivots data using datetime as index and identifiers as columns
- Applies aggregation methods for duplicate handling (sum, first, etc.)

**Key Configuration Elements**:
- Index/date column name: Primary datetime column
- Merging columns: Columns used to create unique identifiers
- Keep columns: Value columns to retain in final dataset
- Aggregation methods: How to handle duplicate entries

**Input**: Organized CSV files from `filtered_data/{category}/`
**Output**: Pivoted CSV files in `pivoted_data/{category}/` directories


## Output Structure

```
processed_data/          # Initial combined files
filtered_data/           # Swedish-filtered data
├── Balancing/              # Balancing market data
├── Generation/             # Generation data  
├── Load/                   # Load forecast data
├── Transmission/           # Transmission data
├── Outages/                # Outage information
└── Congestion Management/  # Congestion data
pivoted_data/               # Wide-format analysis-ready data
├── Balancing/              # Pivoted balancing data
└── [other categories]      # Additional pivoted categories
```

## Data Quality Features

- **Error Handling**: Graceful handling of missing files and columns
- **Encoding Support**: Handles both UTF-8 and Latin1 encoded files
- **Duplicate Detection**: Identifies and handles duplicate time-series entries

## Usage Requirements

- Environment variables: USERNAME and PASSWORD for ENTSOE SFTP access
- Python dependencies: pandas, paramiko, pyarrow, pathlib, concurrent.futures
- Sufficient disk space for downloaded and processed data files (2014-2025 +50GB)
- Access to ENTSOE transparency platform 