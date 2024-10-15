import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def generate_poisson_events(lambda_param, num_events):
    return stats.poisson.rvs(lambda_param, size=num_events)

def generate_normal_events(mean, std_dev, num_events):
    return stats.norm.rvs(mean, std_dev, size=num_events)

def plot_distribution(data, title):
    plt.hist(data, bins=30, density=True, alpha=0.7)
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

def compare_distributions(data1, data2, label1, label2):
    plt.hist(data1, bins=30, density=True, alpha=0.7, label=label1)
    plt.hist(data2, bins=30, density=True, alpha=0.7, label=label2)
    plt.legend()
    plt.title(f'Comparison: {label1} vs {label2}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()