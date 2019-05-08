## 3. Instrucciones de uso

2. Cámbiese a la carpeta del proyecto.
3. Compile la imagen personalizada de la aplicación:

docker build -t flask-mongo .

4. Verifique que la imagen fue creada correctamente y que se encuentra en el repositorio local de imágenes:

`docker images | grep flask-mongo`

7. Inicie un contenedor con la aplicación, a partir de la imagen generada:

docker run --rm --name app -p 5000:5000 -d --net mongo-sh flask-mongo
 
8. Verifique que el contendor se encuentra en ejecución:

`docker ps`

9. Acceda a la interfaz web de la aplicación en un browser en la URL:

[http://localhost:5000](http://localhost:5000)

10. Detenga los contenedores:

`docker stop app`

11. Elimine los contenedores:

`docker rm app`

15. Elimine la imagen en caso de no requerirla:

`docker rmi flask-mongo`

## 4. Recursos

Para aprender a desarrollar una API con Flask API, favor de referirse a la documentación oficial disponible en [Flask API](https://www.flaskapi.org/).  

Para aprender a trabajar con la línea de comandos de `docker`, favor de referirse a la documentación oficial disponible en [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).

Para aprender como definir un archivo `Dockerfile`, favor de referirse a la documentación oficial disponible en [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).

Para aprender como definir un archivo `.dockerignore`, favor de referirse a la documentación oficial disponible en [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#dockerignore-file).