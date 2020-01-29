import numpy as np
import random
from sklearn.metrics import confusion_matrix

def prety_print_result(mem, pred):
    tn, fp, fn, tp = confusion_matrix(mem, pred).ravel()
    print('TP: %d     FP: %d     FN: %d     TN: %d' % (tp, fp, fn, tn))
    print('PPV: %.4f\nAdvantage: %.4f' % (tp / (tp + fp), tp / (tp+fn) - fp / (tn+fp)))

def get_ppv_tpr(mem, pred):
    tn, fp, fn, tp = confusion_matrix(mem, pred).ravel()
    return tp / (tp + fp), tp / (tp + fn)

def loss_range():
    return list(np.arange(0, 0.001, 0.0001)) + list(np.arange(0.001, 0.01, 0.001)) + list(np.arange(0.01, 0.1, 0.01)) + list(np.arange(0.1, 1, 0.1)) + list(np.arange(1, 10, 1)) + [10, 20]

def get_random_features(data, pool, size):
    random.seed(21312)
    features = set()
    while(len(features) < size):
        feat = random.choice(pool)
        if len(np.unique(data[:,feat])) > 1:
            features.add(feat)
    return list(features)

def generate_noise(shape, dtype, noise_params):
    noise_type, noise_coverage, noise_magnitude = noise_params
    if noise_coverage == 'full':
        if noise_type == 'uniform':
            return np.array(np.random.uniform(0, noise_magnitude, size=shape), dtype=dtype)
        else:
            return np.array(np.random.normal(0, noise_magnitude, size=shape), dtype=dtype)
    attr = np.random.randint(shape[1])
    noise = np.zeros(shape, dtype=dtype)
    if noise_type == 'uniform':
        noise[:, attr] = np.array(np.random.uniform(0, noise_magnitude, size=shape[0]), dtype=dtype)
    else:
        noise[:, attr] = np.array(np.random.normal(0, noise_magnitude, size=shape[0]), dtype=dtype)
    return noise

def plot_sign_histogram(membership, signs, trials):
    mem, non_mem = np.zeros(trials + 1), np.zeros(trials + 1)
    for i in range(len(signs)):
        if membership[i] == 1:
            mem[signs[i]] += 1
        else:
            non_mem[signs[i]] += 1
    plt.plot(np.arange(trials + 1), mem, label='Members')
    plt.plot(np.arange(trials + 1), non_mem, label='Non Members')
    plt.xlabel('Number of Times Loss Increases (out of '+str(trials)+')')
    plt.ylabel('Number of Instances')
    plt.xticks(list(range(0, trials + 1)))
    plt.legend()
    plt.show()

def make_histogram(vector):
    mem = vector[:10000]
    non_mem = vector[10000:]
    data, bins, _ = plt.hist([mem, non_mem], bins=loss_range())
    plt.clf()
    mem_hist = np.array(data[0])
    non_mem_hist = np.array(data[1])
    plt.plot(bins[:-1], mem_hist, label='Members')
    plt.plot(bins[:-1], non_mem_hist, label='Non Members')
    plt.xscale('log')
    plt.xlabel('Per-Instance Loss')
    plt.ylabel('Number of Instances')
    plt.legend()
    plt.show()

def make_membership_box_plot(vector):
    plt.boxplot([vector[:10000], vector[10000:]], labels=['members', 'non-members'], whis='range')
    plt.yscale('log')
    plt.ylabel('Per-Instance Loss')
    plt.show()

def make_predictions_box_plot(vector, mem, pred_mem):
    tp_vec = [vector[i] for i in range(len(vector)) if mem[i] == 1 and pred_mem[i] == 1]
    fn_vec = [vector[i] for i in range(len(vector)) if mem[i] == 1 and pred_mem[i] == 0]
    fp_vec = [vector[i] for i in range(len(vector)) if mem[i] == 0 and pred_mem[i] == 1]
    tn_vec = [vector[i] for i in range(len(vector)) if mem[i] == 0 and pred_mem[i] == 0]
    plt.boxplot([tp_vec, fn_vec, fp_vec, tn_vec], labels=['TP', 'FN', 'FP', 'TN'], whis='range')
    plt.yscale('log')
    plt.ylabel('Per-Instance Loss')
    plt.show()