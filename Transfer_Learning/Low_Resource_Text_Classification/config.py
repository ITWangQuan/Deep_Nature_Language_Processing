import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--train_split', type=int, default=1000,help='train file split')
parser.add_argument('--num_steps', type=int, default=10000,help='estimator train steps per epoch')
parser.add_argument('--num_sampled', type=int, default=2000,help='The number of classes to randomly sample per batch')
parser.add_argument('--pretrain', type=bool, default=True,help='pretraining the model by using LM')
parser.add_argument('--allow_emb', type=bool, default=True,help='load embedding')
parser.add_argument('--split', type=int, default=0.9,help='test/train split ratio')
parser.add_argument('--clf', type=str, default="clstm",help='Type of classifiers. Default: c-lstm. You have three choices: [cnn, lstm, clstm]')
parser.add_argument('--data_path', type=str, default="./data/original_data/",help='original data')
parser.add_argument('--save_path', type=str, default="./data/processed_data/", help='processed data')
parser.add_argument('--model_path', type=str, default="./model/saved_model/", help='dir to save model')
parser.add_argument('--result_path', type=str, default="./result/", help='dir to save result')
parser.add_argument('--index_path', type=str, default="./embedding/",help='save word index ')
parser.add_argument('--log_path', type=str, default="./logs/",help='logs to save ')
parser.add_argument('--batch_size', type=int, default=50,help='size of word embeddings')
parser.add_argument('--max_len', type=int, default=80,help='max sentence length')
parser.add_argument('--num_class', type=int, default=4,help='number of classes')
parser.add_argument('--l2', help='L2 normalization constant', type=float, default=0.0001)
parser.add_argument('--filter_sizes', type=str, default="3,4,5",help='CNN filter sizes. For CNN, C-LSTM.')
parser.add_argument('--num_filters', type=int, default=128 , help='Number of filters per filter size. For CNN, C-LSTM.')
parser.add_argument('--hidden_size', type=int, default=128 ,help='Number of hidden units in the LSTM cell. For LSTM, Bi-LSTM')
parser.add_argument('--embedding_size', type=int, default=200 , help='embedding size for words')
parser.add_argument('--nlayers', type=int, default=3,help='number of layers')
parser.add_argument('--decay_factor', type=float, default=0.95)
parser.add_argument('--lr', type=float, default=0.0005)
parser.add_argument('--decay_size', type=float, default=3000)
parser.add_argument('--grad_clip', type=float, default=5.0)
parser.add_argument('--moving_average_decay', type=float, default=0.99)
parser.add_argument('--n_epochs', type=int, default=5,help='upper epoch limit')
parser.add_argument('--dropout', type=float, default=0.4,help='dropout applied to layers (0 = no dropout)')

args = parser.parse_args()

