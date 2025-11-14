# data/products_data.py

import pandas as pd

def load_products_df():
    """Return a mock fashion product dataset as a Pandas DataFrame."""
    data = [
        {
            "name": "Boho Sunset Maxi Dress",
            "desc": "Flowy maxi dress with earthy hues and floral patterns, perfect for sunset festivals and free-spirited vibes.",
            "tags": ["boho", "festival", "earthy"]
        },
        {
            "name": "Urban Edge Bomber Jacket",
            "desc": "Sleek black bomber jacket with silver zippers, crafted for modern city explorers and street chic looks.",
            "tags": ["urban", "chic", "streetwear"]
        },
        {
            "name": "Cozy Knit Sweater",
            "desc": "Warm oversized knit made from soft wool blends, ideal for relaxed weekends and cozy home vibes.",
            "tags": ["cozy", "casual", "comfort"]
        },
        {
            "name": "Energetic Street Sneakers",
            "desc": "White sneakers with cushioned soles for all-day activity. Designed for energetic, active urban lifestyles.",
            "tags": ["sporty", "urban", "energetic"]
        },
        {
            "name": "Minimalist Leather Tote",
            "desc": "Elegant structured tote bag in smooth leather, designed for minimalist everyday style.",
            "tags": ["minimalist", "elegant", "classic"]
        },
        {
            "name": "Retro Denim Jacket",
            "desc": "Vintage-inspired denim jacket with subtle fading for a relaxed, laid-back vibe.",
            "tags": ["retro", "casual", "vintage"]
        },
        {
            "name": "Elegant Silk Blouse",
            "desc": "Champagne-toned silk blouse that drapes gracefully, exuding sophistication and femininity.",
            "tags": ["elegant", "chic", "feminine"]
        },
        {
            "name": "Adventure Cargo Pants",
            "desc": "Durable cotton cargo pants designed for exploration and comfort in outdoor settings.",
            "tags": ["adventure", "rugged", "outdoor"]
        },
        {
            "name": "Summer Linen Shirt",
            "desc": "Lightweight linen shirt in soft sky blue, perfect for relaxed summer getaways.",
            "tags": ["summer", "casual", "relaxed"]
        },
        {
            "name": "Bold Metallic Heels",
            "desc": "Statement metallic heels that add confidence and glamour to any evening outfit.",
            "tags": ["bold", "glam", "nightlife"]
        }
    ]

    return pd.DataFrame(data)
