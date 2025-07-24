from sklearn.metrics import average_precision_score, f1_score, confusion_matrix

def evaluate_model(y_true, y_pred, y_proba):
    auc_pr = average_precision_score(y_true, y_proba)
    f1 = f1_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred)
    return {'AUC-PR': auc_pr, 'F1': f1, 'ConfusionMatrix': cm}
