# Crear una red para el Sharding

docker network create mongo-sh
# -----------------------------------------------
# ------ Configurar el Config Replica Set -------
# -----------------------------------------------

# Crear tres contenedores para los nodos del Config Replica Set

docker run --name mongo-config1 -d --net mongo-sh mongo --replSet "rsConfig" --configsvr
docker run --name mongo-config2 -d --net mongo-sh mongo --replSet "rsConfig" --configsvr
docker run --name mongo-config3 -d --net mongo-sh mongo --replSet "rsConfig" --configsvr

# Iniciar una terminal en uno de los nodos

docker exec -it mongo-config1 bash

# Conectarse a uno de los nodos 

mongo --host mongo-config1 --port 27019

# Inicializar el Config Replica Set

config = {
      "_id" : "rsConfig",
      "configsvr": true,
      "members" : [
          {
              "_id" : 0,
              "host" : "mongo-config1:27019"
          },
          {
              "_id" : 1,
              "host" : "mongo-config2:27019"
          },
          {
              "_id" : 2,
              "host" : "mongo-config3:27019"
          }
      ]
  }

rs.initiate(config)

# Desconectarse del nodo

exit  # Para salir de mongo shell
exit  # Para salir del contenedor

# ------------------------------------------------
# ------ Configurar los Shard Replica Sets -------
# ------------------------------------------------

# Crear tres contenedores para los nodos del Shard Replica Set

docker run --name mongo-shard11 -d --net mongo-sh mongo --replSet "rsShard1" --shardsvr
docker run --name mongo-shard12 -d --net mongo-sh mongo --replSet "rsShard1" --shardsvr
docker run --name mongo-shard13 -d --net mongo-sh mongo --replSet "rsShard1" --shardsvr

# Iniciar una terminal en uno de los nodos

docker exec -it mongo-shard11 bash

# Conectarse a uno de los nodos 

mongo --host mongo-shard11 --port 27018

# Inicializar el Shard Replica Set

config = {
      "_id" : "rsShard1",
      "members" : [
          {
              "_id" : 0,
              "host" : "mongo-shard11:27018"
          },
          {
              "_id" : 1,
              "host" : "mongo-shard12:27018"
          },
          {
              "_id" : 2,
              "host" : "mongo-shard13:27018"
          }
      ]
  }

rs.initiate(config)

# Desconectarse del nodo

exit  # Para salir de mongo shell
exit  # Para salir del contenedor

# --------------------------------
# ------ Iniciar el Router -------
# --------------------------------

docker run  --name mongo-router -d --net mongo-sh mongo  mongos --configdb rsConfig/mongo-config1:27019,mongo-config2:27019,mongo-config3:27019 --bind_ip_all

# Conectarse al router

docker exec -it mongo-router mongo

# Adicionar Shards al clúster

sh.addShard( "rsShard1/mongo-shard11:27018")

# Habilitar sharding para una base de datos

sh.enableSharding("shdb")

# Habilitar sharding en una colección

Range: sh.shardCollection("shdb.data",  { "number" : 1 } )

Hash: sh.shardCollection("shdb.data", { _id : "hashed" } )

# Monitorear el estado del clúster

use shdb
sh.status()
db.printShardingStatus() 

# Ver las bases de datos con sharding 

use config
db.databases.find( { "partitioned": true } )

# Ver la lista de shards

use admin
db.adminCommand( { listShards : 1 } )


# Insertar datos en el cluster

use shdb
var bulk = db.data.initializeUnorderedBulkOp();
people = ["Marc", "Bill", "George", "Eliot", "Matt", "Trey", "Tracy", "Greg", "Steve", "Kristina", "Katie", "Jeff"];
for(var i=0; i<1000000; i++){
   user_id = i;
   name = people[Math.floor(Math.random()*people.length)];
   number = Math.floor(Math.random()*10001);
   bulk.insert( { "user_id":user_id, "name":name, "number":number });
}
bulk.execute();

# Dividir los datos entre chunks

sh.splitFind( "shdb.data", { "number": 4000 } )


# En caso de insertar datos antes de habilitar el sharding

sh.enableSharding( "shdb" )
db.data.createIndex( { number : 1 } )
sh.shardCollection( "shdb.data", { "number" : 1 } )


# Eliminar un shard

use admin
db.adminCommand( { removeShard: "<shard_name>" } )
sharding.js
Página 11 de 12