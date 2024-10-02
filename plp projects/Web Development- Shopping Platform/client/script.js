// client/script.js

const productList = document.getElementById('product-list');

// Fetch products from the server
async function fetchProducts() {
    try {
        const response = await fetch('http://localhost:5000/api/products');
        const products = await response.json();
        displayProducts(products);
    } catch (err) {
        console.error('Error fetching products:', err);
    }
}

// Display products
function displayProducts(products) {
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.classList.add('product');
        productDiv.innerHTML = `
            <h3>${product.name}</h3>
            <p>Price: $${product.price}</p>
            <img src="${product.image}" alt="${product.name}" />
            <button>Add to Cart</button>
        `;
        productList.appendChild(productDiv);
    });
}

// Initialize the app
fetchProducts();
