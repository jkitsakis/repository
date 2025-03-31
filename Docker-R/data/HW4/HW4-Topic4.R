# install.packages("arules")
# install.packages("arulesViz")
library(arules)


# Step 1: Load the dataset interactively
dataset <- read.transactions(file.choose(), sep = ",", rm.duplicates = TRUE)

# Step 2: View summary
summary(dataset)

# Step 3: Find 5 most frequent items
item_freq <- itemFrequency(dataset, type = "absolute")
top5_items <- sort(item_freq, decreasing = TRUE)[1:5]
print("Top 5 most frequent items:")
print(top5_items)

# Run Apriori with specified parameters
rules <- apriori(dataset, parameter = list(
  supp = 0.01,
  conf = 0.4,
  minlen = 3
))

# Show summary of rules
summary(rules)

# Compute absolute support count
abs_min_support <- 0.01 * length(dataset)

cat("Model Minimum Length: 3\n")
cat("Maximum Length:", max(size(rules)), "\n")
cat("Absolute Minimum Support Count:", abs_min_support, "\n")
cat("Number of Rules:", length(rules), "\n")

# Plot top 10 frequent items
itemFrequencyPlot(dataset, topN = 10, type = "relative", main = "Relative Item Frequency")

# Install arulesViz for better rule visualization
library(arulesViz)

# Top 10 rules by lift
top10_lift <- sort(rules, by = "lift", decreasing = TRUE)[1:10]
inspect(top10_lift)

# Graph-based visualization (requires RStudio)
plot(top10_lift, method = "graph", engine = "htmlwidget")


