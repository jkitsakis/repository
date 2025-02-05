# load and read data 
data  <- read.csv("datasets//data.csv", header = TRUE, sep = ",")

# Inspect the structure of the dataset
str(data)

# Exclude the first two columns (ID and diagnosis)
data_clean <- data[, -c(1, 2)]

# Ensure all columns are numeric (or convert if necessary)
data_clean[] <- lapply(data_clean, as.numeric)

# Check the number of rows and columns after cleaning
cat("Rows in data_clean after conversion:", nrow(data_clean), "\n")
cat("Columns in data_clean:", ncol(data_clean), "\n")


# Check how many rows remain after cleaning
cat("Rows in data_clean after removing incomplete cases:", nrow(data_clean), "\n")

# If there are fewer than 2 rows, clustering will not work
if (nrow(data_clean) < 2) {
  stop("Not enough data for clustering! The dataset has fewer than 2 observations.")
}

# Min-max normalization (scaling all columns)
scaled_data <- as.data.frame(lapply(data_clean, function(x) (x - min(x)) / (max(x) - min(x))))

# Check the number of rows in the scaled data
cat("Rows in scaled_data after normalization:", nrow(scaled_data), "\n")

# Compute the dissimilarity matrix using Euclidean distance
dist_matrix <- dist(scaled_data)

# Perform hierarchical clustering
hc_single <- hclust(dist_matrix, method = "single")
hc_complete <- hclust(dist_matrix, method = "complete")

# Plot the dendrograms for both methods
par(mfrow = c(1, 2))  # Plot side by side
plot(hc_single, main = "Single Linkage Dendrogram")
plot(hc_complete, main = "Complete Linkage Dendrogram")
