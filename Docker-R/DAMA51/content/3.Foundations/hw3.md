Title: Topics Analysis from HW3.docx
Slug: hw3
Category_Order: 3
Order: 3
Summary: HW3

Based on the provided document, the following topics in **Machine Learning (ML)** and **Data Analysis (DA)** are covered in **Homework 3**. These topics collectively provide a solid foundation in ML and DA, covering both **supervised** and **unsupervised** learning techniques along with key **data preprocessing and exploratory analysis** methods.:

### **Machine Learning Topics:**
1. **Feature Selection & Linear Regression** (Supervised Learning)
     - Correlation analysis for feature selection
     - Building and evaluating a linear regression model (R-squared, MAE)
     - Standardization (Z-score normalization)
     - Model predictions and de-normalization

2. **Hierarchical Clustering** (Unsupervised Learning)
     - Distance calculations (Euclidean distance)
     - Single and complete linkage methods
     - Dendrogram visualization
     - Cluster analysis (cutting dendrograms and analyzing cluster properties)

3. **Prototype-based and K-Means Clustering** (Unsupervised Learning)
     - Min-max normalization
     - Elbow method for optimal k determination
     - Applying k-means clustering
     - Principal Component Analysis (PCA) for dimensionality reduction before clustering
     - Visualization of clusters after PCA transformation

4. **Association Rule Mining** (Unsupervised Learning)
     - Frequent itemset mining using the Apriori algorithm
     - Extracting and ranking association rules based on lift
     - Visualizing association rules

### **Data Analysis Topics:**
1. **Exploratory Data Analysis (EDA)**
     - Reading and preprocessing datasets
     - Handling categorical and numeric variables
     - Calculating correlations and statistical summaries

2. **Data Standardization & Normalization**
     - Z-score standardization
     - Min-max normalization

3. **Data Visualization**
     - Heatmaps for correlation matrices
     - Dendrograms for hierarchical clustering
     - Bar charts and scatter plots for regression analysis
     - Graph-based visualization of association rules

4. **Distance Metrics & Similarity Analysis**
     - Pairwise dissimilarity calculations in hierarchical clustering


### **Structured Approach to Solving Each Task in R (Per Topic)**

Below is a step-by-step structured approach for each topic in **DAMA51 Homework 3**, including the necessary R functions and key implementation details.

---

## **Topic 2: Feature Selection & Linear Regression**
### **Step 1: Load and Preprocess Data**
```r
# Load dataset interactively
housing_data <- read.csv(file.choose())

# Select only numeric variables
house_prices_numeric <- housing_data[, sapply(housing_data, is.numeric)]

# Standardize data (Z-score normalization)
house_prices_scaled <- scale(house_prices_numeric)

# Compute correlation matrix
cor_matrix <- cor(house_prices_scaled)

# Display correlation matrix
print(cor_matrix)
```

### **Step 2: Feature Selection**
```r
# Compute correlation with price
cor_price <- cor_matrix[,"price"]

# Rank features by absolute correlation with price
selected_features <- names(sort(abs(cor_price), decreasing = TRUE))[2:4]

# Barplot for top 3 correlated features
barplot(sort(abs(cor_price[selected_features]), decreasing = TRUE),
        main="Top 3 Features Correlated with Price",
        col="steelblue")
```

### **Step 3: Train Linear Regression Model**
```r
# Build regression model using selected features
lm_model <- lm(price ~ ., data = house_prices_scaled[, c(selected_features, "price")])

# Model summary
summary(lm_model)

# R-squared value
r_squared <- summary(lm_model)$r.squared

# Compute Mean Absolute Error (MAE)
predictions <- predict(lm_model, newdata = house_prices_scaled)
mae <- mean(abs(predictions - house_prices_scaled$price))

print(paste("R-squared:", round(r_squared, 3)))
print(paste("MAE:", round(mae, 3)))
```

### **Step 4: De-normalization & Visualization**
```r
# Retrieve original mean and SD for de-normalization
price_mean <- mean(housing_data$price, na.rm = TRUE)
price_sd <- sd(housing_data$price, na.rm = TRUE)

# De-normalize predictions
denormalized_predictions <- (predictions * price_sd) + price_mean

# Scatter plot of predicted vs actual
plot(denormalized_predictions, housing_data$price, 
     main="Predicted vs Actual Prices", xlab="Predicted", ylab="Actual",
     col="blue", pch=19)
abline(0,1, col="red", lwd=2)
```

---

