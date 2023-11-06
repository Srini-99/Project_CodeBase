# Cypher Queries
 WIth the fact files from ShadeWatcher Parser,  
 -> perform conversion of text files to ndjson files
 -> perform deduplication of records
 and then feed it into Neo4j with these Cypher queries to visualise them.
 
 NOTE: This requires APOC library installed.

```
// Change the paths to the ndjson files as required.

CALL apoc.load.json('file:///procfact.ndjson') YIELD value as data
CREATE (node:proc)
SET node = data;

CALL apoc.load.json('file:///filefact.ndjson') YIELD value as data
CREATE (node:file)
SET node = data;

CALL apoc.load.json('file:///sockfact.ndjson') YIELD value as data
CREATE (node:sock)
SET node = data;


// Import the edgefact data
CALL apoc.load.json("file:///edgefact.ndjson") YIELD value as data

// Match nodes based on their IDs
MATCH (node1)
WHERE node1.id = data.n1_hash

MATCH (node2)
WHERE node2.id = data.n2_hash

// Create relationships dynamically based on the "relation" field
WITH data, node1, node2
CALL apoc.create.relationship(node1, data.relation, {}, node2) YIELD rel
SET rel.sequence = data.sequence, rel.session = data.session, rel.timestamp = data.timestamp;
```

