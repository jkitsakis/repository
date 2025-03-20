
package com.example.publications.web;

import com.example.publications.application.service.NavigationService;
import com.example.publications.domain.NavigationNode;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/navigation")
public class NavigationController {
    private final NavigationService navigationService;

    public NavigationController(NavigationService navigationService) {
        this.navigationService = navigationService;
    }

    @GetMapping
    public List<NavigationNode> getNavigationTree() {
        return navigationService.getNavigationTree();
    }
}
