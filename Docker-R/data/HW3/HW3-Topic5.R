# Install the arules package (if not installed already)
#install.packages("arules")
#install.packages("arulesViz")

# Load the arules package
library(arules)

data("Groceries")
# summarize Groceries 
summary(Groceries)

# apply the Apriori algorithm 
frequent_itemsets <- apriori(Groceries, parameter = list(support = 0.01, confidence = 0.5))
# top-5 frequent itemsets
inspect(head(frequent_itemsets, 5))

# rules with minimum support of 0.01 and minimum confidence of 0.5
rules <- apriori(Groceries, parameter = list(support = 0.01, confidence = 0.5))
# sort the rules
rules_sorted <- sort(rules, by = "lift", decreasing = TRUE)
# top-5 rules
inspect(head(rules_sorted, 5))
library(arulesViz)
plot(head(rules_sorted, 5), method = "graph")
