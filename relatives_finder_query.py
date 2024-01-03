from sympy import symbols

#Define family members
adam, bob, carol, david, emma, frank, grace, helen, irene, john, kate, luke = symbols('adam bob carol david emma frank grace helen irene john kate luke')

#Define parent-child relationships using lists
parent_relations = {
    adam: [bob, carol],
    bob: [david, emma],
    carol: [frank, grace],
    david: [irene, john],
    emma: [kate, luke],
    frank: [],
    grace: [],
    irene: [],
    john:  [],
    kate:  [],
    luke:  [],
}

#Interactive query for finding relatives
person_to_query = input("Enter a person to find relatives: ").lower()

#Convert symbols to lowercase for comparison
parent_relations_lower = {key.name.lower(): [child.name.lower() for child in value] for key, value in parent_relations.items()}

if person_to_query in parent_relations_lower:
    person_relatives = parent_relations_lower[person_to_query]
    print(f"{person_to_query.capitalize()}'s relatives:", person_relatives)
else:
    print(f"Person '{person_to_query}' not found in the family tree.")
