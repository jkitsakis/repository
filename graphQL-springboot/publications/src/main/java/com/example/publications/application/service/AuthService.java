package com.example.publications.application.service;


import com.example.publications.domain.AuthResponse;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

import java.util.HashMap;
import java.util.Map;

@Service
public class AuthService {

    private final String TOKEN_URL = "https://dxd-live-euipo-development.tridion.sdlproducts.com/token.svc";
    private final String CLIENT_ID = "cduser";  // Replace with actual client_id
    private final String CLIENT_SECRET = "0dDDlFllMs73zPdp9KNx";  // Replace with actual client_secret

    private final WebClient webClient;

    public AuthService(WebClient.Builder webClientBuilder) {
        this.webClient = webClientBuilder.build();
    }

    public AuthResponse getAccessToken() {
        return webClient.post()
                .uri(TOKEN_URL)
                .contentType(MediaType.APPLICATION_FORM_URLENCODED)
                .bodyValue("client_id=" + CLIENT_ID + "&client_secret=" + CLIENT_SECRET + "&grant_type=client_credentials")
                .retrieve()
                .bodyToMono(AuthResponse.class).block();
    }
}
