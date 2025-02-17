# Load the dataset using read.csv and file.choose
data <- read.csv(file.choose(), header = TRUE)

# Inspect the structure of the dataset
str(data)

# Exclude the first two columns (ID and diagnosis) and create data_clean
data_clean <- data[, -c(1, 2)]

# Check the number of features in data_clean
num_features <- ncol(data_clean)
cat("Number of features in data_clean:", num_features, "\n")

# Min-Max normalization function
min_max_normalize <- function(x) {
  return((x - min(x)) / (max(x) - min(x)))
}

# Apply Min-Max normalization to each column of data_clean
scaled_data <- as.data.frame(lapply(data_clean, min_max_normalize))

# Convert scaled_data to a matrix for easier handling
scaled_data_matrix <- as.matrix(scaled_data)

# Check and replace any NA/NaN/Inf values with 0
scaled_data_matrix[is.na(scaled_data_matrix)] <- 0
scaled_data_matrix[is.nan(scaled_data_matrix)] <- 0
scaled_data_matrix[is.infinite(scaled_data_matrix)] <- 0

# Remove constant columns (where all values are the same)
scaled_data_clean <- scaled_data_matrix[, apply(scaled_data_matrix, 2, function(col) length(unique(col)) > 1)]

# Compute the correlation matrix of scaled_data_clean
cor_matrix <- cor(scaled_data_clean)

# Check for NA/NaN/Inf in the correlation matrix
if(any(is.na(cor_matrix)) | any(is.nan(cor_matrix)) | any(is.infinite(cor_matrix))) {
  cat("There are NA/NaN/Inf values in the correlation matrix.\n")
} else {
  cat("Correlation matrix is clean.\n")
}

# Plot the correlation matrix as a heatmap using base R
heatmap(cor_matrix, 
        main = "Correlation Matrix Heatmap",
        scale = "none", 
        margins = c(10, 10))


#b
# Assuming 'scaled_data_clean' is the data we are working with
wcss <- numeric(10)  # To store WCSS values for k = 1 to 10

# Run k-means clustering for k = 1 to 10 and calculate WCSS
for (k in 1:10) {
  kmeans_model <- kmeans(scaled_data_clean, centers = k, nstart = 25)
  wcss[k] <- kmeans_model$tot.withinss  # Total within-cluster sum of squares
}

# Plot WCSS vs k . type = "b" : both points and lines are plotted.
plot(1:10, wcss, type = "b", main = "WCSS vs K", xlab = "Number of Clusters (k)", ylab = "WCSS", pch = 19, col = "blue")


#c
# Apply K-Means with k = 5
set.seed(123)  # Set a random seed for reproducibility
kmeans_model <- kmeans(scaled_data_clean, centers = 5, nstart = 10)  # k = 5 clusters

# Report Cluster Size
cluster_size <- table(kmeans_model$cluster)  # Get the size of each cluster

# Print the result as a table
print(cluster_size)


#d 

# Perform PCA
pca_result <- prcomp(scaled_data_clean, center = TRUE, scale. = TRUE)  # Apply PCA to scaled data
pca_data <- as.data.frame(pca_result$x[, 1:2])  # Use the first 2 principal components

# Apply K-Means on PCA-reduced data
set.seed(456)  # Set a random seed for reproducibility
pca_kmeans <- kmeans(pca_data, centers = 5, nstart = 10)  # Apply k-means with k = 5

# Plot the clusters on the first 2 principal components
plot(pca_data$PC1, pca_data$PC2, col = pca_kmeans$cluster, pch = 20, cex = 2, 
     main = "PCA Clusters (k = 5)", xlab = "Principal Component 1", ylab = "Principal Component 2")

