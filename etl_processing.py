# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:27:47 2025

@author: mmunoz
"""

# !pip install os
# !pip install pandas


import os
import pandas as pd

# Get the directory where the script is located
script_dir = os.getcwd()


# Define paths for raw and processed data
source_path = os.path.join(script_dir, 'data/raw/').replace('\\', '/')
target_path = os.path.join(script_dir, 'data/processed/').replace('\\', '/')

# =============================================================================
# Extraction of info from data source 
# =============================================================================

# Read files
df_x_clustering = pd.read_csv(os.path.join(source_path, 'x-clustering.csv'))
df_x_clustering_cluster_metadata = pd.read_csv(os.path.join(source_path, 'x-clustering-cluster_metadata.csv'))
df_x_raw = pd.read_csv(os.path.join(source_path, 'x-raw.csv'))
df_x_related_factchecks = pd.read_csv(os.path.join(source_path, 'x-related-factchecks.csv'))
df_x_toxicity_attacks = pd.read_csv(os.path.join(source_path, 'x-toxicity_attacks.csv'))

# =============================================================================
# Transformation of data needed
# =============================================================================

## x-clustering-cluster_metadata

df_x_clustering_cluster_metadata['keywords'] = df_x_clustering_cluster_metadata['keywords'].apply(
    lambda x: [kw.strip().capitalize().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u') for kw in x.split(',')]
)
df_x_clustering_cluster_metadata_exploded = df_x_clustering_cluster_metadata.explode('keywords').reset_index(drop=True)

# Define banks for categorization
banks = [
    "Banco santander", "Caixabank", "Bbva", "Banco sabadell", 
    "Kutxabank", "Unicaja", "Bankinter", 
    "Evo banco", "Banco de españa", "Openbank", "Abanca", "Banc sabadell"
]

# Assign 'is_bank' and 'bank_keyword' fields
df_x_clustering_cluster_metadata_exploded['is_bank'] = df_x_clustering_cluster_metadata_exploded['keywords'].apply(lambda x: x in banks)

# Update to create separate records for each bank_keyword found within the same cluster_id
def explode_bank_keywords(group):
    # Get bank keywords present in the group
    bank_keywords_in_group = set(group['keywords']).intersection(banks)
    if bank_keywords_in_group:
        # Duplicate rows for each bank_keyword found
        expanded_rows = []
        for _, row in group.iterrows():
            for bank in bank_keywords_in_group:
                new_row = row.copy()
                new_row['bank_keyword'] = bank
                expanded_rows.append(new_row)
        return pd.DataFrame(expanded_rows)
    else:
        group['bank_keyword'] = None
        return group
    
# Apply the function to each cluster group
df_x_clustering_cluster_metadata_exploded = df_x_clustering_cluster_metadata_exploded.groupby('cluster_id').apply(explode_bank_keywords)


# Drop rows where 'keywords' matches 'bank_keyword'
df_x_clustering_cluster_metadata_exploded = df_x_clustering_cluster_metadata_exploded[
    df_x_clustering_cluster_metadata_exploded['keywords'] != df_x_clustering_cluster_metadata_exploded['bank_keyword']
]

## x-raw

# Convert the 'date' column to datetime
df_x_raw['date'] = pd.to_datetime(df_x_raw['date'])

# Create a 'week' column representing the ISO week of the year
df_x_raw['week'] = df_x_raw['date'].dt.isocalendar().week

# Count unique messages per user.id and week
messages_per_week = df_x_raw.groupby(['user.id', 'week']).size().reset_index(name='messages_per_week')

# Calculate the average number of messages per week for each user.id
avg_messages_per_week = messages_per_week.groupby('user.id')['messages_per_week'].mean().reset_index()
avg_messages_per_week.rename(columns={'messages_per_week': 'avg_messages_per_week'}, inplace=True)

# Merge the average frequency back into the original DataFrame
df_x_raw = df_x_raw.merge(avg_messages_per_week, on='user.id', how='left')

df_x_raw.drop(columns=['week'], inplace=True)

## x-toxicity_attacks
# Convert strings representing lists into actual lists and trim elements
df_x_toxicity_attacks['object_attack'] = df_x_toxicity_attacks['object_attack'].apply(
    lambda x: [item.strip() for item in eval(x)] if isinstance(x, str) and x.startswith('[') else []
)

# Explode the list into individual rows
df_x_toxicity_attacks_exploded = df_x_toxicity_attacks.explode('object_attack')


# =============================================================================
# Load of transformed data into target path
# =============================================================================

df_x_clustering.to_csv(target_path + 'x-clustering_processed.csv', index=False)
df_x_clustering_cluster_metadata.to_csv(target_path + 'x-clustering-cluster_metadata_processed.csv', index=False)
df_x_clustering_cluster_metadata_exploded.to_csv(target_path + 'x-clustering-cluster_metadata_pivot_processed.csv', index=False)
df_x_raw.to_csv(target_path + 'x-raw_processed.csv', index=False)
df_x_related_factchecks.to_csv(target_path + 'x-related-factchecks_processed.csv', index=False)
df_x_toxicity_attacks.to_csv(target_path + 'x-toxicity_attacks_processed.csv', index=False)
df_x_toxicity_attacks_exploded.to_csv(target_path + 'x-toxicity_attacks_pivot_processed.csv', index=False)
