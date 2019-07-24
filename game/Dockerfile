FROM openjdk:8-jdk-alpine
ADD target/game-0.0.1-SNAPSHOT.jar app.jar

ENV APP_PORT 8085
ENV JAVA_OPTS=""

EXPOSE 8081

ENTRYPOINT ["java","-jar",  "/app.jar", ${APP_PORT}]