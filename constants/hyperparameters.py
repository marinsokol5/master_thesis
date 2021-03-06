VOCABULARY_SIZE = 20_000
EMBEDDING_SIZE = 400
MODEL_DIMENSION = 400  # 512
SOURCE_SEQUENCE_LENGTH = 512
TARGET_SEQUENCE_LENGTH = 256
SOURCE_MAX_NUMBER_OF_TOKENS = SOURCE_SEQUENCE_LENGTH
TARGET_MAX_NUMBER_OF_TOKENS = TARGET_SEQUENCE_LENGTH
BATCH_SIZE = 32
DROPOUT_PROBABILITY = 0.1
FEED_FORWARD_TRANSFORMER_LAYER_DIMENSION = 1024
NUMBER_OF_PROPERTIES = 5

NUMBER_OF_INPUT_REVIEWS = 3

SOURCE_MAX_NUMBER_OF_SUBWORDS = SOURCE_MAX_NUMBER_OF_TOKENS - 2 * NUMBER_OF_INPUT_REVIEWS # for every review for start and end token
TARGET_MAX_NUMBER_OF_SUBWORDS = TARGET_MAX_NUMBER_OF_TOKENS - 1 # either start or end token, target_input has start while target_output has end

PADDING_INDEX = 3
LEARNING_RATE = 6 * 10e-5






