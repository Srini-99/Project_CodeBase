import json
from collections import OrderedDict

# profact deduplication
unique_proc = set()

with open('procfact.ndjson', 'r') as input_file:
    for line in input_file:
        record = json.loads(line, object_pairs_hook=OrderedDict)
        
        record_str = json.dumps(record)
        unique_proc.add(record_str)

with open('dedup_procfact.ndjson', 'w') as output_file:
    for record_str in unique_proc:
        output_file.write(record_str + '\n')

print("Duplicates removed from procfact.")
#---------------------------------------------------

# sockfact deduplication
unique_sock = set()

with open('socketfact.ndjson', 'r') as input_file:
    for line in input_file:
        record = json.loads(line, object_pairs_hook=OrderedDict)
        
        record_str = json.dumps(record)
        unique_sock.add(record_str)

with open('dedup_sockfact.ndjson', 'w') as output_file:
    for record_str in unique_sock:
        output_file.write(record_str + '\n')

print("Duplicates removed from sockfact.")
#---------------------------------------------------

# edgefact deduplication
unique_edge = set()

with open('edgefact_0.ndjson', 'r') as input_file:
    for line in input_file:
        record = json.loads(line, object_pairs_hook=OrderedDict)
        
        record_str = json.dumps(record)
        unique_edge.add(record_str)

with open('dedup_edgefact.ndjson', 'w') as output_file:
    for record_str in unique_edge:
        output_file.write(record_str + '\n')

print("Duplicates removed from edgefact.")
#---------------------------------------------------

# nodefact deduplication
unique_node = set()

with open('nodefact.ndjson', 'r') as input_file:
    for line in input_file:
        record = json.loads(line, object_pairs_hook=OrderedDict)
        
        record_str = json.dumps(record)
        unique_node.add(record_str)

with open('dedup_nodefact.ndjson', 'w') as output_file:
    for record_str in unique_node:
        output_file.write(record_str + '\n')

print("Duplicates removed from nodefact.")
#---------------------------------------------------

# nodefact deduplication
unique_file = set()

with open('filefact.ndjson', 'r') as input_file:
    for line in input_file:
        record = json.loads(line, object_pairs_hook=OrderedDict)
        
        record_str = json.dumps(record)
        unique_file.add(record_str)

with open('dedup_filefact.ndjson', 'w') as output_file:
    for record_str in unique_file:
        output_file.write(record_str + '\n')

print("Duplicates removed from filefact.")
#---------------------------------------------------