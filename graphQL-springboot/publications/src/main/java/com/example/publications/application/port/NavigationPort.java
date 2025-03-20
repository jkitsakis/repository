
package com.example.publications.application.port;

import com.example.publications.domain.NavigationNode;
import java.util.List;

public interface NavigationPort {
    List<NavigationNode> getNavigationTree();
}
