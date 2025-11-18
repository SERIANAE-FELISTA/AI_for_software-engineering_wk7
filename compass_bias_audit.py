import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing

# ----------------------
# 1. Load Dataset
# ----------------------
df = pd.read_csv("compas-scores.csv")
df['two_year_recid'] = df['two_year_recid'].apply(lambda x: 1 if x==1 else 0)

print("Dataset head:\n", df.head())
print("Race counts:\n", df['race'].value_counts())

# ----------------------
# 2. Prepare BinaryLabelDataset
# ----------------------
privileged_groups = [{'race': 1}]  # White
unprivileged_groups = [{'race': 0}]  # Black

dataset = BinaryLabelDataset(
    df=df,
    label_names=['two_year_recid'],
    protected_attribute_names=['race']
)

# ----------------------
# 3. Split Data & Train Classifier
# ----------------------
X = df.drop(columns=['two_year_recid'])
y = df['two_year_recid']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# ----------------------
# 4. Evaluate Bias
# ----------------------
dataset_pred = BinaryLabelDataset(
    df=X_test.assign(two_year_recid=y_pred),
    label_names=['two_year_recid'],
    protected_attribute_names=['race']
)

metric = ClassificationMetric(dataset, dataset_pred,
                              unprivileged_groups=unprivileged_groups,
                              privileged_groups=privileged_groups)

print("False Positive Rate Difference:", metric.false_positive_rate_difference())
print("Disparate Impact:", metric.disparate_impact())

# ----------------------
# 5. Visualize Disparity
# ----------------------
labels = ['White (Privileged)', 'Black (Unprivileged)']
fpr_values = [
    metric.false_positive_rate(privileged=True),
    metric.false_positive_rate(privileged=False)
]

plt.bar(labels, fpr_values, color=['blue', 'red'])
plt.ylabel("False Positive Rate")
plt.title("FPR Disparity by Race")
plt.show()

# ----------------------
# 6. Apply Bias Mitigation (Reweighing)
# ----------------------
RW = Reweighing(unprivileged_groups=unprivileged_groups,
                privileged_groups=privileged_groups)
dataset_transf = RW.fit_transform(dataset)

clf.fit(X_train, y_train, sample_weight=dataset_transf.instance_weights)

print("Model retrained with reweighing applied to mitigate bias.")
