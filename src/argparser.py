import argparse
import yaml
import os

def argparser_trainer():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_file",   default=os.getcwd() + "/config.yaml", type=str,   help="Config file")
    parser.add_argument("--output_dir",    default=os.getcwd(),                  type=str,   help="Output dir")
    parser.add_argument("--dataset_dir",   default='datasets/S1465',             type=str,   help="Dataset dir")
    parser.add_argument("--model",         default='MSA_Finetuning',             type=str,   help="Model name")
    parser.add_argument("--learning_rate", default='1e-5',                       type=float, help="Learning rate")
    parser.add_argument("--max_epochs",    default='5',                          type=int,   help="Number of epochs")
    parser.add_argument("--loss_fn",       default='MSE',                        type=str,   help="Loss function ('MSE' or 'L1')")
    parser.add_argument("--seeds",         default=None,                         type=list,  help="Random seeds (10,11,12)")
    parser.add_argument("--max_length",    default='1024',                       type=int,   help="max_length")
    parser.add_argument("--optimizer",     default='Adam',                       type=str,   help="Optimizer name ('Adam' or 'AdamW')")
    parser.add_argument("--weight_decay",  default='0.',                         type=float, help="Weight Decay")
    parser.add_argument("--momentum",      default='0.',                         type=float, help="Momentum")
    parser.add_argument("--max_tokens",    default='15000',                      type=int,   help="max_tokens for MSA")
    args = parser.parse_args()
    return args

def argparser_tester():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_file",   default=os.getcwd() + "/config.yaml",          type=str,help="Config file")
    parser.add_argument("--snapshot_file", default=os.getcwd() + "/snapshots/snapshot.pt",type=str,help="Snapshot file")
    parser.add_argument("--model",         default='MSA_Finetuning',                      type=str,help="Model name")
    parser.add_argument("--max_tokens",    default='15000',                               type=int,help="max_tokens for MSA")
    parser.add_argument("--max_length",    default='1024',                                type=int, help="max_length")
    parser.add_argument("--output_dir",    default=os.getcwd(),                           type=str, help="Output dir")
    parser.add_argument("--dataset_dir",   default='datasets/S1465',                      type=str, help="Dataset dir")
    args = parser.parse_args()
    return args


def argparser_translator():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file",  default='datasets/S1465/train/databases/db_s1465.csv', type=str,  help="In")
    parser.add_argument("--output_file", default='datasets/S1465/train/translated_databases/tb_s1465.csv', type=str, help="Out")
    args = parser.parse_args()
    return args


# Function to load yaml configuration file
def load_config(confir_file):
    with open(confir_file) as file:
        config = yaml.safe_load(file)

    return config

