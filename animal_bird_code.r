# Define the entities
entities <- c("Animal", "Bird")

# Define the attributes and behaviors
attributes_behaviors <- c("has_legs", "has_tail", "can_walk", "has_feathers", "can_fly")

# Create the semantic net
semantic_net <- data.frame(
  Entity = rep(entities, each = length(attributes_behaviors)),
  Characteristic = rep(attributes_behaviors, times = length(entities)),
  Value = c(
    "Yes", "Yes", "Yes", "No", "No",
    "Yes", "Yes", "Yes", "Yes", "Yes"
  )
)

# Print the semantic net
print(semantic_net)

