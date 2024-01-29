library(DiagrammeR)

# Define the flowchart using the DOT language with custom colors
graph <- "
digraph ClothingRecommendations {
  node [fontcolor=yellow, fontsize=20, shape=box];
  edge [color=Green];

  # Define seasons and their colors
  Winter [color=blue, style=filled];
  Spring [color=Green, style=filled];
  Summer [color=skyblue, style=filled];
  Fall [color=brown, style=filled];
  
  # Define types of places and their colors
  Cold_Place [color=paleturquoise, style=filled];
  Mild_Place [color=orange, style=filled];
  Hot_Place [color=red, style=filled];
  
  # Define clothing options and their colors
  Wear_Heavy_Coat [color=blue, style=filled];
  Wear_Jacket [color=blue, style=filled];
  Wear_Windbreaker [color=Green, style=filled];
  Wear_Polo_Shirt [color=Green, style=filled];
  Wear_Tshirt [color=skyblue, style=filled];
  Wear_Light_Jacket [color=skyblue, style=filled];
  Wear_Sweater [color=brown, style=filled];
  Wear_Long_Sleeve_Shirt [color=brown, style=filled];

  # Define connections between seasons and places
  Winter -> Cold_Place [color=blue];
  Winter -> Mild_Place [color=blue];
  Spring -> Cold_Place [color=Green];
  Spring -> Mild_Place [color=Green];
  Summer -> Mild_Place [color=skyblue];
  Summer -> Hot_Place [color=skyblue];
  Fall -> Cold_Place [color=brown];
  Fall -> Mild_Place [color=brown];
  
  # Define connections between places and clothing options
  Cold_Place -> {Wear_Heavy_Coat Wear_Jacket Wear_Sweater Wear_Windbreaker} [color=paleturquoise];
  Mild_Place -> {Wear_Polo_Shirt Wear_Light_Jacket Wear_Long_Sleeve_Shirt} [color=orange];
  Hot_Place -> {Wear_Tshirt} [color=red];
}
"

# Display the graph in a larger size
grViz(graph, width=800, height=700)
