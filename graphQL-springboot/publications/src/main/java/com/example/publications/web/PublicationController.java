
package com.example.publications.web;

import com.example.publications.application.service.PublicationService;
import com.example.publications.domain.Publication;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/publications")
public class PublicationController {
    private final PublicationService publicationService;

    public PublicationController(PublicationService publicationService) {
        this.publicationService = publicationService;
    }

    @GetMapping
    public List<Publication> getPublications(
            @RequestParam(defaultValue = "10") int first,
            @RequestParam(required = false) String after) {
        return publicationService.getPublications(first, after);
    }
}
