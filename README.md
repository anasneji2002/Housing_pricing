# Housing pricing

This repository contains the implementation of a machine learning project designed for data processing, feature engineering, model training, evaluation, and visualization in order to predict the price of houses in Grand Tunis area.

---

## 📁 Repository Architecture

The repository is structured as follows:

```
my_ml_project/
├── data/
│   ├── raw/                  # Raw, unprocessed data
│   ├── processed/            # Processed/cleaned data
├── notebooks/                # Jupyter notebooks for exploration and prototyping
├── src/\n
│   ├── __init__.py           # Marks src as a package
│   ├── data/                 # Scripts for data processing
│   │   ├── __init__.py
│   │   └── load_data.py
│   ├── features/             # Feature engineering scripts 
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models/               # Model training and evaluation scripts
│   │   ├── __init__.py
│   │   └── train_model.py
│   └── visualization/        # Scripts for generating plots and graphs
│       ├── __init__.py
│       └── visualize.py
├── tests/                    # Unit tests
│   ├── test_data.py          # Tests for data loading and preprocessing
│   ├── test_features.py      # Tests for feature engineering
│   └── test_models.py        # Tests for model training
├── .github/                  # GitHub configuration (optional, e.g., CI/CD workflows)
├── .gitignore                # Files and folders to ignore in version control
├── Dockerfile                # Docker configuration for containerization
├── environment.yml           # Conda environment specification
├── README.md                 # Project overview and instructions
```

---

## 🛠️ Setup Instructions

Follow these steps to set up the project on your local machine:

### **1. Clone the Repository**
First, clone this repository to your local machine:
```bash
git clone <repository_url>
cd <repository_name>
```

### **2. Create a Virtual Environment and install Dependencies**
```bash
conda env create -f environment.yml
```

### **3. Run the Project**
Run the main script to start the project:
```bash
python src/main.py
```

---

## 🧪 Testing
Run the unit tests to ensure everything works correctly:
```bash
pytest
```

---

## ✨ Features
 - Data Loading: Load raw data from CSV files.
 - Feature Engineering: Transform raw data into useful features.
 - Model Training: Train machine learning models with various algorithms.
 - Evaluation: Assess model performance with relevant metrics.
 - Visualization: Generate plots for data and results analysis.

---

Feel free to contribute or open issues to enhance the repository. Let me know if you face any issues during setup!