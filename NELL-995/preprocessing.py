"""simple preprocessing script for NELL-995"""

import pandas as pd
from pathlib import Path

#1.load train
path = Path(__file__).parent / "train.txt"
source_df = pd.read_csv(path, sep="\t", names=["head", "relation", "tail"], dtype={"head": str, "relation": str,"tail": str})
#2. get all unique nodes 
node = pd.concat([source_df["head"], source_df["tail"]]).unique()
#3. get all unique relations
relation = source_df["relation"].unique()
#4. enumerate them
node_df = pd.DataFrame(node)
relation_df = pd.DataFrame(relation)
#5. save them
path_entity = Path(__file__).parent / 'entity2id.txt'
node_df.to_csv(path_entity, sep='\t', header=False, index=True)
path_relation = Path(__file__).parent / 'relation2id.txt'
relation_df.to_csv(path_relation, sep='\t', header=False, index=True)
