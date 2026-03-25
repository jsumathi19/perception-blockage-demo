# Validates: KPI_BLUR_ACC

def evaluate_accuracy(predictions, ground_truth):
    correct = sum(p == g for p, g in zip(predictions, ground_truth))
    return correct / len(predictions)

if __name__ == "__main__":
    preds = [1, 0, 1, 1]
    gt = [1, 0, 0, 1]
    acc = evaluate_accuracy(preds, gt)
    print(f"Accuracy: {acc}")