FROM openjdk:8-jdk-alpine
ADD target/game-0.0.1-SNAPSHOT.jar app.jar

ENV JAVA_OPTS=""

EXPOSE 8088

ENTRYPOINT ["java","-jar", "/app.jar"]
CMD ["--server.port=8088"]