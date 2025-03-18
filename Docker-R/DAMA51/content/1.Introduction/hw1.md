Title: Topics Analysis from HW1.docx
Slug: hw1
Category_Order: 1
Order: 3
Summary: HW1

Based on the provided document, **HW1** in the **DAMA51** course covers the following **Machine Learning (ML) and Data Analysis (DA)** topics:

### **Data Analysis (DA) Topics:**
1. **Tabular and Graphical Representations**
     - Dataset inspection using `str()` and `head()`
     - Creating contingency tables (absolute frequency tables)
     - Bar charts for categorical variables
     - Pie charts for categorical data distribution
     - Box plots for age distribution analysis

2. **Correlation Analysis**
     - Computing correlation matrices using Pearson’s correlation coefficient
     - Visualizing correlation using heatmaps
     - Extracting specific correlation values between variables
     - Interpreting scatter plots for correlation strength

3. **Data Frames and Data Manipulation**
     - Handling and transforming datasets in **R**
     - Removing unnecessary attributes
     - Setting row names and filtering data based on conditions
     - Aggregation and computation of statistics (mean, median)
     - Normalization using the **Min-Max** formula
     - Creating new attributes and deriving performance metrics
     - Categorizing data using ordinal classification

### **Machine Learning (ML) Topics:**
1. **Feature Engineering**
     - Normalizing attributes (Min-Max scaling)
     - Creating new features based on derived formulas (Performance metric)
     - Categorizing data using manually defined rules (`Weak`, `Normal`, `Strong` grades)

2. **Exploratory Data Analysis (EDA)**
     - Understanding dataset structures
     - Identifying variable distributions
     - Identifying relationships between features
     - Detecting patterns in data using visualization techniques (scatter plots, heatmaps)  

### **Key Datasets Used:**  
- **Disease Symptoms and Patient Profile Dataset** (Health-related data analysis)  
- **Student Performance Factors Dataset** (Education-related feature analysis)  
- **PokeDex Dataset** (Game-related dataset for practice with data frames)  

---

## Here is a structured **step-by-step approach** to solving each topic using **R**:

### **Topic 2: Tabular and Graphical Representations**  

### **Dataset: Disease Symptoms and Patient Profile Dataset**  
 
**Steps:**  

- **Load the dataset**  

```r
   dataset <- read.csv("path_to_file.csv", stringsAsFactors = TRUE)
```  

- **Inspect the dataset**  

```r
   str(dataset)   # Check structure
   head(dataset)  # View first few rows
```

- **Retrieve specific values**  

```r
   nrow(dataset)  # Number of records
   length(which(sapply(dataset, is.numeric)))  # Count numeric attributes
   dataset$Disease[3]  # Get "Disease" value for the 3rd record
```

- **Create a contingency table for Fever & Cough**  

```r
   table_FC <- table(dataset$Fever, dataset$Cough)
   addmargins(table_FC)  # Include row/column sums
```
- **Bar chart for Fatigue symptom frequency**  

```r
   library(ggplot2)
   ggplot(dataset, aes(x = Fatigue)) +
     geom_bar(fill = "blue") +
     labs(title = "Fatigue Symptom Frequency")
```

- **Pie chart for Cholesterol Levels**  

```r
   cholesterol_table <- table(dataset$Cholesterol_Level)
   pie(cholesterol_table, main = "Cholesterol Level Distribution")
```

- **Box plots for age distribution across diseases**  
```r
   ggplot(dataset, aes(x = Disease, y = Age)) +
     geom_boxplot() +
     theme(axis.text.x = element_text(angle = 90, hjust = 1))
```

---

## **Topic 3: Correlation**
### **Dataset: Student Performance Factors**
📌 **Steps:**  

- **Load the dataset**  
```r
   student_data <- read.csv("path_to_file.csv", stringsAsFactors = FALSE)
```

- **Inspect the dataset**  
```r
   str(student_data)
   nrow(student_data)  # Number of records
   names(student_data)  # Attribute names
```

- **Subset numeric attributes only**  
```r
   student_numeric <- student_data[sapply(student_data, is.numeric)]
```

