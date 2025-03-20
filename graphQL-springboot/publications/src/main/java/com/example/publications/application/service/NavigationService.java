
package com.example.publications.application.service;

import com.example.publications.application.port.NavigationPort;
import com.example.publications.domain.NavigationNode;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class NavigationService {
    private final NavigationPort navigationPort;

    public NavigationService(NavigationPort navigationPort) {
        this.navigationPort = navigationPort;
    }

    public List<NavigationNode> getNavigationTree() {
        return navigationPort.getNavigationTree();
    }
}
