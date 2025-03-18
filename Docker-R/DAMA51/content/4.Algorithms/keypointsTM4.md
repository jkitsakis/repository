Title: Fundamental Machine Learning Algorithms from TM4.pdf Notes
Slug: algorithms
Category_Order: 4 
Order: 1 
Summary: **Decision Trees, Random Forest, Naive Bayes, Logistic Regression, Linear Regression, and k-Nearest Neighbors**

The topics of **machine learning and data analysis** covered seem to focus on the following key areas:

The TM4 tutorial meeting document from the Hellenic Open University covers several fundamental machine learning algorithms. Here's a breakdown of the key algorithms mentioned:

### **1. Decision Trees**
- Used for both classification and regression tasks.
- Structure:
  - Nodes: Decision points based on attribute values.
  - Leaves: Final classification or decision.
  - Branches: Different outcomes of a decision.
- **Popular Decision Tree Algorithms:**
  - **ID3 (Iterative Dichotomiser 3)** – Uses entropy and information gain for attribute selection.
  - **C4.5 & C5.0** – Improvements over ID3, handling continuous values and pruning.
  - **CART (Classification and Regression Trees)** – Uses the Gini index for splitting.

---

### **2. Bayes Classifiers**
- Based on **Bayes' Theorem**, which calculates the probability of a class given a set of features.
- **Naïve Bayes**:
  - Assumes independence between features.
  - Works well for text classification (e.g., spam detection).
- **Limitation**: Assumption of independence rarely holds in real-world data.

---

### **3. Regression**
- Used for predicting continuous values.
- **Linear Regression**:
  - Finds the best fit line by minimizing the sum of squared errors.
  - Can be solved using **closed-form solutions (Normal Equation)** or **Gradient Descent**.
- **Logistic Regression**:
  - Used for classification (binary/multiclass).
  - Uses the **sigmoid function** to model probabilities.

---

### **4. Nearest-Neighbor Predictors (k-NN)**
- A **lazy learning algorithm** (stores all training data).
- **Classification**: Assigns the majority class among k nearest neighbors.
- **Regression**: Averages the values of k nearest neighbors.
- **Challenges**:
  - Sensitive to noisy data.
  - High computational cost with large datasets.


---

#### **5. Entropy & Information Gain (Feature Selection)**
- Used in decision tree algorithms like **ID3, C4.5, and C5.0**.
- **Shannon Entropy**:
  - Measures impurity in a dataset.
  - Lower entropy means purer nodes.
- **Information Gain**:
  - Measures reduction in entropy after a split.
  - Used to select the best attribute for decision tree splitting.

---

#### **6. Gini Index (Used in Decision Trees)**
- Used by **CART (Classification and Regression Trees)** instead of entropy.
- Measures impurity:
  - Lower values indicate purer nodes.
  - Common in classification problems.

---

#### **7. Gain Ratio (Quinlan 1986/1993)**
- Improvement over information gain.
- Adjusts for attributes with many values.
- Used in **C4.5 Decision Trees**.

---

#### **8. Minimum Description Length (MDL) Principle**
- Based on **Occam’s Razor**: Prefer the simplest hypothesis.
- Used in **Decision Tree Pruning** to avoid overfitting.

---

#### **9. Pruning Techniques (Overfitting Reduction)**
- **Pre-Pruning**: Stops tree growth early based on conditions.
- **Post-Pruning**: Trims the fully grown tree based on evaluation metrics.
- **Reduced-Error Pruning**: Removes branches that don’t improve accuracy.
- **Pessimistic Pruning**: Assumes unseen data would behave similarly.

---

#### **10. Lazy Learning vs. Eager Learning**
- **Lazy Learning (e.g., k-NN)**: Stores data and makes predictions when queried.
- **Eager Learning (e.g., Decision Trees, Regression)**: Builds a model before making predictions.

---

#### **11. Splitting on Numerical Attributes (Handling Continuous Data)**
- Converts numerical features into categorical ones.
- Uses thresholding and binning techniques.

---

#### **12. Missing Value Handling**
- Replace missing values with:
  - The **most frequent** value in a class.
  - **Mean/Median** for numerical values.
  - A **placeholder category** if missing values are frequent.

---

#### **13. k-Nearest Neighbors (k-NN) Enhancements**
- **Distance Metrics**:
  - **Euclidean Distance** (default)
  - **Manhattan Distance** (for grid-based data)
  - **Minkowski Distance** (generalized form)
- **Weighted k-NN**: Assigns more influence to closer neighbors.
- **Choosing Optimal k**:
  - Cross-validation to avoid overfitting (low k) and underfitting (high k).

---

### **Key Takeaways**
- The tutorial discusses **supervised learning** algorithms with a focus on **classification and regression**.
- **Decision Trees, Bayes Classifiers, Regression, and k-NN** are the primary models.
- **Feature selection** (Entropy, Gini Index, Gain Ratio) and **pruning** are crucial for optimizing models.
- **Handling numerical attributes and missing values** is essential for real-world applications.

---

### **What You Need to Know About These Algorithms** 
To effectively use the algorithms covered in TM4, you should understand their **strengths, weaknesses, applications, and key concepts**. Below is a structured breakdown:

---

