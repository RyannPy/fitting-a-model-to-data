import pandas as pd
import numpy as np

def pelanggan_generator(n_user=1000):
    np.random.seed(42)

    data = []

    for user_id in range(1, n_user + 1):

        # 1. DAYS ACTIVE
        days_active =  round(np.random.uniform(0, 365))

        # 2. AVG SESSION TIME
        avg_session_time = round(np.random.uniform(0, 240))

        # 3. COMUNITY ENGAGEMENT
        comunity_engagement = round(np.random.uniform(1, 100))

        


