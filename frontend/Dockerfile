FROM openjdk:8-jdk-alpine
ADD target/frontend-0.0.1-SNAPSHOT.war app.war

ENV JAVA_OPTS=""

ENTRYPOINT ["java","-jar", "/app.war", "--server.port=8095"]