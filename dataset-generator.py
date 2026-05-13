import pandas as pd
import numpy as np

def pelanggan_generator(n_user=1000):

    np.random.seed(42)

    data = []

    for user_id in range(1, n_user + 1):

        # =========================================
        # 1. FEATURE GENERATION
        # =========================================

        days_active = round(np.random.uniform(1, 365))

        avg_session_time = round(np.random.uniform(5, 240))

        community_engagement = round(np.random.uniform(1, 100))


        # =========================================
        # 2. TOTAL SPEND (REGRESSION TARGET)
        # =========================================

        noise = np.random.normal(0, 25)

        total_spend = (
            0.45 * days_active +
            1.2 * avg_session_time +
            0.8 * community_engagement +
            noise
        ) * 1000

        
        total_spend = max(0, round(total_spend))


        # =========================================
        # 3. PREMIUM SCORE
        # =========================================

        premium_score = (
            -6 + # default player = f2p
            0.015 * days_active +
            0.02 * avg_session_time +
            0.03 * community_engagement +
            np.random.normal(0, 1)
        )


        # =========================================
        # 4. SUPER NOISE / PLAYER PERSONAS
        # =========================================

        random_event = np.random.rand()


        # A. HARDCORE FREE PLAYER
        # aktif banget tapi tetap gratis
        if (
            days_active > 250 and
            avg_session_time > 150 and
            random_event < 0.07
        ):
            premium_score -= 5


        # B. RICH CASUAL
        # jarang main tapi suka top up
        elif (
            days_active < 80 and
            random_event < 0.05
        ):
            total_spend += np.random.randint(200000, 700000)


        # C. SOCIAL PLAYER
        # aktif komunitas tapi ga premium
        elif (
            community_engagement > 85 and
            random_event < 0.06
        ):
            premium_score -= 3


        # D. WHALE
        # spender besar
        elif random_event < 0.02:

            whale_bonus = np.random.randint(1000000, 5000000)

            total_spend += whale_bonus

            premium_score += 3


        # =========================================
        # 5. CONVERT SCORE -> PROBABILITY
        # =========================================

        premium_probability = 1 / (
            1 + np.exp(-premium_score)
        )


        # =========================================
        # 6. FINAL CLASSIFICATION
        # =========================================

        is_premium = np.random.choice(
            [0, 1],
            p=[
                1 - premium_probability,
                premium_probability
            ]
        )


        # =========================================
        # 7. SAVE ROW
        # =========================================

        data.append({
            "user_id": user_id,
            "days_active": days_active,
            "avg_session_time": avg_session_time,
            "community_engagement": community_engagement,
            "total_spend": total_spend,
            "is_premium": is_premium
        })


    df = pd.DataFrame(data)

    return df


df = pelanggan_generator()

print(df.head())

df.to_csv("indie_studio_players.csv", index=False)