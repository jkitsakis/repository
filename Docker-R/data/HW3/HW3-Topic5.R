# Install the arules package (if not installed already)
#install.packages("arules")
#install.packages("arulesViz")

# Load the arules package
library(arules)

# Load the Groceries dataset
data("Groceries")

# Summarize the dataset to answer the questions
summary(Groceries)

# Apply the Apriori algorithm with minimum support of 0.01
frequent_itemsets <- apriori(Groceries, parameter = list(support = 0.01, confidence = 0.5))

# Display the top-5 frequent itemsets
inspect(head(frequent_itemsets, 5))

# Generate association rules with minimum support of 0.01 and minimum confidence of 0.5
rules <- apriori(Groceries, parameter = list(support = 0.01, confidence = 0.5))

# Sort the rules by lift in descending order
rules_sorted <- sort(rules, by = "lift", decreasing = TRUE)

# Display the top-5 rules
inspect(head(rules_sorted, 5))

library(arulesViz)
plot(head(rules_sorted, 5), method = "graph")
