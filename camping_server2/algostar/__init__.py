import pandas as pd
from datetime import datetime
from tqdm import tqdm
import sys
import os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + '/preprocessing')
import algo_config as config
import cat_points as cp
import algo_points as ap
import tag_points as tp
import weights as wc
today = datetime.today().strftime('%m%d')

if __name__ == '__main__':
    # c5 = cp.Cat5Points()
    algo = ap.AlgoPoints()
    # tag = tp.TagPoints()
    # tag = tp.TagMerge()
    # final_weights = wc.FinalWeights().final_weights()

    # algo.polar_points('답게')
    # algo.algo_star('별똥별 글램핑')
    # algo_df = algo.make_algo_df()
    # algo_df.to_csv(config.Config.PATH + f"algo_df_{today}.csv", encoding='utf-8-sig')
    data, algo_log_scale = algo.algo_log_scale(just_load_file='max')
    algo_log_scale.to_csv("../../datas/algo_df_scaled.csv", encoding='utf-8-sig')

    # tag.tag_priority(8036, rank=3)
    # tag.tag_priority(7980, rank=5)
    # tag_df = tag.make_tag_prior_df(rank=7)

    # final_weights.final_weights()

    # tag.tag_merge()