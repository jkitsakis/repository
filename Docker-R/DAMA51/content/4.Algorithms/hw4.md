Title: Topics Analysis from HW4.docx
Slug: hw4
Category_Order: 4
Order: 3
Summary: HW4

The HW4 assignment covers the following topics in **Machine Learning (ML)** and **Data Analysis (DA)**:

1. **Decision Trees (ML)**
  > - Entropy and Information Gain calculations.
  > - Implementation of the ID3 algorithm in R.
  > - Building and visualizing a decision tree from a dataset.

2. **Bayes Classifier (ML)**
  > - Probabilistic calculations for Naïve Bayes classification.
  > - Implementation of a Naïve Bayes classifier in R.
  > - Making predictions for new instances.

3. **Itemset Mining & Association Rules (DA/ML)**
  > - Frequent itemset analysis using the Apriori algorithm.
  > - Generating and analyzing association rules.
  > - Visualizing the rules using lift and network graphs.

4. **Online Quiz**
  > - Likely covering general ML and DA concepts.

5. **Project (Open-ended)**
  > - This could involve applying ML and DA techniques in a practical scenario.

The assignment involves both **theoretical and practical implementation** in **R**, requiring entropy calculations, probability derivations, and coding solutions for decision trees, Naïve Bayes classifiers, and association rule mining. Let me know if you need help with any specific topic!

To systematically approach the HW4 tasks in **R**, we should break them down into **structured steps** per topic. Below is a **topic-wise plan** with the key **methods, functions, and approach** for solving them.

---
### **Structured Approach to Solving DAMA51 HW4 Tasks in R**


## **📌 Topic 2: Decision Trees (ML)**
**Goal:** Build a decision tree for the given dataset, compute entropy, information gain, and implement ID3 algorithm in R.

### **Steps to Follow:**
- **Load Dataset**
  > - Read `Tennis_final.csv` interactively.  
```r
   file_path <- file.choose() 
   data <- read.csv(file_path, header=TRUE, sep=",")
   print(data)
```

- **Compute Entropy**
  > - Define an entropy function using Shannon’s formula.
```r
   Entropy <- function(vls) {
  > res <- vls / sum(vls) * log2(vls / sum(vls))
  > res[vls == 0] <- 0
  > -sum(res)
   }
```

- **Compute Information Gain for Each Attribute**
  > - Define a function to calculate **Information Gain (IG)**.
```r
   InformationGain <- function(table) {
  > table <- as.data.frame.matrix(table)
  > entropyBefore <- Entropy(colSums(table))
  > s <- rowSums(table)
  > entropyAfter <- sum(s / sum(s) * apply(table, 1, Entropy))
  > entropyBefore - entropyAfter
   }
```
   - Compute IG for `Outlook`, `Temperature`, and `Humidity`.

4. **Implement the ID3 Algorithm**
  > - Create recursive decision tree construction.
```r
   TrID3 <- function(node, data) {
  > node$obsCount <- nrow(data)
  > if (IsPure(data)) {
  >   child <- node$AddChild(unique(data[, ncol(data)]))
  >   child$obsCount <- nrow(data)
  > } else {
  >   ig <- sapply(names(data)[-ncol(data)], function(x) 
  >     InformationGain(table(data[, x], data[, ncol(data)])))
  >   feature <- names(ig)[which.max(ig)]
  >   node$feature <- feature
  >   childObs <- split(data[, !(names(data) %in% feature)], data[, feature])
  >   for (i in seq_along(childObs)) {
  >     child <- node$AddChild(names(childObs)[i])
  >     TrID3(child, childObs[[i]])
  >   }
  > }
   }
```

- **Visualize the Decision Tree**
```r
   install.packages("data.tree")
   library(data.tree)
   tree <- Node$new("Play")
   TrID3(tree, data)
   print(tree, "feature", "obsCount")
```

---

## **📌 Topic 3: Bayes Classifier (ML)**
**Goal:** Implement a **Naïve Bayes** classifier in R.

### **Steps to Follow:**
- **Load the dataset**
```r
   file_path <- file.choose()
   data <- read.csv(file_path, header=TRUE, sep=",")
   data <- data[,-1] # Remove 'Day' column
```

- **Install and Load the `naivebayes` Package**
```r
   install.packages("naivebayes")
   library(naivebayes)
```

- **Train the Naïve Bayes Model**
```r
   classifier <- naive_bayes(PlayTennis ~ ., data=data)
```

- **Make Predictions for Test Instances**
```r
   test1 <- data.frame(Outlook="Sunny", Temperature="Mild", Humidity="High", Wind="Strong")
   prediction1 <- predict(classifier, test1, type="prob")
   print(round(prediction1, 3))

   test2 <- data.frame(Outlook="Overcast", Temperature="Mild", Humidity="Normal", Wind="Weak")
   prediction2 <- predict(classifier, test2, type="prob")
   print(round(prediction2, 3))
```

---

## **📌 Topic 4: Itemset Mining & Association Rules (DA)**
**Goal:** Use the Apriori algorithm for **association rule mining**.

### **Steps to Follow:**  
- **Install and Load Necessary Libraries**  

```r
   install.packages("arules")
   install.packages("arulesViz")
   library(arules)
   library(arulesViz)
```  

- **Load the Transaction Data**  

```r
   dataset <- read.transactions(file.choose(), sep=",", rm.duplicates=TRUE)
```

- **Find the Top 5 Most Frequent Items**  

```r
   itemFrequencyPlot(dataset, topN=5)
```

- **Run the Apriori Algorithm**  

```r
   rules <- apriori(dataset, 
  >   >   >   > parameter=list(supp=0.01, conf=0.4, minlen=3))
```

- **Extract Model Parameters**  

```r
   summary(rules)
```

- **Visualize the Rules**  

```r
   inspect(head(sort(rules, by="lift"), 10))
   plot(rules, method="graph", engine="htmlwidget")
```

- **Find the Best-Selling Product**  

```r
   itemFrequencyPlot(dataset, topN=1, col="blue", main="Best-Selling Product")
```  

---

## **📌 Topic 5: Project**  

**Goal:** Special track – may involve a mix of decision trees, Bayes classification, and association rules.

**Suggested Approach:**  
1. **Identify the problem statement** (e.g., predicting customer purchases, optimizing marketing strategies).  
2. **Prepare and clean data** (handle missing values, categorical encoding).  
3. **Choose the right ML technique** (Decision Trees for classification, Bayes for probabilistic modeling, Apriori for recommendations).  
4. **Implement and evaluate the model** (use cross-validation, accuracy metrics).  
5. **Summarize findings and conclusions**.  

---

## **✅ Summary of R Packages & Functions Used**
| Task | Package | Key Functions |
|------|---------|--------------|
| Decision Trees | `data.tree` | `Entropy()`, `InformationGain()`, `TrID3()` |
| Naïve Bayes | `naivebayes` | `naive_bayes()`, `predict()` |
| Association Rules | `arules`, `arulesViz` | `apriori()`, `inspect()`, `itemFrequencyPlot()`, `plot()` |

This **structured approach** ensures **step-by-step completion** of HW4 tasks while maintaining best practices in R. Let me know if you need any **code explanations or modifications!** 🚀