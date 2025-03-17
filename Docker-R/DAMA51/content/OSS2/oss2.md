Title: OSS2 - Advanced Data Analysis
Slug: oss2
Category_Order: 2
Summary: **Dimensionality reduction (PCA), Classification Evaluation (confusion matrix, ROC curve), Optimization (gradient descent), and Regression  (linear models)**

The document discusses several key topics in data analysis. Here’s a structured list with simple explanations:

Here’s an organized breakdown of the data analysis topics covered in your document, along with simple explanations for each:

### **1. Principal Component Analysis (PCA)**
   - **Concept:** A dimensionality reduction technique that transforms data into a new coordinate system.
   - **Key Points:**
     - Reduces the number of features while retaining maximum variance.
     - Helps in visualization when dealing with high-dimensional data.
     - Uses **eigenvectors** and **eigenvalues** to determine principal components.
     - Standardization (mean = 0, variance = 1) improves PCA effectiveness.
     - Example: Applied to the **Iris dataset** to visualize feature relationships.

### **2. Confusion Matrix and Classification Metrics**
   - **Concept:** A table used to evaluate the performance of a classification model.
   - **Key Points:**
     - **True Positives (TP):** Correctly predicted positive cases.
     - **False Positives (FP):** Incorrectly predicted positive cases (Type I error).
     - **False Negatives (FN):** Incorrectly predicted negative cases (Type II error).
     - **True Negatives (TN):** Correctly predicted negative cases.
     - Metrics:
       - **Sensitivity (Recall):** TP / (TP + FN) – ability to identify positive cases.
       - **Specificity:** TN / (TN + FP) – ability to identify negative cases.
       - **Precision:** TP / (TP + FP) – reliability of positive predictions.
       - **Accuracy:** (TP + TN) / Total – overall model performance.
       - **F1-score:** Balance between precision and recall.
     - **Example:** Used in COVID-19 classification problems.

### **3. ROC Curve & AUC (Receiver Operating Characteristic Curve)**
   - **Concept:** A graphical representation of classification model performance across different thresholds.
   - **Key Points:**
     - **True Positive Rate (TPR)** vs **False Positive Rate (FPR).**
     - **Optimal threshold** balances sensitivity and specificity.
     - **Area Under Curve (AUC):** Measures overall model effectiveness.
     - **Example:** Used to fine-tune decision thresholds in medical diagnosis.

### **4. Gradient Descent Optimization**
   - **Concept:** An iterative optimization algorithm to minimize an error function.
   - **Key Points:**
     - Moves in the opposite direction of the gradient to find the **global minimum**.
     - Uses **learning rate (step size)** to control movement speed.
     - **Convex functions** are ideal for minimization.
     - Can be applied to neural networks for parameter tuning.
     - Example: Used for optimizing error functions in machine learning models.

### **5. Linear Regression**
   - **Concept:** A statistical method to predict a dependent variable based on an independent variable.
   - **Key Points:**
     - Finds the **best-fit line** that minimizes errors.
     - Uses the formula **Y = aX + b** (where `a` is slope, `b` is intercept).
     - **Least Squares Method** minimizes the sum of squared errors.
     - **Gradient Descent** is an alternative method for optimization.
     - **Example:** Predicting house prices based on square footage.

### **6. Logistic Regression**
   - **Concept:** A classification algorithm for predicting binary outcomes.
   - **Key Points:**
     - Uses a **sigmoid function** to map outputs between 0 and 1.
     - Often used in **binary classification** problems.
     - Outputs a probability that is converted to a class label (0 or 1).
     - **Example:** Used for medical diagnosis (disease vs no disease).

### **7. Hypothesis Testing**
   - **Concept:** A statistical method to test assumptions about data.
   - **Key Points:**
     - **Null Hypothesis (H₀):** Assumption that there is no effect.
     - **Alternative Hypothesis (H₁):** Assumption that there is an effect.
     - Uses **p-values** to determine statistical significance.
     - **Example:** Testing if a new drug significantly reduces weight.


---

## Further in-depth analysis on each topic along with **R code examples** for better understanding.  


## **1. Principal Component Analysis (PCA)**  
### **Further Analysis**
PCA is used in scenarios where:
- There are too many features in a dataset, making computations expensive.
- Some features are highly correlated, leading to redundant information.
- You want to visualize high-dimensional data in 2D or 3D.

### **Mathematical Foundation**
- PCA finds a new set of **orthogonal axes (principal components)**.
- The first principal component (PC1) captures the most variance.
- The second principal component (PC2) is perpendicular to PC1 and captures the next highest variance.
- Eigenvalues determine how much variance each principal component explains.
- The **covariance matrix** helps in computing the eigenvectors and eigenvalues.

### **Example in R**
Let’s perform PCA on the **Iris dataset** in R:

```r
# Load dataset
data(iris)

# Remove categorical variable
iris_numeric <- iris[, 1:4]  

# Standardizing the data (important for PCA)
iris_scaled <- scale(iris_numeric)

# Perform PCA
pca_result <- prcomp(iris_scaled, center = TRUE, scale = TRUE)

# Summary of PCA
summary(pca_result)

# Plot the variance explained by each principal component
screeplot(pca_result, type = "lines", main = "Scree Plot")

# Biplot of PCA
biplot(pca_result, scale = 0)
```
**Key Insights:**
- The **scree plot** shows how much variance each component captures.
- The **biplot** visualizes the principal components with the original feature directions.
- PCA is useful in reducing the number of dimensions while retaining important information.

