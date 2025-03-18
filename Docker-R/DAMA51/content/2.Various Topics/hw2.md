Title: Topics Analysis from HW2.docx
Slug: hw2
Category_Order: 2
Order: 3
Summary: HW2

The topics covered in the **DAMA51 Homework 2** assignment from the **Hellenic Open University** include the following **Machine Learning (ML)** and **Data Analysis (DA)** concepts:

### **Machine Learning (ML) Topics:**
1. **Principal Component Analysis (PCA)**
     - Standardization (Z-score)
     - Variance explained by principal components
     - Scree plot and scatter plots of principal components

2. **Confusion Matrix and ROC Curve**
     - Classification threshold selection
     - Calculating confusion matrix, recall, precision, and accuracy
     - Computing True Positive Rate (TPR) & False Positive Rate (FPR) for different thresholds
     - Creating an ROC curve

3. **Gradient Descent for Linear Regression**
     - Implementing gradient descent from scratch
     - Using Sum of Squared Errors (SSE) as the cost function
     - Updating slope and intercept using gradient updates
     - Visualizing best-fit line for different iterations

### **Data Analysis (DA) Topics:**
1. **Hypothesis Testing**
     - Conducting a **t-test** on the PlantGrowth dataset
     - Performing a **Chi-Square Test of Independence** on customer satisfaction data

2. **Linear Regression**
     - Building a linear model using `lm()` in R
     - Predicting population values using the model
     - Calculating Mean Squared Error (MSE)
     - Visualizing the regression line with a scatter plot

This assignment focuses heavily on **statistical analysis**, **dimensionality reduction**, **classification metrics**, and **machine learning model training** using **R**.

--- 

### **Structured Approach to Solving DAMA51 HW2 Tasks in R**

Below is a structured approach to systematically tackle each topic in R.

---

## **📌 Topic 2: Principal Component Analysis (PCA)**  
**Steps:**
1. **Load and Clean Data**
   - Read CSV file (`read.csv`)
   - Remove ID column
   - Handle missing values (e.g., `na.omit()`, `mean imputation`)

2. **Compute Summary Statistics**
   - Calculate mean (`mean()`) and standard deviation (`sd()`) for each column.

3. **Standardize Data**
   - Use `scale()` function for Z-score normalization.

4. **Perform PCA**
   - Use `prcomp()` function to extract principal components.
   - Compute variance explained by each component.

5. **Visualizations**
   - **Scree Plot:** Use `barplot()` or `ggplot2` to visualize variance explained.
   - **Scatter Plot:** Use `ggplot2` to plot first 2 and first 3 principal components.

**R Code Template:**
```r
# Load Data
water_data <- read.csv(file.choose())  # Choose the dataset file interactively
water_data_noid <- water_data[,-1]  # Remove ID column

# Summary statistics
summary(water_data_noid)
sapply(water_data_noid, mean, na.rm=TRUE)
sapply(water_data_noid, sd, na.rm=TRUE)

# Standardization
scaled_data <- scale(water_data_noid)

# Perform PCA
pca_result <- prcomp(scaled_data, center = TRUE, scale. = TRUE)
summary(pca_result)

# Scree Plot
variance_explained <- pca_result$sdev^2 / sum(pca_result$sdev^2)
barplot(variance_explained, main="Scree Plot", xlab="Principal Component", ylab="Variance Explained")

# Scatter Plot of First 2 Components
library(ggplot2)
pca_df <- data.frame(pca_result$x[,1:3])
ggplot(pca_df, aes(x=PC1, y=PC2)) + geom_point() + theme_minimal() + ggtitle("PCA Scatter Plot (PC1 vs PC2)")
```

---

## **📌 Topic 3: Confusion Matrix and ROC Curve**  
**Steps:**
1. **Load Data**
   - Read CSV file (`read.csv`).

2. **Construct Confusion Matrix**
   - Classify based on threshold (0.65) using `ifelse()`.
   - Use `table()` to create a confusion matrix.

3. **Compute Performance Metrics**
   - Calculate **recall, precision, and accuracy** using:
     - `TPR = TP / (TP + FN)`
     - `FPR = FP / (FP + TN)`
     - `Accuracy = (TP + TN) / (TP + FP + TN + FN)`

4. **Vary Threshold and Compute TPR, FPR**
   - Loop through different thresholds (0.25, 0.5, 0.75) and compute confusion matrices.

5. **Plot ROC Curve**
   - Compute ROC points for multiple thresholds.
   - Use `ggplot2` to visualize.

