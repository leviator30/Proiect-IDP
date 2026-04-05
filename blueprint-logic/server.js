const express = require('express');
const axios = require('axios');
const app = express();
app.use(express.json());

const BRIDGE_URL = 'http://persistence-bridge:3000/blueprints';

// Rule: Users must provide a title and a valid string to save
app.post('/api/blueprints/share', async (req, res) => {
    try {
        const { title, blueprintString, author } = req.body;

        // Business Rule: Check for minimum title length
        if (!title || title.length < 3) {
            return res.status(400).send({ error: "Title too short" });
        }

        // Business Rule: Forward to Persistence Bridge for validation & storage
        const response = await axios.post(BRIDGE_URL, {
            title,
            blueprintString,
            author: author || "Anonymous"
        });

        res.status(201).send({
            message: "Blueprint shared successfully!",
            id: response.data._id
        });
    } catch (error) {
        // Observability: Check Kibana if the error happened here or in the Bridge
        res.status(error.response?.status || 500).send(error.response?.data || error.message);
    }
});

// Rule: Fetch all blueprints
app.get('/api/blueprints', async (req, res) => {
    try {
        const response = await axios.get(BRIDGE_URL);
        res.send(response.data);
    } catch (error) {
        res.status(500).send("Internal Logic Error");
    }
});

app.listen(3000, () => console.log('Blueprint Logic Service active on port 3000'));