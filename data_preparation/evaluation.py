import numpy as np


def to_subsets(labels):
    clusters = {}

    for idx, label in enumerate(labels):
        if label is None:
            continue

        if label not in clusters:
            clusters[label] = []

        clusters[label].append(idx)

    values = list(clusters.values())
    for idx, value in enumerate(values):
        values[idx] = set(value)

    return values


def jaccard_similarity(set1, set2):
    return float(len(set1 & set2)) / len(set1 | set2)


def similarity_matrix(expected_subsets, actual_subsets):
    matrix = []

    for actual_idx, actual_set in enumerate(actual_subsets):
        matrix.append([])

        for expected_set in expected_subsets:
            matrix[actual_idx].append(jaccard_similarity(actual_set, expected_set))

    return np.array(matrix)


def weight_matrix(expected_subsets, actual_subsets, total_labels):
    matrix = []

    fraction = 1. / float(total_labels)

    for expected_idx, expected_set in enumerate(expected_subsets):
        matrix.append([])

        for actual_set in actual_subsets:
            intersection = actual_set & expected_set
            difference = actual_set | expected_set - intersection
            additional = actual_set - intersection
            missing = expected_set - intersection

            additional_percentage = float(len(additional)) / float(len(actual_set))
            missing_percentage = float(len(missing)) / float(len(expected_set))

            relative_weight = len(intersection) - (additional_percentage * missing_percentage * len(difference))
            weight = fraction * float(max(relative_weight, 0))

            matrix[expected_idx].append(weight)

    return np.array(matrix)


def matching_score(expected_labels, labels):
    expected_subsets = to_subsets(expected_labels)
    actual_subsets = to_subsets(labels)

    similarities = similarity_matrix(expected_subsets, actual_subsets)
    weights = weight_matrix(expected_subsets, actual_subsets, len(expected_labels))

    return (similarities @ weights).sum()


def best_fit_matching_score(expected_labels, labels):
    expected_subsets = to_subsets(expected_labels)
    actual_subsets = to_subsets(labels)

    similarities = similarity_matrix(expected_subsets, actual_subsets)

    rows, cols = similarities.shape
    if cols > rows:
        similarities = similarities.T

    total_similarity = 0
    for row in similarities:
        total_similarity += row.max()

    return total_similarity / len(similarities)


if __name__ == '__main__':
    expectations = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
    actual       = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]

    print(best_fit_matching_score(expectations, actual))

