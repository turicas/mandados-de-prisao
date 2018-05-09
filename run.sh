#!/bin/bash

time scrapy runspider listagem.py \
	-s RETRY_TIMES=5 \
	-s LOG_LEVEL=INFO \
	-o listagem.jl

time scrapy runspider detalhes.py \
	-s RETRY_TIMES=5 \
	-s LOG_LEVEL=INFO \
	-o detalhes.jl
