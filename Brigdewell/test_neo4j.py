import truststore
from neo4j import GraphDatabase

truststore.inject_into_ssl()

uri = "neo4j+s://a23140fb.databases.neo4j.io"
user = "neo4j"
password = "0e4_OEA3SnwOu0PDdF-mJXlGzeX55b-rOijUPS5i7cg"

driver = GraphDatabase.driver(uri, auth=(user, password))

with driver.session() as session:
    result = session.run("RETURN 1 AS x")
    print(result.single()["x"])

driver.close()