**R Code Template:**
```r
# Load Data
eye_data <- read.csv(file.choose(), sep=";")

# Define Threshold
threshold <- 0.65
eye_data$predicted_class <- ifelse(eye_data$UseOfGlassesPredicted >= threshold, 1, 0)

# Confusion Matrix
conf_matrix <- table(eye_data$predicted_class, eye_data$UseOfGlassesActual)
print(conf_matrix)

# Compute Performance Metrics
TP <- conf_matrix[2,2]
FP <- conf_matrix[2,1]
FN <- conf_matrix[1,2]
TN <- conf_matrix[1,1]

recall <- TP / (TP + FN)
precision <- TP / (TP + FP)
accuracy <- (TP + TN) / sum(conf_matrix)

cat("Recall:", recall, "\nPrecision:", precision, "\nAccuracy:", accuracy, "\n")

# ROC Curve Calculation
library(pROC)
roc_curve <- roc(eye_data$UseOfGlassesActual, eye_data$UseOfGlassesPredicted)
plot(roc_curve, col="blue", main="ROC Curve")
```

---

## **📌 Topic 4: Hypothesis Testing & Gradient Descent**  
### **4A: T-Test on PlantGrowth Dataset**
1. Load dataset (`PlantGrowth`).
2. Split data into control and treatment groups.
3. Perform t-test (`t.test()`).
4. Interpret p-value.

**R Code:**
```r
# Load dataset
data("PlantGrowth")

# Subset Treatment 2
treatment2 <- subset(PlantGrowth, group == "trt2")

# T-Test
t_test_result <- t.test(treatment2$weight, mu=mean(PlantGrowth$weight))
print(t_test_result)
```

### **4B: Chi-Square Test on Customer Satisfaction**
1. Create contingency table.
2. Perform chi-square test (`chisq.test()`).
3. Interpret p-value.

**R Code:**
```r
# Create Contingency Table
contract_table <- matrix(c(109,141,94,180), nrow=2, byrow=TRUE)
colnames(contract_table) <- c("Satisfied", "Unsatisfied")
rownames(contract_table) <- c("Stable", "Dynamic")
contract_table <- as.table(contract_table)

# Perform Chi-Square Test
chi_test <- chisq.test(contract_table)
print(chi_test)
```

### **4C: Linear Regression on longley Dataset**
1. Load `longley` dataset.
2. Fit linear regression (`lm()`).
3. Compute MSE (`mean()`).
4. Predict population for future years.
5. Plot regression line.

**R Code:**
```r
# Load dataset
data("longley")

# Linear Regression Model
model <- lm(Population ~ Year, data=longley)
summary(model)

# Compute MSE
preds <- predict(model, longley)
mse <- mean((longley$Population - preds)^2)
cat("MSE:", mse, "\n")

# Predict Population for 1963-1967
new_years <- data.frame(Year=1963:1967)
predicted_population <- predict(model, new_years)
print(predicted_population)

# Scatter Plot + Regression Line
ggplot(longley, aes(x=Year, y=Population)) +
  geom_point() +
  geom_smooth(method="lm", se=FALSE, col="red") +
  theme_minimal()
```

### **4D: Gradient Descent for Linear Regression**
1. Implement gradient descent algorithm.
2. Update parameters using learning rate.
3. Plot cost reduction.

**R Code:**
```r
# Gradient Descent Function
LR_GradientDescent <- function(xx, yy, r, m, b, N) {
  n <- length(xx)
  for (i in 1:N) {
    y_pred <- m * xx + b
    grad_m <- -sum((yy - y_pred) * xx) / n
    grad_b <- -sum(yy - y_pred) / n
    m <- m - r * grad_m
    b <- b - r * grad_b
    cost <- sum((yy - y_pred)^2) / 2
    cat("Iteration:", i, " Cost:", round(cost,3), " Slope:", round(m,3), " Intercept:", round(b,3), "\n")
  }
  return(list("slope" = m, "intercept" = b))
}

# Load Dataset
x_data <- longley$Year
y_data <- longley$GNP
xx <- scale(x_data)
yy <- scale(y_data)

# Apply Gradient Descent
lr_gd <- LR_GradientDescent(xx, yy, 0.01, 1, 1, 50)

# Plot Regression Line
ggplot(longley, aes(x=Year, y=GNP)) +
  geom_point() +
  geom_abline(slope=lr_gd$slope, intercept=lr_gd$intercept, col="blue")
```

---

### **🚀 Summary**   
- **PCA:** `prcomp()`, scree plots, variance analysis.  
- **Classification:** Confusion matrix, ROC curves, thresholding.  
- **Statistical Tests:** T-test, chi-square test.   
- **Regression:** Linear model, MSE, predictions.  
- **Gradient Descent:** Implementing from scratch.  