---

## **2. Feature Selection and Data Compression**  
### **Further Analysis**
- **Feature Selection**: Choosing a subset of relevant features based on statistical significance.
- **Dimensionality Reduction**: Transforming features into a lower-dimensional representation (e.g., PCA, Autoencoders).
- **Compression Example**: PCA can be used for image compression by keeping only the most significant components.

### **Example in R**
Compress an image using PCA:
```r
library(jpeg)

# Read an image
img <- readJPEG("example.jpg")

# Convert image to grayscale
gray_img <- (img[,,1] + img[,,2] + img[,,3]) / 3

# Perform PCA
pca_img <- prcomp(gray_img, center = TRUE, scale = TRUE)

# Reconstruct image using only top components
compressed_img <- pca_img$x[, 1:50] %*% t(pca_img$rotation[, 1:50])

# Plot original and compressed images
par(mfrow = c(1,2))
image(gray_img, col = gray(0:255/255), main = "Original Image")
image(compressed_img, col = gray(0:255/255), main = "Compressed Image")
```
This demonstrates how PCA helps in compressing data while retaining most of the useful information.

---

## **3. Data Visualization and Eigenvectors**  
### **Further Analysis**
- Eigenvectors **represent directions** of maximum variance.
- Eigenvalues **indicate how important** each eigenvector is.
- In PCA, eigenvectors help in transforming data into a new coordinate system.

### **Example in R**
```r
# Compute covariance matrix
cov_matrix <- cov(iris_scaled)

# Compute eigenvectors and eigenvalues
eigen_result <- eigen(cov_matrix)

# Print eigenvalues
print(eigen_result$values)

# Print eigenvectors
print(eigen_result$vectors)
```
This helps understand how PCA selects directions of maximum variance.

---

## **4. Confusion Matrix and Classification Metrics**  
### **Further Analysis**
- **Precision**: \\( TP / (TP + FP) \\) - How many of the predicted positives are actual positives?
- **Recall (Sensitivity)**: \\( TP / (TP + FN) \\) - How many actual positives are correctly predicted?
- **F1-Score**: Harmonic mean of precision and recall.
- **Specificity**: \\( TN / (TN + FP) \\) - How many actual negatives are correctly predicted?

### **Example in R**
Perform classification using a decision tree and compute a confusion matrix:
```r
library(caret)

# Create a binary classification problem
iris$Species <- ifelse(iris$Species == "setosa", "Setosa", "Other")

# Split dataset
set.seed(123)
trainIndex <- createDataPartition(iris$Species, p = 0.7, list = FALSE)
trainData <- iris[trainIndex, ]
testData <- iris[-trainIndex, ]

# Train a model
model <- train(Species ~ ., data = trainData, method = "rpart")

# Make predictions
predictions <- predict(model, testData)

# Compute confusion matrix
confusionMatrix(predictions, testData$Species)
```
This evaluates model performance using **true positives, false positives, etc.**

---

## **5. Gradient Descent and Optimization**  
### **Further Analysis**
- **Gradient Descent** updates parameters iteratively to minimize the error function.
- **Learning Rate**: Determines the step size in each update.
- **Batch Gradient Descent**: Uses the entire dataset in each iteration.
- **Stochastic Gradient Descent (SGD)**: Uses one data point at a time.
- **Mini-batch Gradient Descent**: Uses small batches for optimization.

### **Example in R**
Implement gradient descent for linear regression:
```r
# Generate data
set.seed(123)
x <- rnorm(100)
y <- 3*x + rnorm(100, mean = 0, sd = 0.5)

# Initialize parameters
theta0 <- 0
theta1 <- 0
alpha <- 0.01  # Learning rate
iterations <- 1000

# Gradient descent loop
for (i in 1:iterations) {
  predictions <- theta0 + theta1 * x
  error <- y - predictions
  
  # Compute gradients
  theta0 <- theta0 + alpha * sum(error) / length(y)
  theta1 <- theta1 + alpha * sum(error * x) / length(y)
}

# Print final parameters
print(theta0)
print(theta1)
```
This finds the best-fit line by minimizing the error.

---

## **6. Linear Regression and Least Squares Optimization**  
### **Further Analysis**
- **Linear regression** models the relationship between a dependent variable and independent variables.
- The **least squares method** minimizes the sum of squared differences between actual and predicted values.

### **Example in R**
```r
# Fit linear model
model <- lm(y ~ x)

# Print model summary
summary(model)

# Plot regression line
plot(x, y, main = "Linear Regression", col = "blue", pch = 16)
abline(model, col = "red")
```
This provides the regression coefficients and evaluates model fit.

---

## **7. Hypothesis Testing and Model Evaluation**  
### **Further Analysis**
- **Null Hypothesis (H0)**: No effect or relationship.
- **Alternative Hypothesis (H1)**: There is a significant effect.
- **p-value**: If \( p < 0.05 \), we reject the null hypothesis.
- **t-test**: Used to compare means.

### **Example in R**
Perform a t-test:
```r
t.test(iris$Sepal.Length[iris$Species == "setosa"], 
       iris$Sepal.Length[iris$Species == "versicolor"])
```
This tests if there is a significant difference in Sepal Length between **Setosa and Versicolor** species.

---

## **Final Thoughts**
These examples demonstrate the practical applications of PCA, classification metrics, gradient descent, regression, and hypothesis testing in R. 

