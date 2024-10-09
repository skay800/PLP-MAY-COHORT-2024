// client/script.js

const productList = document.getElementById('product-list');

// Fetch products from the server
async function fetchProducts() {
    try {
        const response = await fetch('http://localhost:5001/api/products');
        const products = await response.json();
        displayProducts(products);
    } catch (err) {
        console.error('Error fetching products:', err);
    }
}
async function createProduct(product) {
    try {
        const response = await fetch('http://localhost:5001/api/products', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(product), // Convert the product object to JSON
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const newProduct = await response.json();
        console.log('Created product:', newProduct);
    } catch (err) {
        console.error('Error creating product:', err);
    }
}

async function editProduct(id, updatedProduct) {
    try {
        const response = await fetch(`http://localhost:5001/api/products/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedProduct), // Convert the updated product object to JSON
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const product = await response.json();
        console.log('Updated product:', product);
    } catch (err) {
        console.error('Error updating product:', err);
    }
}

// Example usage
editProduct('productIdHere', { name: 'Updated Product', price: 25, image: 'updatedimage.jpg' });

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