## **📌 1. Decision Trees**  
**🔹 Key Concepts:**
- **Tree Structure**: Nodes (decisions), branches (outcomes), leaves (final classification).
- **Splitting Criteria**:  
  - **Entropy & Information Gain (ID3, C4.5)** → Choose attributes that reduce entropy the most.  
  - **Gini Index (CART)** → Measures impurity of a node; lower is better.  
  - **Gain Ratio (C4.5 improvement)** → Adjusts for biased splits with many categories.  

**🔹 Handling Issues:**  
- **Overfitting?** Use **pruning techniques** (pre-pruning stops early, post-pruning trims after full growth).  
- **Numerical Data?** Convert into categorical (e.g., threshold-based splits).  
- **Missing Values?** Replace with the most common or mean value in the same class.  

**🔹 When to Use?**
✔️ When you need an **interpretable model** (e.g., medical decisions).  
✔️ When features are a **mix of categorical and numerical**.  
❌ Not ideal for **large datasets** (deep trees can be slow).

---

## **📌 2. Bayes Classifiers** (Naïve Bayes)  
**🔹 Key Concepts:**
- **Uses Bayes’ Theorem**:  
  \\[
  P(Class|Data) = \frac{P(Data|Class) P(Class)}{P(Data)}
  \\]  
- **Naïve Assumption**: Features are independent given the class (often unrealistic).  
- **Works well with text data (Spam filtering, Sentiment Analysis).**  

**🔹 When to Use?**  
✔️ When working with **high-dimensional data** (e.g., text classification).  
✔️ When you need a **fast and simple** classifier.  
❌ Fails when **features are correlated** (independence assumption breaks).  

---

## **📌 3. Regression (Linear & Logistic)**  
**🔹 Linear Regression** (for continuous outputs):  
- Fits a **straight-line equation**:  
  \\[
  y = mx + b
  \\]
- Uses **least squares method** to minimize prediction error.

**🔹 Logistic Regression** (for classification):  
- Predicts probabilities using the **sigmoid function**:  
  \\[
  P(y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x)}}
  \\]
- Used for **binary classification**.

**🔹 When to Use?**  
✔️ Linear Regression: When relationships are approximately **linear** (e.g., predicting house prices).   
✔️ Logistic Regression: When predicting **binary outcomes** (e.g., pass/fail, fraud detection).   
❌ Doesn’t work well with **non-linear** relationships.  

---

## **📌 4. Nearest-Neighbor Predictors (k-NN)**  
**🔹 Key Concepts:**  
- **Lazy learner** → No training phase; stores data and classifies based on closest points.  
- Uses **distance metrics**:  
  - **Euclidean Distance** (default) → Best for continuous features.  
  - **Manhattan Distance** → Better for grid-based data.  

**🔹 Tuning k (number of neighbors)**:  
- **Small k?** Leads to overfitting (high variance).  
- **Large k?** Leads to underfitting (too generic).  

**🔹 When to Use?**  
✔️ When **data is small** and you need a **non-parametric model**.  
✔️ Good for **pattern recognition** (e.g., handwriting recognition).  
❌ Not great for **large datasets** (slow lookups).  

---

## **📌 5. Feature Selection Metrics (Entropy, Gini, Gain Ratio)**  
**🔹 Why?** Avoid irrelevant features that slow models down.  
- **Entropy & Information Gain**: Picks attributes that reduce disorder.  
- **Gini Index**: Works similarly but focuses on purity of groups.  
- **Gain Ratio**: Adjusts information gain to prevent bias toward attributes with many values.

**🔹 When to Use?**  
✔️ Before building Decision Trees or other models to improve efficiency.  
✔️ When dealing with **many categorical features**.  

---

## **📌 6. Model Optimization (Pruning & Overfitting Control)**  
**🔹 Avoiding Overfitting in Decision Trees**:  
- **Pre-pruning**: Stop splitting if information gain is small.  
- **Post-pruning**: Cut back parts of the tree if they don’t generalize well.  

**🔹 In k-NN:**  
- Reduce overfitting by **increasing k** (but not too much).  

**🔹 In Regression:**  
- Use **regularization techniques** like Ridge or Lasso regression.  

---

## **📌 7. Handling Missing Values**  
- **Replace with Most Frequent Value** (for categorical data).  
- **Mean/Median Imputation** (for numerical data).  
- **Drop Rows** if too many values are missing.  

---

## **📌 8. Key Differences Between Lazy & Eager Learning**  
| **Type**  | **Description** | **Example Algorithms** |
|-----------|---------------|--------------------|
| **Lazy Learning** | No training phase; stores data and makes predictions on demand. | k-NN |
| **Eager Learning** | Builds a model before predictions. | Decision Trees, Regression |  

---

### **🚀 Practical Summary: What to Focus On**  
1. **Understand the types of problems these models solve**:  
     - **Regression** → Predicts continuous values.  
     - **Classification** → Predicts discrete labels.  
2. **Know when to use pruning & regularization** to avoid overfitting.  
3. **Choose the right metric for feature selection** (Entropy, Gini, Gain Ratio).  
4. **For large datasets**, prefer eager learners (decision trees, regression) over k-NN.  
5. **Optimize hyperparameters** like:  
     - **k** in k-NN.  
     - **Depth & pruning strategy** in decision trees.  
     - **Regularization strength** in regression.  

---

### **Would You Like...**  
✅ **Code examples for each algorithm?**    
✅ **A comparison with deep learning models?**    
✅ **How to implement them in Python (Scikit-learn, TensorFlow, etc.)?**  