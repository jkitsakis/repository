package com.example.publications.infrastructure.adapter;

import com.example.publications.application.port.NavigationPort;
import com.example.publications.domain.NavigationNode;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class NavigationAdapter implements NavigationPort {

    @Override
    public List<NavigationNode> getNavigationTree() {
        // Dummy implementation - replace with actual logic
        return null;
    }
}
