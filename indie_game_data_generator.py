import numpy as np
import pandas as pd

def indie_game_data_generate(n_games=500):
    np.random.seed(42) 
    
    data = []

    for game_id in range(1, n_games + 1):
        # 1. BIAYA (Independent Variables)
        dev_cost = np.random.uniform(500, 3000) * 100
        market_cost = np.random.uniform(50, 1000) * 100
        
        # 2. PRICE & QUALITY
        price_tag = np.random.choice([0, 9.99, 14.99, 19.99, 29.99, 59.99])
        
        # Anggap dev_cost mencerminkan kualitas dasar
        quality_score = (dev_cost / 300000) * 100 + np.random.normal(0, 10) 

        # 3. PLAYER BASE (Tergantung Marketing + Quality + Harga)
        # Marketing menarik player, Quality membuat mereka bertahan atau viral, Harga mahal mengurangi player
        base_players = (market_cost * 2) + (quality_score * 50)
        price_penalty = 1 - (price_tag / 100)
        
        # Ada game yg meledak
        luck_factor = np.random.pareto(1.2) * 5000
        
        player_base = (base_players * price_penalty) + luck_factor
        player_base = int(np.clip(player_base, 100, 1000000)) # Minimal 100 player

        # 4. REVIEW SCORE (Korelasi dengan Quality + Noise)
        review_score = np.clip(quality_score + np.random.normal(0, 15), 0, 100)

        # 5. AVG PLAYTIME (Tergantung Quality & Genre/Random)
        avg_playtime = np.random.uniform(1, 40)
        # Kadang ada bot atau glitch (Playtime 999 jam)
        if np.random.random() < 0.02:
            avg_playtime = 999.0

        # 6. IS PROFITABLE? (The Logic)
        revenue = (player_base * price_tag) * 0.7 # Potongan Steam/Platform 30%
        total_costs = dev_cost + market_cost
        is_profitable = 1 if revenue > total_costs else 0

        data.append({
            "game_id": f"ID_{game_id:03d}",
            "dev_cost": round(dev_cost, 2),
            "market_cost": round(market_cost, 2),
            "price_tag": price_tag,
            "player_base": player_base,
            "review_score": round(review_score, 1),
            "avg_playtime": round(avg_playtime, 1),
            "is_profitable": is_profitable, 
        })

    return pd.DataFrame(data)

# Eksekusi dan simpan
df = indie_game_data_generate(500)