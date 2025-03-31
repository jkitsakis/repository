# install.packages("arules")
# install.packages("arulesViz")
library(arules)
dataset <- read.transactions(file.choose(), sep = ",", rm.duplicates = TRUE)
summary(dataset)

#  5 most frequent items
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

summary(rules)

# absolute support count
abs_min_support <- 0.01 * length(dataset)

cat("Model Minimum Length: 3\n")
cat("Maximum Length:", max(size(rules)), "\n")
cat("Absolute Minimum Support Count:", abs_min_support, "\n")
cat("Number of Rules:", length(rules), "\n")

# Plot top 5 frequent items
itemFrequencyPlot(dataset, topN = 5, type = "relative", main = "Relative Item Frequency")

library(arulesViz)
# Top 10 rules
top10_lift <- sort(rules, by = "lift", decreasing = TRUE)[1:10]
inspect(top10_lift)

plot(top10_lift, method = "graph", engine = "htmlwidget")


