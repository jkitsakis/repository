package com.example.publications.infrastructure.adapter;

import com.example.publications.domain.Publication;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import java.util.List;

@JsonIgnoreProperties(ignoreUnknown = true)
public class GraphQLResponse {

    @JsonProperty("data")
    private DataContainer data;

    public DataContainer getData() {
        return data;
    }

    public void setData(DataContainer data) {
        this.data = data;
    }

    public List<PublicationEdge> getPublications() {
        return data != null ? data.getPublications().getEdges() : List.of();
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class DataContainer {
        @JsonProperty("publications")
        private Publications publications;

        public Publications getPublications() {
            return publications;
        }

        public void setPublications(Publications publications) {
            this.publications = publications;
        }
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class Publications {
        @JsonProperty("edges")
        private List<PublicationEdge> edges;

        public List<PublicationEdge> getEdges() {
            return edges;
        }

        public void setEdges(List<PublicationEdge> edges) {
            this.edges = edges;
        }
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static class PublicationEdge {
        @JsonProperty("node")
        private Publication node;

        public Publication getNode() {
            return node;
        }

        public void setNode(Publication node) {
            this.node = node;
        }
    }
}
