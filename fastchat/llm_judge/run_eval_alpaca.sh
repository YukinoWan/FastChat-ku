python gen_alpaca_answer.py \
    --base_model "/home/zhen/models/alpaca-lora-13b"\
    --model_id alpaca-lora-13b\
    --benchmark lima_test\
    --with_prompt \
    --gpus 0 \
    --max_new_tokens 1024 \
