# Load the dataset 
poke_data <- read.csv("datasets//pokedex.csv", header = TRUE, sep = ",")

#
#a.
# Inspect structure
str(poke_data)

# Remove image path column
poke_data$Image <- NULL

# Set row names to 'Name' and remove the column
rownames(poke_data) <- poke_data$Name
poke_data$Name <- NULL

# Fetch record for "Omastar"
omastar_record <- poke_data["Omastar",]
omastar_record

#b. Identifying Specific pokemons
# number of Pokemon that do not have a second type
num_no_second_type <- sum(poke_data$Type.2 == "")

# number of Pokemon whose Speed is less than 60
num_speed_less_than_60 <- sum(poke_data$Speed < 60)

# Step 3: Print the results
print(paste("Number of pokemon without a second type: ",num_no_second_type))
print(paste("Number of pokemon whose Speed is less than 60: ",num_speed_less_than_60))

#c. average attack value of Water type Pokemon
water_attack <- mean(poke_data$Attack[poke_data$Type.1 == "Water" | poke_data$Type.2 == "Water"], na.rm = TRUE)
cat("Average attack value of all Water type Pokémon: ", water_attack, "\n")

# Identify the Fairy-type Pokémon with the greatest HP value
fairy_hp <- poke_data[poke_data$Type.1 == "Fairy" | poke_data$Type.2 == "Fairy", ]
fairy_max_hp <- fairy_hp[which.max(fairy_hp$HP), ]
fairy_max_hp_name <- rownames(fairy_max_hp)
print(fairy_max_hp_name)

#d

# Normalize HP, Attack, and Defense using min-max normalization
poke_data$NormHP <- (poke_data$HP - min(poke_data$HP)) / (max(poke_data$HP) - min(poke_data$HP))
poke_data$NormAttack <- (poke_data$Attack - min(poke_data$Attack)) / (max(poke_data$Attack) - min(poke_data$Attack))
poke_data$NormDefense <- (poke_data$Defense - min(poke_data$Defense)) / (max(poke_data$Defense) - min(poke_data$Defense))

# Fetch required values
top_norm_hp_pokemon <- rownames(poke_data[order(-poke_data$NormHP), ])[1:3]
median_norm_attack <- median(poke_data$NormAttack)
average_norm_defense <- mean(poke_data$NormDefense)

cat("Names of Pokemon with the three highest NormHP values: ", top_norm_hp_pokemon, "\n")
cat("Median value of the NormAttack attribute: ", median_norm_attack, "\n")
cat("Average value of the NormDefense attribute: ", average_norm_defense, "\n")


#e.	Calculate  Performance 
poke_data$Performance <- poke_data$NormHP * poke_data$NormAttack * poke_data$NormDefense + 0.0002

# Create Grade
poke_data$Grade <- cut(poke_data$Performance,
                       breaks = c(0, 0.15, 0.2, 1),
                       labels = c("Weak", "Normal", "Strong"),
                       right = TRUE)  # TRUE to include upper limits of the intervals

# Required values
strong_grade_count <- sum(poke_data$Grade == "Strong")
haunter_grade <- poke_data["Haunter", "Grade"]

cat("Number of Pokémon with Strong Grade: ", strong_grade_count, "\n")
cat("Grade of Pokémon named 'Haunter': ", haunter_grade, "\n")

