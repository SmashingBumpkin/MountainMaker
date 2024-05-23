import torch
import Nadeem.config_local as config_local

if torch.backends.mps.is_available():
    DEVICE = "mps"
elif torch.cuda.is_available():
    DEVICE = "cuda"
else:
    DEVICE = "cpu"
TRAIN_DIR = config_local.TRAIN_DIR
VAL_DIR = config_local.VAL_DIR
LEARNING_RATE_DISC = 5e-5
LEARNING_RATE_GEN = 1e-4
BATCH_SIZE = 2
NUM_WORKERS = 2
IMAGE_SIZE = 256
CHANNELS_IMG = 3
L1_LAMBDA = 100
LAMBDA_GP = 10
DISC_BETA1 = 0.5
DISC_BETA2 = 0.99
GEN_BETA1 = 0.5
GEN_BETA2 = 0.99
NUM_EPOCHS = 500
SAVE_INTERVAL = 15
LOAD_MODEL = True
SAVE_MODEL = True
CHECKPOINT_DISC = config_local.CHECKPOINT_DISC
CHECKPOINT_GEN = config_local.CHECKPOINT_GEN
LOAD_DISC = config_local.LOAD_DISC
LOAD_GEN = config_local.LOAD_GEN
EVALUATION_GEN = config_local.EVALUATION_GEN
SAMPLE_FOLDER = config_local.SAMPLE_FOLDER