- **Compute correlation matrix**  
```r
   cor_matrix <- cor(student_numeric, use = "complete.obs", method = "pearson")
```

- **Visualize correlation matrix (heatmap)**  
```r
   library(ggplot2)
   library(reshape2)
   melted_cor <- melt(cor_matrix)
   ggplot(melted_cor, aes(Var1, Var2, fill = value)) +
     geom_tile() +
     scale_fill_gradient2(low = "blue", high = "red", mid = "white") +
     theme(axis.text.x = element_text(angle = 90))
```

- **Extract specific correlation values**  
```r
   cor_matrix["Attendance", "Hours_Studied"]
   cor_matrix["Attendance", "Exam_Score"]
   cor_matrix["Tutoring_Sessions", "Previous_Scores"]
   cor_matrix["Physical_Activity", "Sleep_Hours"]
```

- **Identify scatter plot pattern (manually check plots)**  
```r
   ggplot(student_data, aes(x = Hours_Studied, y = Exam_Score)) +
     geom_point() + geom_smooth(method = "lm", se = FALSE)
```

---

## **Topic 4: Data Frames**
### **Dataset: PokeDex Dataset**  
📌 **Steps:**  
- **Load the dataset**  
```r
   pokedex <- read.csv("pokedex.csv", stringsAsFactors = FALSE)
```
- **Remove image path column**  
```r
   pokedex <- pokedex[ , !(names(pokedex) %in% c("Image.Path"))]
```
- **Set row names and remove Name column**  
```r
   rownames(pokedex) <- pokedex$Name
   pokedex$Name <- NULL
```
- **Retrieve Omastar’s record**  
```r
   pokedex["Omastar", ]
```
- **Count Pokémon without a second type**  
```r
   sum(pokedex$Type.2 == "")
```
- **Count Pokémon with Speed < 60**  
```r
   sum(pokedex$Speed < 60)
```
- **Compute average attack of Water-type Pokémon**  
```r
   mean(pokedex$Attack[pokedex$Type.1 == "Water" | pokedex$Type.2 == "Water"])
```
- **Identify Fairy Pokémon with highest HP**  
```r
   fairy_pokemon <- pokedex[pokedex$Type.1 == "Fairy" | pokedex$Type.2 == "Fairy", ]
   fairy_pokemon[which.max(fairy_pokemon$HP), ]
```
- **Normalize HP, Attack, Defense using Min-Max**  
```r
   normalize <- function(x) (x - min(x)) / (max(x) - min(x))
   pokedex$NormHP <- normalize(pokedex$HP)
   pokedex$NormAttack <- normalize(pokedex$Attack)
   pokedex$NormDefense <- normalize(pokedex$Defense)
```
- **Find Pokémon with top 3 NormHP values**  
 ```r
    head(pokedex[order(-pokedex$NormHP), "NormHP"], 3)
 ```
- **Compute median NormAttack and average NormDefense**  
 ```r
    median(pokedex$NormAttack)
    mean(pokedex$NormDefense)
 ```
- **Create Performance metric & Grade column**  
 ```r
    pokedex$Performance <- pokedex$NormHP * pokedex$NormAttack * pokedex$NormDefense + 0.0002
    pokedex$Grade <- cut(pokedex$Performance, 
                          breaks = c(0, 0.15, 0.2, 1),
                          labels = c("Weak", "Normal", "Strong"))
 ```
- **Find number of Pokémon with "Strong" Grade**  
 ```r
    sum(pokedex$Grade == "Strong")
 ```
- **Find Grade of Pokémon named "Haunter"**  
 ```r
    pokedex["Haunter", "Grade"]
 ```

---

### **Summary of the Approach**  
1. **Load and inspect the dataset** (`read.csv()`, `str()`, `head()`)  
2. **Process and clean the data** (`subset()`, `filter()`, `normalize()`)  
3. **Perform calculations and statistical analysis** (`cor()`, `mean()`, `median()`)  
4. **Visualize the results** (`ggplot2` for charts, `table()` for contingency tables)  
5. **Extract key insights and categorize data** (`cut()` for grading, sorting methods)  

Would you like additional guidance or refinements in specific areas? 🚀