document.addEventListener("DOMContentLoaded", () => {
    const searchBar = document.getElementById("search-bar");
    const searchButton = document.getElementById("search-button");
    const productGrid = document.getElementById("product-grid");

    searchButton.addEventListener("click", () => {
        const query = searchBar.value.trim();
        if (query) {
            alert(Searching for: ${query});
            // Here you can add actual search functionality.
        }
    });
    function searchProduct() {
        let query = document.getElementById('search-box').value;
        window.location.href = `search.html?query=${query}`;
    }

    let banners = document.querySelectorAll('.banner');
    let index = 0;
    
    function changeBanner() {
        banners.forEach(banner => banner.classList.remove('active'));
        banners[index].classList.add('active');
        index = (index + 1) % banners.length;
    }
    
    setInterval(changeBanner, 4000);