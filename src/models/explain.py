import shap
import matplotlib.pyplot as plt

def shap_summary_plot(model, X):
    explainer = shap.Explainer(model, X)
    shap_values = explainer(X)
    shap.summary_plot(shap_values, X)
    plt.show()

def shap_force_plot(model, X, idx=0):
    explainer = shap.Explainer(model, X)
    shap_values = explainer(X)
    shap.force_plot(explainer.expected_value, shap_values[idx], X.iloc[idx], matplotlib=True)
    plt.show()
