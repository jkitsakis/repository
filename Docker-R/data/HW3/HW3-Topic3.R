data(mtcars)

# standardize the data (z-score)
mtcars_scaled <- scale(mtcars)

# compute the pairwise dissimilarity matrix using Euclidean distance
dissimilarity <- dist(mtcars_scaled, method = "euclidean")

#dissimilarity matrix into a matrix to find where the models are
dissimilarity_matrix <- as.matrix(dissimilarity)
dissimilarity_matrix

# row number for Mazda RX4 and all Mercedeses
mazda_rx4_index <- which(rownames(mtcars) == "Mazda RX4")
merc_450se_index <- which(rownames(mtcars) == "Merc 450SE")
merc_450sl_index <- which(rownames(mtcars) == "Merc 450SL")
merc_450slc_index <- which(rownames(mtcars) == "Merc 450SLC")

# dissimilarities for Mazda RX4 and all Mercedeses
dissimilarity_mazda_merc <- c(
  Mazda_RX4_Merc_450SE = dissimilarity_matrix[mazda_rx4_index, merc_450se_index],
  Mazda_RX4_Merc_450SL = dissimilarity_matrix[mazda_rx4_index, merc_450sl_index],
  Mazda_RX4_Merc_450SLC = dissimilarity_matrix[mazda_rx4_index, merc_450slc_index]
)

# Print the dissimilarities
print(dissimilarity_mazda_merc)

#-- b --#

# single linkage
hc_single <- hclust(dissimilarity, method = "single")
# plot single linkage
plot(hc_single, main = "Dendrogram (Single Linkage)", xlab = "", sub = "", cex = 0.8)

# complete linkage
hc_complete <- hclust(dissimilarity, method = "complete")
# plot complete linkage
plot(hc_complete, main = "Dendrogram (Complete Linkage)", xlab = "", sub = "", cex = 0.8)


#-- c --#
# cut the single and complete linkage dendograms into 4 clusters 
clusters_single <- cutree(hc_single, k = 4)
clusters_complete <- cutree(hc_complete, k = 4)

# number of observations for single linkage
table_single <- table(clusters_single)
print(table_single)
# number of observations for complete linkage
table_complete <- table(clusters_complete)
print(table_complete)


#-- d --#
# extract the data calculate the mean of 'cyl' and 'hp'for clusters 1 
cluster_1_data <- mtcars[clusters_single == 1, c("cyl", "hp")]
mean_cluster_1 <- colMeans(cluster_1_data)
mean_cluster_1
# extract the data calculate the mean of 'cyl' and 'hp'for clusters 3 
cluster_3_data <- mtcars[clusters_single == 3, c("cyl", "hp")]
mean_cluster_3 <- colMeans(cluster_3_data)
mean_cluster_3


