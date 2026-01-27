// Custom Product Tabs - Switches between Atoms and Waves products
(function() {
    const PRODUCTS = [
        { name: 'Atoms', slug: 'atoms', icon: 'fa-solid fa-robot' },
        { name: 'Waves', slug: 'waves', icon: 'fa-solid fa-waveform-lines' }
    ];

    function getCurrentProduct() {
        const path = window.location.pathname;
        if (path.includes('/atoms')) return 'atoms';
        if (path.includes('/waves')) return 'waves';
        return 'atoms'; // default
    }

    function createTabsContainer() {
        const container = document.createElement('div');
        container.className = 'custom-product-tabs';
        container.setAttribute('role', 'tablist');
        
        const currentProduct = getCurrentProduct();
        
        PRODUCTS.forEach(product => {
            const tab = document.createElement('button');
            tab.className = 'custom-product-tab';
            tab.setAttribute('role', 'tab');
            tab.setAttribute('aria-selected', currentProduct === product.slug ? 'true' : 'false');
            tab.setAttribute('data-product', product.slug);
            
            if (currentProduct === product.slug) {
                tab.classList.add('active');
            }
            
            // Create icon element
            const icon = document.createElement('i');
            icon.className = product.icon;
            
            // Create text element
            const text = document.createElement('span');
            text.textContent = product.name;
            
            tab.appendChild(icon);
            tab.appendChild(text);
            
            tab.addEventListener('click', () => {
                navigateToProduct(product.slug);
            });
            
            container.appendChild(tab);
        });
        
        return container;
    }

    function navigateToProduct(productSlug) {
        // Navigate to the product's root page
        const baseUrl = window.location.origin;
        window.location.href = `${baseUrl}/${productSlug}`;
    }

    function insertTabs() {
        // Find the header element
        const header = document.querySelector('.fern-header');
        if (!header) {
            return false;
        }
        
        // Check if tabs already exist
        if (document.querySelector('.custom-product-tabs')) {
            return true;
        }
        
        // Find the header tabs container or create insertion point
        const headerTabs = header.querySelector('.fern-header-tabs');
        const tabsContainer = createTabsContainer();
        
        if (headerTabs) {
            // Insert at the beginning of header tabs
            headerTabs.insertBefore(tabsContainer, headerTabs.firstChild);
        } else {
            // Find a suitable place in the header
            const headerContent = header.querySelector('.fern-header-content') || header;
            headerContent.appendChild(tabsContainer);
        }
        
        return true;
    }

    function updateActiveTab() {
        const currentProduct = getCurrentProduct();
        const tabs = document.querySelectorAll('.custom-product-tab');
        
        tabs.forEach(tab => {
            const isActive = tab.getAttribute('data-product') === currentProduct;
            tab.classList.toggle('active', isActive);
            tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
        });
    }

    function init() {
        // Try to insert tabs
        if (!insertTabs()) {
            // If header not found, retry after a short delay
            setTimeout(init, 100);
            return;
        }
        
        // Update active state on navigation
        updateActiveTab();
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Re-initialize on navigation changes (for SPA behavior)
    let lastUrl = location.href;
    new MutationObserver(() => {
        const url = location.href;
        if (url !== lastUrl) {
            lastUrl = url;
            setTimeout(() => {
                insertTabs();
                updateActiveTab();
            }, 100);
        }
    }).observe(document, { subtree: true, childList: true });
})();
