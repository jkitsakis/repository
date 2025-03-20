package com.example.publications.domain;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Publication {
    @JsonProperty("id")
    private String id;

    @JsonProperty("title")
    private String title;

    public Publication() {}

    public Publication(String id, String title) {
        this.id = id;
        this.title = title;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
}
