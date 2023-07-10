OPENAI_API_KEY=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 python gen_judgment.py \
    --bench-name "lima_test" \
    --mode pairwise-all \
    --model-list lima-13b lima-wiki-13b lima-nowiki-13b \
    --parallel 2
