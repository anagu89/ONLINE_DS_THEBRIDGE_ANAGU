import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def main():
    data = load_data('../data/sample_data.csv')
    print(data.head())

if __name__ == '__main__':
    main()
