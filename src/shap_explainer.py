import shap
explainer = shap.Explainer(rf_model, X_train)
shap_values = explainer(X_test)
shap.plots.beeswarm(shap_values[:, :, 1])
shap.plots.waterfall(shap_values[0, :, 1])
