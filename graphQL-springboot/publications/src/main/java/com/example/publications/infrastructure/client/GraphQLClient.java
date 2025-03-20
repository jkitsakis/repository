package com.example.publications.infrastructure.client;

import com.example.publications.domain.Publication;
import com.example.publications.infrastructure.adapter.GraphQLResponse;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.http.HttpHeaders;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import java.util.List;
import java.util.Map;

@Service
public class GraphQLClient {
    private final WebClient webClient;
    private final String query;

    public GraphQLClient(WebClient.Builder webClientBuilder,  @Qualifier("publicationsQueryBean")  String publicationsQuery) {
        this.webClient = webClientBuilder.baseUrl("https://dxd-live-euipo-development.tridion.sdlproducts.com/cd/api").build();
        this.query = publicationsQuery;
    }

    public List<Publication> getPublications(int first, String after, String accessToken) {
        // Inject dynamic values into the query
        String formattedQuery = query
                .replace("$namespaceId", String.valueOf(2))
                .replace("$first", String.valueOf(first));
                //.replace("$after", after/*!=null ? String.valueOf(after) : ""*/);

        // Create the request body
        Map<String, Object> requestBody = Map.of(
                "query", formattedQuery,
                "variables", Map.of()
        );

        // Send request
        GraphQLResponse response = webClient.post()
                .uri("")
                .header(HttpHeaders.AUTHORIZATION, "Bearer " + accessToken)
                .header(HttpHeaders.CONTENT_TYPE, "application/json")
                .bodyValue(requestBody)
                .retrieve()
                .bodyToMono(GraphQLResponse.class)
                .block();

        return response != null ? response.getPublications().stream().map(GraphQLResponse.PublicationEdge::getNode).toList() : List.of();
    }
}