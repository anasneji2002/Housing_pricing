# Import everything from the src package (i.e., from all the __init__.py files)
from src import *

def main():
    # Step 1: Load data
    print("Loading data...")
    data = load_data("data/raw/data.csv")
    
    # Step 2: Feature engineering
    print("Building features...")
    features = build_features(data)
    
    # Step 3: Train model
    print("Training model...")
    model = train_model(features)
    
    # Step 4: Evaluate model
    print("Evaluating model...")
    evaluation_results = evaluate_model(model, features)
    
    # Step 5: Visualize results
    print("Visualizing results...")
    plot_results(evaluation_results)
    
    print("Project completed successfully!")

if __name__ == "__main__":
    main()