## **Topic 3: Hierarchical Clustering**
### **Step 1: Load Data & Compute Dissimilarity Matrix**
```r
# Load dataset
data(mtcars)

# Standardize data
mtcars_scaled <- scale(mtcars)

# Compute Euclidean distance
dist_matrix <- dist(mtcars_scaled, method = "euclidean")

# Display distances between Mazda RX4 and Merc 450 cars
subset(as.matrix(dist_matrix), rownames(as.matrix(dist_matrix)) == "Mazda RX4",
       colnames(as.matrix(dist_matrix)) %in% c("Merc 450SE", "Merc 450SL", "Merc 450SLC"))
```

### **Step 2: Hierarchical Clustering**
```r
# Perform clustering
hc_single <- hclust(dist_matrix, method = "single")
hc_complete <- hclust(dist_matrix, method = "complete")

# Plot dendrograms
plot(hc_single, main="Single Linkage Clustering")
plot(hc_complete, main="Complete Linkage Clustering")
```

### **Step 3: Cluster Analysis**
```r
# Cut dendrogram into 4 clusters
clusters_single <- cutree(hc_single, k=4)
clusters_complete <- cutree(hc_complete, k=4)

# Count observations per cluster
table(clusters_single)
table(clusters_complete)

# Compute means of 'cyl' and 'hp' for Clusters 1 and 3
aggregate(mtcars[,c("cyl","hp")], by=list(Cluster=clusters_single), mean)
```

---

## **Topic 4: Prototype-based and k-means Clustering**
### **Step 1: Load & Normalize Data**
```r
# Load dataset
cancer_data <- read.csv(file.choose())

# Drop ID and diagnosis columns
data_clean <- cancer_data[, -c(1,2)]

# Min-max normalization
scaled_data <- as.data.frame(lapply(data_clean, function(x) (x - min(x)) / (max(x) - min(x))))
```

### **Step 2: Determine Optimal k (Elbow Method)**
```r
# Compute Within-Cluster Sum of Squares (WCSS)
wcss <- sapply(1:10, function(k) kmeans(scaled_data, centers=k, nstart=10)$tot.withinss)

# Plot Elbow Curve
plot(1:10, wcss, type="b", pch=19, frame=FALSE,
     main="Elbow Method for Optimal k", xlab="Number of clusters", ylab="WCSS")
```

### **Step 3: Apply K-Means Clustering**
```r
# Apply k-means with k=5
set.seed(123)
kmeans_model <- kmeans(scaled_data, centers=5, nstart=10)

# Cluster sizes
table(kmeans_model$cluster)
```

### **Step 4: PCA for Dimensionality Reduction**
```r
# Perform PCA
pca_result <- prcomp(scaled_data, center=TRUE, scale.=TRUE)

# Use first 2 principal components
pca_data <- as.data.frame(pca_result$x[,1:2])

# Apply K-means on PCA data
pca_kmeans <- kmeans(pca_data, centers=5, nstart=10)

# Plot clusters
library(ggplot2)
ggplot(pca_data, aes(x=PC1, y=PC2, color=factor(pca_kmeans$cluster))) +
  geom_point(size=3) +
  labs(title="PCA-Based Clustering", color="Cluster")
```

---

## **Topic 5: Association Rules (Itemset Mining)**
### **Step 1: Load Data & Perform Initial Analysis**
```r
# Load required library
library(arules)

# Load dataset
data("Groceries")

# Summary statistics
summary(Groceries)

# Display top 5 most frequent items
itemFrequencyPlot(Groceries, topN=5, col="steelblue")
```

### **Step 2: Apply Apriori Algorithm**
```r
# Apply Apriori algorithm with minimum support of 0.01
frequent_itemsets <- apriori(Groceries, parameter = list(supp=0.01, target="frequent itemsets"))

# Display top 5 frequent itemsets
inspect(head(sort(frequent_itemsets, by="support"), 5))
```

### **Step 3: Generate & Visualize Association Rules**
```r
# Generate rules with min confidence 0.5 and min support 0.01
rules <- apriori(Groceries, parameter = list(supp=0.01, conf=0.5, target="rules"))

# Display top 5 rules sorted by lift
inspect(head(sort(rules, by="lift"), 5))

# Visualize rules
library(arulesViz)
plot(rules, method="graph", control=list(type="items"))
```

---

### **Final Thoughts**  
This structured approach ensures:  
1. **Consistency:** All tasks follow a **logical flow** from **loading data** to **modeling and evaluation**.  
2. **Modularity:** Each step can be run **independently** and **modified** if needed.  
3. **Visualization & Interpretation:** Key **plots and tables** are included for better insights.  
