import pandas as pd
import numpy as np

def pelanggan_generator(n_user=1000):
    np.random.seed(42)

    data = []

    for user_id in range(1, n_user + 1):

        premium_score = 0

        # 1. DAYS ACTIVE
        days_active =  round(np.random.uniform(0, 365))
        if days_active >= 300:
            premium_score += 2
        elif days_active >= 180:
            premium_score += 1

        # 2. AVG SESSION TIME
        avg_session_time = round(np.random.uniform(5, 240))
        if avg_session_time >= 180:
            premium_score += 2
        elif avg_session_time >= 120:
            premium_score += 1

        # 3. COMMUNITY ENGAGEMENT
        community_engagement = round(np.random.uniform(1, 100))
        if community_engagement > 75:
            premium_score += 1

        # 4 TOTAL SPEND : linear dengan days_active, avg_session_time, dan community_engagement (dalam rupiah)
        noise = round(np.random.uniform(-10, 10), 1)
        total_spend = (avg_session_time + 0.5 * (days_active + community_engagement) + noise) * 1000

        # 5. IS PREMIUM?
        prob_noise = np.random.uniform(-0.05, 0.05)
        premium_prob = (premium_score / 10) * 2
        if premium_prob > 0.8:
            is_premium = 1
        else:
            is_premium = 0

    






        



        


