import pandas as pd
import argparse
from sklearn.model_selection import train_test_split
import os

def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument("--dataset", default='all')
    args = args.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    df = pd.read_csv(f'{args.dataset}.txt',dtype='str',sep='\t')
    df = df[['entity1', 'relation', 'entity2']]
    train, test, _, _ = train_test_split(df, df, test_size=0.1, random_state=2020)
    train, valid, _, _ = train_test_split(train, train, test_size=0.11, random_state=2020)
    os.makedirs(args.dataset, exist_ok=True)
    train.to_csv(f'{args.dataset}/train.tsv', sep='\t', index=False, header=None)
    valid.to_csv(f'{args.dataset}/valid.tsv', sep='\t', index=False, header=None)
    test.to_csv(f'{args.dataset}/test.tsv', sep='\t', index=False, header=None)

    train.to_csv(f'{args.dataset}/train.txt', sep='\t', index=False, header=None)
    valid.to_csv(f'{args.dataset}/valid.txt', sep='\t', index=False, header=None)
    test.to_csv(f'{args.dataset}/test.txt', sep='\t', index=False, header=None)
    