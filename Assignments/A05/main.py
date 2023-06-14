import csv

def assign_color(clan_number):
    colors = {
        '1': 'cyan',
        '2': 'pink',
        '3': 'yellow',
        '4': 'green',
        '5': 'orange'
    }
    return colors.get(clan_number, 'white')

def assign_shape(gender):
    if gender == 'Male':
        return 'ellipse'
    elif gender == 'Female':
        return 'polygon'
    else:
        return 'ellipse'

# Open the CSV file
with open('family_tree_data.csv', mode='r') as file:
    reader = csv.DictReader(file)

    # Initialize the dot file contents
    dot_content = 'digraph FamilyTree {\n'

    # Iterate over each row in the CSV file
    for row in reader:
        pid = row['pid']
        name = row['name']
        gender = row['gender']
        generation = row['generation']
        byear = row['byear']
        dyear = row['dyear']
        dage = row['dage']
        myear = row['myear']
        mage = row['mage']
        ptype = row['ptype']
        clan = row['clan']
        spouseId = row['spouseId']
        parentId1 = row['parentId1']
        parentId2 = row['parentId2']
        parentNodeId = row['parentNodeId']

        # Add the node definition to the dot file contents
        color = assign_color(clan)
        shape = assign_shape(gender)
        node_definition = f'"{pid}" [label="{name}\\nGender: {gender}\\nGeneration: {generation}\\nBirth Year: {byear}\\nDeath Year: {dyear}\\nDeath Age: {dage}\\nMarriage Year: {myear}\\nMarriage Age: {mage}\\nParent Type: {ptype}\\nClan: {clan}", style="filled", fillcolor="{color}", shape="{shape}", sides="4"];\n'
        dot_content += node_definition

        # Add the edge definitions to the dot file contents
        if spouseId:
            edge_definition = f'"{pid}" -> "{spouseId}" [label="Spouse"];\n'
            dot_content += edge_definition

        if parentId1:
            edge_definition = f'"{parentId1}" -> "{pid}" [label="Child"];\n'
            dot_content += edge_definition

        if parentId2:
            edge_definition = f'"{parentId2}" -> "{pid}" [label="Child"];\n'
            dot_content += edge_definition

        if parentNodeId:
            edge_definition = f'"{parentNodeId}" -> "{pid}" [label="Child"];\n'
            dot_content += edge_definition

    # Close the dot file
    dot_content += '}'

    # Save the dot file to disk
    with open('family_tree.dot', mode='w') as dot_file:
        dot_file.write(dot_content)
