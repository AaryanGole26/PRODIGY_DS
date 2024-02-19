import matplotlib.pyplot as matplt

# Sample data for age groups and corresponding counts
age_groups = ['0-9', '10-19', '20-29', '30-39', '40-49']
matplt.figure(figsize=(7, 7))
counts = [50, 120, 300, 200, 80]

# Bar Chart Characteristics
matplt.bar(age_groups, counts, color='red')

# Labels and Title
matplt.title('Distribution of Individuals in Different Age Groups')
matplt.xlabel('Age Groups')
matplt.ylabel('Number of Individuals')

matplt.show()