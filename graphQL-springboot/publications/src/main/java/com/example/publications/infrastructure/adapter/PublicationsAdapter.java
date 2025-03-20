package com.example.publications.infrastructure.adapter;

import com.example.publications.application.port.PublicationPort;
import com.example.publications.domain.Publication;
import com.example.publications.infrastructure.client.GraphQLClient;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PublicationsAdapter implements PublicationPort {

    @Autowired
    private GraphQLClient client;


    @Override
    public List<Publication> getPublications(int first, String after, String accessToken) {
        return client.getPublications(first, after, accessToken);

    }
}
