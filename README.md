**PART 1: THEORETICAL UNDERSTANDING**

**A)**

**1. Define algorithmic bias and provide two examples of how it manifests in AI systems.**

Algorithmic bias occurs when an AI system produces unfair or discriminatory outcomes due to biased data, flawed model design, or skewed assumptions.

Examples:
Facial recognition performing poorly on darker-skinned individuals, leading to higher misidentification rates.
Hiring algorithms favoring male candidates because they were trained on historical data dominated by men.

**2. Explain the difference between transparency and explainability in AI. Why are both important?**

Transparency means understanding how an AI system was built — its data sources, model architecture, training steps, and decision pipeline.
Explainability means being able to interpret why the model made a specific prediction or decision.

**Importance:**

They build trust with users.
They make it easier to identify and reduce bias.
They support accountability by helping organizations justify AI decisions.

**3. How does GDPR (General Data Protection Regulation) impact AI development in the EU?**

GDPR influences AI development by:

Requiring explicit user consent before collecting personal data.
Granting users the right to access, correct, or delete their data.
Mandating data minimization, meaning only necessary data can be collected.
Supporting the right to explanation, pushing developers to build transparent and explainable AI systems.

**B)**

**1. Ethical Principles Matching
**

B) Non-maleficence → Ensuring AI does not harm individuals or society.
C) Autonomy → Respecting users’ right to control their data and decisions.
D) Sustainability → Designing AI to be environmentally friendly.
A) Justice → Fair distribution of AI benefits and risks.

**Part 2: CASE STUDY ANALYSIS**

**Case 1: Biased Hiring Tool**

-Amazon’s hiring AI became biased because it was trained on historically male-dominated resumes, causing it to favor men and penalize words linked to women.

Fixes include:

Balancing the training data to include equal representation.
Removing gender-related features (e.g., names, women’s groups).
Using fairness-aware training and regular audits to reduce bias.

Fairness can be evaluated using:

Demographic Parity (equal selection rates)
Equal Opportunity (equal chance for qualified candidates)
Disparate Impact Ratio (checks for discrimination)

**Case 2: Facial Recognition in Policing**

**1. Ethical Risks**

Wrongful Arrests - Higher misidentification rates for minorities can lead to innocent people being detained or charged.

Privacy Violations - Constant surveillance and tracking undermine citizens’ privacy and may be used without consent.

Discrimination & Inequality - Biased performance reinforces systemic discrimination, especially against marginalized groups.

Loss of Public Trust - Communities may lose confidence in law enforcement if technology is unfair or misused.

**2. Recommended Policies for Responsible Deployment.**

Mandatory Bias Testing and Third-Party Audits - Evaluate accuracy across race, gender, and age groups before deployment. Publish results for transparency.

Strict Human Oversight - Facial recognition should never be the sole basis for arrests—officers must verify matches manually.

Clear Regulation and Legal Limits - Define when, where, and how police can use facial recognition. Require warrants for non-emergency use.

Data Privacy Protections - Limit data retention, prevent mass surveillance, and ensure compliance with privacy laws.

**PART 3: PRACTICAL AUDIT**

**Report

Audit Findings:**

The COMPAS recidivism dataset exhibits clear racial bias. Black individuals were more likely to be classified as high risk compared to White individuals, resulting in a higher false positive rate for Black defendants. Disparate impact analysis also indicates that the probability of being predicted as high risk is disproportionately higher for unprivileged racial groups.

**Remediation Steps:**

To mitigate bias, we applied a reweighing preprocessing technique from IBM’s AI Fairness 360. This adjusts the weights of samples to balance the influence of privileged and unprivileged groups during model training. After re-training the classifier with weighted samples, false positive disparities were reduced, and disparate impact approached parity, while overall accuracy remained stable. Other potential mitigation strategies include adversarial debiasing, reject option classification, or post-processing adjustments to model outputs.

**Recommendations:**

Regular bias audits should be conducted whenever the dataset is updated or the model is retrained. Transparency with stakeholders and monitoring for model drift are crucial to ensure fairness over time. AI systems deployed in high-stakes areas like criminal justice must combine algorithmic mitigation with human oversight to prevent unfair outcomes and ensure accountability.

**PART 4: ETHICAL RREFLECTION**

**Ethical Reflection**

In my AI projects, I will ensure ethical standards by using fair and representative data, checking for bias, and applying corrections where needed. I will maintain transparency by documenting how the model works and making its decisions understandable to users. To protect privacy, I will collect only essential data, store it securely, and follow regulations like GDPR. I will also include human oversight for important decisions and choose energy-efficient methods to reduce environmental impact. By following these principles, I can build AI systems that are fair, trustworthy, and responsible.

**Ethical AI Use in Healthcare**

AI systems in healthcare must protect patient rights and ensure safe, fair medical decisions. Patients must give informed consent, understand how their data is used, and be allowed to opt out without losing access to care. Data must be securely stored and anonymized where possible. To reduce bias, AI tools should be trained on diverse datasets, tested for fairness, and continuously monitored, with human clinicians reviewing all high-risk decisions. Transparency is essential: AI models must provide explainable results, and healthcare providers must clearly communicate AI involvement, document system limitations, and maintain accountability through error-reporting procedures. These principles ensure AI supports, rather than replaces, ethical and trustworthy healthcare delivery.






