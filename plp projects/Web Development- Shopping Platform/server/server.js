const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const Product = require('./models/Product'); // Import the Product model

const app = express();
const PORT = process.env.PORT || 5001;

// Enable CORS for all routes
app.use(cors());
app.use(express.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/shopping-platform', { // Update with your MongoDB URI
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => {
    console.log('Connected to MongoDB');
})
.catch(err => {
    console.error('Error connecting to MongoDB:', err);
});

// Route to fetch products from the database
app.get('/api/products', async (req, res) => {
    try {
        const products = await Product.find(); // Fetch products from the database
        res.json(products); // Send products as JSON response
    } catch (err) {
        console.error('Error fetching products:', err);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});
// Route to create a new product
app.post('/api/products', async (req, res) => {
  const { name, price, image } = req.body;

  try {
      const newProduct = new Product({ name, price, image });
      await newProduct.save(); // Save the product to the database
      res.status(201).json(newProduct); // Respond with the created product
  } catch (err) {
      console.error('Error creating product:', err);
      res.status(500).json({ message: 'Internal Server Error' });
  }
});
// Route to update an existing product
app.put('/api/products/:id', async (req, res) => {
  const { id } = req.params; // Get the product ID from the request parameters
  const { name, price, image } = req.body; // Get the updated data from the request body

  try {
      const updatedProduct = await Product.findByIdAndUpdate(
          id,
          { name, price, image },
          { new: true } // Return the updated document
      );

      if (!updatedProduct) {
          return res.status(404).json({ message: 'Product not found' });
      }

      res.json(updatedProduct); // Respond with the updated product
  } catch (err) {
      console.error('Error updating product:', err);
      res.status(500).json({ message: 'Internal Server Error' });
  }
});
// Route to partially update an existing product
app.patch('/api/products/:id', async (req, res) => {
  const { id } = req.params;
  
  try {
      const updatedProduct = await Product.findByIdAndUpdate(id, req.body, { new: true });
      
      if (!updatedProduct) {
          return res.status(404).json({ message: 'Product not found' });
      }

      res.json(updatedProduct);
  } catch (err) {
      console.error('Error updating product:', err);
      res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start your server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
