
package com.example.publications.application.service;

import com.example.publications.application.port.PublicationPort;
import com.example.publications.domain.Publication;
import com.example.publications.infrastructure.adapter.RedisCache;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.concurrent.TimeUnit;

@Service
public class PublicationService {
    private final PublicationPort publicationPort;
    private final RedisCache redisCache;
    @Autowired
    private AuthService authService;

    public PublicationService(PublicationPort publicationPort, RedisCache redisCache) {
        this.publicationPort = publicationPort;
        this.redisCache = redisCache;
    }

    public List<Publication> getPublications(int first, String after) {
        String cacheKey = "publications:" + first + ":" + after;
        //Object cachedData = redisCache.get(cacheKey);

//        if (cachedData != null) {
//            return (List<Publication>) cachedData;
//        }

        List<Publication> publications = publicationPort.getPublications(first, after, authService.getAccessToken().getAccessToken());
        //redisCache.put(cacheKey, publications, 10, TimeUnit.MINUTES);
        return publications;
    }
}
