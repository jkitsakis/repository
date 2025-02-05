# Load the mtcars dataset
data(mtcars)

# Standardize the data (Z-score normalization)
mtcars_scaled <- scale(mtcars)

# Compute the pairwise dissimilarity matrix using Euclidean distance
dissimilarity_matrix <- dist(mtcars_scaled, method = "euclidean")

# Convert the dissimilarity matrix into a matrix form for easier access
dissimilarity_matrix <- as.matrix(dissimilarity_matrix)

# Get the row number for Mazda RX4 and all Merc 450 cars
mazda_rx4_index <- which(rownames(mtcars) == "Mazda RX4")
merc_450se_index <- which(rownames(mtcars) == "Merc 450SE")
merc_450sl_index <- which(rownames(mtcars) == "Merc 450SL")
merc_450slc_index <- which(rownames(mtcars) == "Merc 450SLC")

# Extract the dissimilarities between Mazda RX4 and all Merc 450 cars
dissimilarity_mazda_merc <- c(
  Mazda_RX4_Merc_450SE = dissimilarity_matrix[mazda_rx4_index, merc_450se_index],
  Mazda_RX4_Merc_450SL = dissimilarity_matrix[mazda_rx4_index, merc_450sl_index],
  Mazda_RX4_Merc_450SLC = dissimilarity_matrix[mazda_rx4_index, merc_450slc_index]
)

# Print the dissimilarities
print(dissimilarity_mazda_merc)

#-- b --#
# Standardize the data (Z-score normalization)
mtcars_scaled <- scale(mtcars)

# Compute the dissimilarity matrix using Euclidean distance
dissimilarity_matrix <- dist(mtcars_scaled, method = "euclidean")

# Perform hierarchical clustering with single linkage
hc_single <- hclust(dissimilarity_matrix, method = "single")

# Plot the dendrogram for single linkage
plot(hc_single, main = "Dendrogram (Single Linkage)", xlab = "", sub = "", cex = 0.8)

# Perform hierarchical clustering with complete linkage
hc_complete <- hclust(dissimilarity_matrix, method = "complete")

# Plot the dendrogram for complete linkage
plot(hc_complete, main = "Dendrogram (Complete Linkage)", xlab = "", sub = "", cex = 0.8)


#-- c --#
# Perform hierarchical clustering with single linkage (already done)
# Cut the single linkage dendrogram into 4 clusters
clusters_single <- cutree(hc_single, k = 4)

# Perform hierarchical clustering with complete linkage (already done)
# Cut the complete linkage dendrogram into 4 clusters
clusters_complete <- cutree(hc_complete, k = 4)

# Count the number of observations in each cluster for single linkage
table_single <- table(clusters_single)

# Count the number of observations in each cluster for complete linkage
table_complete <- table(clusters_complete)

# Print the results for single linkage
cat("Single Linkage Cluster Counts:\n")
print(table_single)

# Print the results for complete linkage
cat("\nComplete Linkage Cluster Counts:\n")
print(table_complete)

#-- d --#
# Assuming you have already run the clustering for both linkage methods
# Extract the clusters for single linkage
clusters_single <- cutree(hc_single, k = 4)

# Extract the data for clusters 1 and 3
cluster_1_data <- mtcars[clusters_single == 1, c("cyl", "hp")]
cluster_3_data <- mtcars[clusters_single == 3, c("cyl", "hp")]

# Calculate the mean of 'cyl' and 'hp' for cluster 1
mean_cluster_1 <- colMeans(cluster_1_data)

# Calculate the mean of 'cyl' and 'hp' for cluster 3
mean_cluster_3 <- colMeans(cluster_3_data)

# Print the results
cat("Mean values for Cluster 1:\n")
print(mean_cluster_1)

cat("\nMean values for Cluster 3:\n")
print(mean_cluster_3)


