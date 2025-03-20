package com.example.publications.infrastructure.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

@Configuration
public class GraphQLConfig {

    @Bean(name = "publicationsQueryBean")
    public String publicationsQuery() {
        return loadGraphQLQuery("graphql/publicationsQuery.graphql");
    }

    private String loadGraphQLQuery(String resourcePath) {
        try (InputStream inputStream = new ClassPathResource(resourcePath).getInputStream()) {
            return new String(inputStream.readAllBytes(), StandardCharsets.UTF_8);
        } catch (IOException e) {
            throw new RuntimeException("Failed to load GraphQL query from classpath: " + resourcePath, e);
        }
    }
}

