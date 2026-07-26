import matplotlib.pyplot as plt
import shap

# Create SHAP Explainer
explainer = shap.Explainer(rf_model, X_train)

# Generate SHAP Values
shap_values = explainer(X_test)

# SHAP Summary Plot
plt.figure(figsize=(10,6))
shap.plots.beeswarm(shap_values[:, :, 1], show=False)
plt.savefig("../assets/shap_summary.png")
plt.show()

# SHAP Waterfall Plot
plt.figure(figsize=(10,6))
shap.plots.waterfall(shap_values[0, :, 1], show=False)
plt.savefig("../assets/shap_waterfall.png")
plt.show()
