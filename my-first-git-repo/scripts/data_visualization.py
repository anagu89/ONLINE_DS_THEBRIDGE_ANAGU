import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def plot_data(data):
    data.plot(kind='bar', x='name', y='grade')
    plt.show()

def main():
    data = load_data('../data/sample_data.csv')
    plot_data(data)

if __name__ == '__main__':
    main()
