
package com.example.publications.application.port;

import com.example.publications.domain.Publication;
import java.util.List;

public interface PublicationPort {
    List<Publication> getPublications(int first, String after, String accessToken);
}
